#!/usr/bin/env python3
"""Recover exact Teen Yupi head crops from the approved emotion sheet.

This is a deterministic crop only. No image generation or redraw is performed.
The output hashes are checked against the approved manifest hashes.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/yupi/teen/expressions/head/emotion-sheet.png"
OUTDIR = ROOT / "assets/yupi/teen/expressions/head"

CROPS = {
    "happy": ((0, 60, 280, 650), "4d7e3a18da4c3ea105e2eb2086892a40a4f38c703babaa10f7d29679f632568c"),
    "sad": ((280, 60, 560, 650), "ecfcee46c25e8d62d8d4e67dfd92602811dffc04aeca37d12e54cb221c0be896"),
    "angry": ((560, 60, 840, 650), "3c95003d015e956e6e21a8bb717f4d6933c7f3edeb847450c92eaf5b01f7be4a"),
    "surprised": ((840, 60, 1122, 650), "624696f175fd2517ac47e911a2734245d030d03b7b6e62fad8e7d4c88bcfbacf"),
    "scared": ((0, 690, 280, 1325), "dca01c1febfef6367b6824e1ce22edb914510e20ceb2f77dc8c1f46fc70994e3"),
    "determined": ((280, 690, 560, 1325), "5be997f0cd54c8bd3fa0f613097047dcccc29cdae3a1195562d0bb5d894cc597"),
    "curious": ((560, 690, 840, 1325), "343c20bcac772ab54d31d88a98d51e2c843a42494434cf0e8a94fd3bbedb1e14"),
    "playful": ((840, 690, 1122, 1325), "90cd24b851322eecb1d150a4b62bf81073cffc94da6dd027534be1c125b27bca"),
}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Missing approved source sheet: {SOURCE}")

    OUTDIR.mkdir(parents=True, exist_ok=True)

    with Image.open(SOURCE) as sheet:
        for emotion, (box, expected) in CROPS.items():
            out = OUTDIR / f"{emotion}.png"
            sheet.crop(box).save(out)
            actual = digest(out)
            if actual != expected:
                raise SystemExit(
                    f"{emotion}: SHA-256 mismatch after deterministic crop: "
                    f"expected {expected}, got {actual}"
                )
            print(f"OK {emotion}: {actual}")


if __name__ == "__main__":
    main()
