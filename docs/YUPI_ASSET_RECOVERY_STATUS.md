# YUPI ASSET RECOVERY STATUS

> Laatste update: 2026-10-01  
> Protocol: `docs/MICHEL_AI_ASSET_RECOVERY_PROTOCOL.md`  
> Status: **in uitvoering — exacte bronnen teruggevonden en technisch gevalideerd; repo-binaries nog te plaatsen**

## Samenvatting

De eerder foutief als volledig `approved` geregistreerde Yupi-imageassets zijn teruggezet naar de tijdelijke status `approved_pending_binary` zolang de echte imagebinary nog niet op het canonieke GitHub-pad staat.

Exacte bronnen zijn teruggevonden voor:

- Pup: 3 imageassets;
- Teen: 17 imageassets;
- Adult: 4 imageassets.

Totaal: **24 exacte goedgekeurde imagebronnen**.

Alle teruggevonden bestanden zijn technisch geopend/gedecodeerd. Voor Teen en Adult komen de berekende SHA-256 hashes exact overeen met de reeds geregistreerde manifest-hashes. Voor Pup zijn de hashes nu opnieuw berekend uit de teruggevonden oorspronkelijke bronnen en in het manifest vastgelegd.

Er is **niets opnieuw gegenereerd**.

## Pup — teruggevonden exacte bronnen

| Asset | Canoniek repo-pad | SHA-256 | Bron |
|---|---|---|---|
| base design | `assets/yupi/pup/design/approved/base-reference.jpeg` | `10cdb7a1a237ac830199e2a7f593b327971f8f4afa1850953678f5674d3d101e` | `75F1FA34-806F-4C92-8B3A-75224D88A121.jpeg` |
| sitting front | `assets/yupi/pup/poses/sitting/front.png` | `437cb34f25cb36931fcc48198fa0fd06bc57617fae2708d08f35b2dac5ee56c4` | `Vrolijke eenbenige puppy Yupi.png` |
| standing bark front | `assets/yupi/pup/poses/standing-bark/front.png` | `537d3a098c54fb2339461cf64d7c1ff83efc992c50c5da146172c8164b32a58e` | `Vrolijke Driepotige Blaffende Pup.png` |

Technische decode:

- base: JPEG 1122×1402;
- sitting: PNG 1198×1313;
- standing bark: PNG 1199×1312.

## Teen — 17 bronnen gevalideerd

De volgende canonieke paden zijn in het manifest vastgelegd en hebben een teruggevonden bron met exact overeenkomende SHA-256:

- `poses/playful-with-ball/reference.png`
- `expressions/head/emotion-sheet.png`
- `expressions/head/happy.png`
- `expressions/head/sad.png`
- `expressions/head/angry.png`
- `expressions/head/surprised.png`
- `expressions/head/scared.png`
- `expressions/head/determined.png`
- `expressions/head/curious.png`
- `expressions/head/playful.png`
- `poses/standing/front.png`
- `poses/standing/right.png`
- `poses/standing/left.png`
- `poses/standing/top.png`
- `poses/standing/bottom.png`
- `poses/playful-ball-action/low-front-action.png`
- `poses/balancing-hindlegs/top.png`

De precieze bronpaden, Library file IDs, hashes, afmetingen en approval-basis staan in `assets/yupi/teen/asset-manifest.json`.

## Adult — 4 bronnen gevalideerd

De volgende canonieke paden zijn geregistreerd:

- `design/approved/base.png`
- `poses/sitting/reference.png`
- `poses/running/reference.png`
- `poses/sniffing/reference.png`

Alle vier bronnen openen technisch correct en hun SHA-256 komt exact overeen met het bestaande Adult-manifest.

## Wat nog ontbreekt

De resterende herstelstap is fysiek: de 24 exacte binaries moeten op hun geregistreerde canonieke paden in GitHub worden geplaatst.

Pas daarna:

1. repo-bestand opnieuw hashen;
2. hash vergelijken met manifest;
3. status per asset wijzigen van `approved_pending_binary` naar `approved`;
4. `recovery_status` per levensfase op `complete` zetten;
5. CI-validatie opnieuw draaien;
6. herstel afsluiten in `AI_JOHAN.md`.

## Beveiliging tegen herhaling

Toegevoegd:

- `scripts/validate_yupi_assets.py`;
- `.github/workflows/yupi-asset-validation.yml`;
- uitgebreid `docs/YUPI_ASSET_PIPELINE.md` voor Pup + Teen + Adult.

De validator controleert echte repo-paden en hashes voor `approved` assets en voorkomt dat een manifest met `recovery_status: complete` nog pending binaries bevat.

## Tijdelijke harde regel

Tot dit document als voltooid is bijgewerkt:

> **Geen nieuwe canonieke Yupi-assets genereren.**
