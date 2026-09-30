# YUPI ASSET RECOVERY STATUS

> Laatste update: 2026-10-01  
> Protocol: `docs/MICHEL_AI_ASSET_RECOVERY_PROTOCOL.md`  
> Status: **22/24 imagebinaries hersteld; 2 Teen-views nog pending**

## Samenvatting

De herstelronde heeft de eerder foutieve Library-only toestand grotendeels gerepareerd.

Exacte goedgekeurde bronnen zijn teruggevonden voor alle 24 betrokken assets. Er is niets opnieuw gegenereerd.

Huidige repo-status:

- **Pup: 3/3 hersteld — recovery complete**
- **Adult: 4/4 hersteld — recovery complete**
- **Teen: 15/17 hersteld — 2 binaries pending**
- totaal: **22/24 exacte imagebinaries staan nu echt op hun canonieke GitHub-pad**

De automatische Yupi asset validation draait en is na promotie van Pup, Teen en Adult succesvol afgerond.

## Pup — compleet

De drie corrupte/afgekapt opgeslagen bestanden zijn vervangen door de exacte oorspronkelijke goedgekeurde bronnen:

| Asset | Canoniek repo-pad | SHA-256 |
|---|---|---|
| base design | `assets/yupi/pup/design/approved/base-reference.jpeg` | `10cdb7a1a237ac830199e2a7f593b327971f8f4afa1850953678f5674d3d101e` |
| sitting front | `assets/yupi/pup/poses/sitting/front.png` | `437cb34f25cb36931fcc48198fa0fd06bc57617fae2708d08f35b2dac5ee56c4` |
| standing bark front | `assets/yupi/pup/poses/standing-bark/front.png` | `537d3a098c54fb2339461cf64d7c1ff83efc992c50c5da146172c8164b32a58e` |

De drie oude corrupte bestanden zijn uit de canonieke mappen verwijderd:

- `design/approved/base-reference.jpg`
- `poses/sitting/front.webp`
- `poses/standing-bark/front.webp`

Pup manifest: `recovery_status: complete`.

## Adult — compleet

Alle vier exact goedgekeurde Adult-bronnen staan nu als echte binaries in GitHub:

- `assets/yupi/adult/design/approved/base.png`
- `assets/yupi/adult/poses/sitting/reference.png`
- `assets/yupi/adult/poses/running/reference.png`
- `assets/yupi/adult/poses/sniffing/reference.png`

Hun repo-binaries corresponderen met de reeds geregistreerde SHA-256 hashes.

Adult manifest: `recovery_status: complete`.

## Teen — 15/17 hersteld

Hersteld en als `approved` gepromoveerd:

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
- `poses/standing/left.png`
- `poses/standing/bottom.png`
- `poses/playful-ball-action/low-front-action.png`
- `poses/balancing-hindlegs/top.png`

### Head-crops

De acht losse hoofdexpressies zijn exact en deterministisch teruggewonnen uit de goedgekeurde `emotion-sheet.png`.

Dit was **crop/compositing-herstel, geen regeneratie**. De recovery-script controleerde elke output tegen de reeds geregistreerde SHA-256; alle acht hashes waren exact gelijk.

Recovery utility:

- `scripts/recover_yupi_teen_heads.py`

### Nog pending: twee Teen-views

Alleen deze twee exacte binaries ontbreken nog op GitHub:

1. **standing right**
   - repo-pad: `assets/yupi/teen/poses/standing/right.png`
   - SHA-256: `3ff031577422e75f3eaf6e567a20cdafb441328a1a1ea01ce9ef7cc6941c22f8`
   - exacte Library-bron: `/Yupi Game/Assets/Yupi/teen/approved/views/teen-yupi-standing-right.png`
   - Library file ID: `libfile_aebec7bf42e48191a1abb5b9790ef74f`

2. **standing top**
   - repo-pad: `assets/yupi/teen/poses/standing/top.png`
   - SHA-256: `da434d4aedd84156530691067f605deac930e45a050e883c93a0d9b099abd21c`
   - exacte Library-bron: `/Yupi Game/Assets/Yupi/teen/approved/views/teen-yupi-top.png`
   - Library file ID: `libfile_0c177fd6de748191a9053578e80adfc5`

Deze twee blijven terecht `approved_pending_binary`. Ze worden niet vervangen door een nieuwe generatie.

Teen manifest blijft `recovery_status: in_progress` totdat beide exacte binaries zijn geplaatst en geverifieerd.

## Automatische beveiliging

Actief:

- `scripts/validate_yupi_assets.py`
- `.github/workflows/yupi-asset-validation.yml`
- uitgebreid `docs/YUPI_ASSET_PIPELINE.md`

De validator controleert repo-paden en SHA-256 voor `approved` assets en voorkomt dat een levensfase met `recovery_status: complete` nog pending binaries bevat.

De laatste validaties voor de herstelde Pup-, Teen- en Adult-manifests zijn **geslaagd**.

## Tijdelijke harde regel

Tot Teen eveneens `recovery_status: complete` heeft:

> **Geen nieuwe canonieke Yupi-assets genereren.**
