#!/usr/bin/env python3
"""Validate canonical Yupi assets against their manifests."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = [
    ROOT / "assets/yupi/pup/asset-manifest.json",
    ROOT / "assets/yupi/teen/asset-manifest.json",
    ROOT / "assets/yupi/adult/asset-manifest.json",
]
IMAGE_TYPES = {"design", "pose", "expression", "expression_sheet"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".svg"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    pending_total = 0

    for manifest_path in MANIFESTS:
        if not manifest_path.exists():
            errors.append(f"missing manifest: {manifest_path.relative_to(ROOT)}")
            continue

        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        form = data.get("form", manifest_path.parent.name)
        pending_here = 0

        for asset in data.get("approved_assets", []):
            asset_id = asset.get("id", "<missing-id>")
            status = asset.get("status")
            rel = asset.get("path")
            is_image = asset.get("type") in IMAGE_TYPES

            if status == "approved_pending_binary":
                pending_total += 1
                pending_here += 1
                if not asset.get("sha256"):
                    errors.append(f"{form}/{asset_id}: pending image has no sha256")
                source = asset.get("persistent_source")
                if not source:
                    errors.append(f"{form}/{asset_id}: pending image has no persistent_source provenance")
                continue

            if status != "approved":
                continue

            if not rel:
                errors.append(f"{form}/{asset_id}: approved asset has no repo path")
                continue

            path = ROOT / rel
            if not path.exists():
                errors.append(f"{form}/{asset_id}: approved path missing: {rel}")
                continue
            if path.stat().st_size == 0:
                errors.append(f"{form}/{asset_id}: approved file is empty: {rel}")
                continue

            if is_image and path.suffix.lower() not in IMAGE_EXTENSIONS:
                errors.append(f"{form}/{asset_id}: approved image has unexpected extension: {rel}")

            expected = asset.get("sha256")
            if expected:
                actual = sha256(path)
                if actual.lower() != expected.lower():
                    errors.append(
                        f"{form}/{asset_id}: sha256 mismatch: expected {expected}, got {actual}"
                    )
            elif is_image:
                warnings.append(f"{form}/{asset_id}: approved image has no sha256 yet")

        if data.get("recovery_status") == "complete" and pending_here:
            errors.append(
                f"{form}: recovery_status is complete but {pending_here} asset(s) are still approved_pending_binary"
            )

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    print(f"Yupi asset validation: {pending_total} pending binary asset(s), {len(errors)} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
