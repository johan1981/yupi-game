# YUPI ASSET RECOVERY STATUS

> Laatste update: 2026-10-01  
> Protocol: `docs/MICHEL_AI_ASSET_RECOVERY_PROTOCOL.md`  
> Status: **voltooid — 24/24 exacte imagebinaries hersteld**

## Samenvatting

De volledige herstelactie is afgerond.

- **Pup: 3/3 hersteld — recovery complete**
- **Teen: 17/17 hersteld — recovery complete**
- **Adult: 4/4 hersteld — recovery complete**
- totaal: **24/24 exacte goedgekeurde imagebinaries staan nu daadwerkelijk op hun canonieke GitHub-pad**

Er is tijdens deze herstelactie **niets opnieuw gegenereerd**. Alle assets zijn hersteld vanuit de exacte goedgekeurde bron of via deterministische crop/compositing uit een exact goedgekeurde bron, met SHA-256-controle.

## Pup — compleet

De drie corrupte/afgekapt opgeslagen bestanden zijn vervangen door de exacte oorspronkelijke goedgekeurde bronnen:

| Asset | Canoniek repo-pad | SHA-256 |
|---|---|---|
| base design | `assets/yupi/pup/design/approved/base-reference.jpeg` | `10cdb7a1a237ac830199e2a7f593b327971f8f4afa1850953678f5674d3d101e` |
| sitting front | `assets/yupi/pup/poses/sitting/front.png` | `437cb34f25cb36931fcc48198fa0fd06bc57617fae2708d08f35b2dac5ee56c4` |
| standing bark front | `assets/yupi/pup/poses/standing-bark/front.png` | `537d3a098c54fb2339461cf64d7c1ff83efc992c50c5da146172c8164b32a58e` |

De oude corrupte varianten zijn uit de canonieke mappen verwijderd.

Pup manifest: `recovery_status: complete`.

## Teen — compleet

Alle 17 Teen-assets zijn nu fysiek aanwezig en hash-geverifieerd.

De laatste twee ontbrekende binaries zijn exact toegevoegd:

1. `assets/yupi/teen/poses/standing/right.png`
   - SHA-256 bron: `3ff031577422e75f3eaf6e567a20cdafb441328a1a1ea01ce9ef7cc6941c22f8`
   - Git blob SHA: `f9d3a7daa5ad36d203fa0f39c94d92c4e1944b97`

2. `assets/yupi/teen/poses/standing/top.png`
   - SHA-256 bron: `da434d4aedd84156530691067f605deac930e45a050e883c93a0d9b099abd21c`
   - Git blob SHA: `f75ac3912166c22fb0f97cef599634e5c48aa60d`

Beide bestanden zijn vanuit de exact teruggevonden Library-bron als binary in GitHub geplaatst. Voor beide kwam de berekende Git blob SHA exact overeen met de vooraf berekende lokale blob SHA.

De acht losse hoofdexpressies zijn exact deterministisch teruggewonnen uit de goedgekeurde `emotion-sheet.png` en hun SHA-256 hashes kwamen exact overeen met de bestaande manifestwaarden.

Teen manifest: `recovery_status: complete`.

## Adult — compleet

Alle vier exact goedgekeurde Adult-bronnen staan als echte binaries in GitHub:

- `assets/yupi/adult/design/approved/base.png`
- `assets/yupi/adult/poses/sitting/reference.png`
- `assets/yupi/adult/poses/running/reference.png`
- `assets/yupi/adult/poses/sniffing/reference.png`

Adult manifest: `recovery_status: complete`.

## Beveiliging tegen herhaling

Actief:

- `scripts/validate_yupi_assets.py`
- `.github/workflows/yupi-asset-validation.yml`
- `docs/YUPI_ASSET_PIPELINE.md`

De validator controleert voor `approved` assets:

- echt repo-pad aanwezig;
- bestand niet leeg;
- juiste image-extensie;
- SHA-256 overeenkomst;
- geen Library-only asset die als volledig approved wordt voorgesteld.

Een levensfase mag alleen `recovery_status: complete` hebben als er geen `approved_pending_binary` entries meer zijn.

## Eindstatus

> **Yupi asset recovery: VOLTOOID.**
>
> Pup + Teen + Adult gebruiken voortaan de echte goedgekeurde visuele bronnen als canonieke referentie, niet alleen JSON of chatgeheugen.
