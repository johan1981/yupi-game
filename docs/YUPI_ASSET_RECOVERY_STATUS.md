# YUPI ASSET RECOVERY STATUS

> Laatste update: 2026-10-01  
> Protocol: `docs/MICHEL_AI_ASSET_RECOVERY_PROTOCOL.md`  
> Status: **VOLTOOID — 24/24 exacte approved imagebinaries hersteld en gevalideerd**

## Eindresultaat

De herstelactie is afgerond.

- **Pup: 3/3 hersteld — complete**
- **Teen: 17/17 hersteld — complete**
- **Adult: 4/4 hersteld — complete**
- totaal: **24/24 exacte goedgekeurde imagebinaries staan daadwerkelijk in GitHub**
- geen van deze assets is opnieuw gegenereerd
- alle drie manifests hebben `recovery_status: complete`
- de automatische Yupi asset validation is succesvol geslaagd nadat de laatste Teen-binaries zijn gepromoveerd

## Pup

De drie corrupte/afgekapt opgeslagen bestanden zijn vervangen door de exacte oorspronkelijke goedgekeurde bronnen:

| Asset | Canoniek repo-pad | SHA-256 |
|---|---|---|
| base design | `assets/yupi/pup/design/approved/base-reference.jpeg` | `10cdb7a1a237ac830199e2a7f593b327971f8f4afa1850953678f5674d3d101e` |
| sitting front | `assets/yupi/pup/poses/sitting/front.png` | `437cb34f25cb36931fcc48198fa0fd06bc57617fae2708d08f35b2dac5ee56c4` |
| standing bark front | `assets/yupi/pup/poses/standing-bark/front.png` | `537d3a098c54fb2339461cf64d7c1ff83efc992c50c5da146172c8164b32a58e` |

De oude corrupte bestanden zijn uit de canonieke mappen verwijderd:

- `design/approved/base-reference.jpg`
- `poses/sitting/front.webp`
- `poses/standing-bark/front.webp`

## Teen

Alle 17 goedgekeurde Teen-assets staan als echte binaries op de canonieke repo-paden:

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

### Head-expressions

De acht losse hoofdexpressies zijn exact deterministisch teruggewonnen uit de goedgekeurde `emotion-sheet.png`.

Dit was **uitsluitend cropping van de bestaande approved bron**, geen regeneratie. Iedere output is tegen de reeds geregistreerde SHA-256 gecontroleerd en exact gelijk bevonden.

Recovery utility:

- `scripts/recover_yupi_teen_heads.py`

### Standing right en top

De laatste twee Teen-bronnen zijn uiteindelijk eveneens als exacte originele bytes in GitHub gezet:

- `assets/yupi/teen/poses/standing/right.png`
  - SHA-256 `3ff031577422e75f3eaf6e567a20cdafb441328a1a1ea01ce9ef7cc6941c22f8`
- `assets/yupi/teen/poses/standing/top.png`
  - SHA-256 `da434d4aedd84156530691067f605deac930e45a050e883c93a0d9b099abd21c`

Geen vervangende generatie of conversie gebruikt.

## Adult

Alle vier exact goedgekeurde Adult-bronnen staan als echte binaries in GitHub:

- `assets/yupi/adult/design/approved/base.png`
- `assets/yupi/adult/poses/sitting/reference.png`
- `assets/yupi/adult/poses/running/reference.png`
- `assets/yupi/adult/poses/sniffing/reference.png`

Hun repo-binaries corresponderen met de geregistreerde SHA-256 hashes.

## Automatische beveiliging

Actief:

- `scripts/validate_yupi_assets.py`
- `.github/workflows/yupi-asset-validation.yml`
- uitgebreid `docs/YUPI_ASSET_PIPELINE.md`

De validator controleert repo-paden en SHA-256 voor `approved` assets en voorkomt dat een levensfase met `recovery_status: complete` nog pending binaries bevat.

De validatie na voltooiing van Teen is **success**.

## Werkregel vanaf nu

De tijdelijke totale generatieblokkade uit de herstelperiode is opgeheven, maar de normale harde pre-image regel blijft gelden:

> **Voor iedere nieuwe canonieke Yupi-generatie eerst de echte relevante approved repo-afbeelding als visuele referentie gebruiken.**
>
> **Niet genereren op basis van alleen JSON, bestandsnamen of chatgeheugen.**
>
> **Nieuwe approval = echte repo-binary + correcte SHA-256 + geslaagde validatie.**
