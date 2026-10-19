# Development workflow — Yupi game

**Repository:** `johan1981/yupi-game`  
**Standaardbranch:** `main` (GitHub, 19 oktober 2026)  
**Publicatie:** `README.md` beschrijft een mobiele webgame/PWA en GitHub Pages vanaf `main` / repositoryroot (`index.html`).

## Verplichte projectbronnen
- `docs/YUPI_GAME_BIBLE.md` is de game-/verhaalcanon.
- `AI_JOHAN.md` is de communicatie en handoff tussen Johan-AI en Michel-AI; **geen vervanging voor canon**.
- `docs/characters/YUPI_SPEC.md` en `docs/characters/YUPI_SPEC.json` zijn de verplichte visuele/anatomische toetssteen.
- Voor beeldgeneratie: eerst `docs/IMAGE_GENERATION_PROTOCOL.md`; voor goedgekeurde assets `docs/YUPI_ASSET_PIPELINE.md` en het bestaande manifest.

## Werken en publiceren
| Onderdeel | Werkwijze |
|---|---|
| Git | Featurebranches vanaf `main`; nieuwe remote branch lokaal tracken, daarna `git pull` op de actieve getrackte branch. |
| IDE en lokale map | **Nog te verifiëren**. Geen PhpStorm/SFTP of Ubuntu aannemen. |
| Runtime | Browser/PWA; game start bij `index.html`. Test iPhone-landscape en desktopgedrag na wijzigingen. |
| Publicatie | GitHub Pages vanaf `main` volgens README; featurebranch is geen automatisch gepubliceerde release. |
| Asset-validatie | Alleen echte goedgekeurde binaries naar canonieke assetpaden; anatomie en aanzichten vóór promotie controleren. |

## Algemene afspraken

Lees vóór iedere ontwikkeltaak [de Livome AI-samenwerkingsstandaard](AI_COLLABORATION_STANDARD.md), dit document en de bestaande projectbronnen. Eerst huidige default branch, code, tests, implementatie en eventuele openstaande wijzigingen onderzoeken.

- Werk voor nieuwe wijzigingen op een eigen `feature/...`- of `fix/...`-branch vanaf de actuele default branch. Remote featurebranches lokaal met upstream/tracking ophalen; daarna is op de juiste getrackte branch normaal `git pull` voldoende.
- Git in de **daadwerkelijk gebruikte lokale ontwikkelterminal**. Git op een server alleen als deze repository aantoonbaar zo is ingericht; kopieer niet automatisch de Livome Intern PhpStorm/SFTP-werkwijze.
- AI kan, indien toegestaan, op de remote featurebranch committen. **Geen PR of merge zonder uitdrukkelijke toestemming van Johan.**
- Geen ongevraagde dependencies, resets, schemawijzigingen, service-restarts, credentials of deployacties. Projectgegevens en reeds goedgekeurde assets beschermen.
- Geef Johan precies de noodzakelijke commando's met het juiste omgevingslabel, niet universeel Laravel/Ubuntu-commando's.
- Doe of vraag passende regressie- en functionele tests. Vermeld onbevestigde omgevingsinformatie expliciet als **nog te verifiëren**.

## Nieuwe remote branch (juiste lokale Git-terminal)
`git fetch origin` en `git switch --track origin/<featurebranch>`. Daarna alleen `git pull`. Na expliciete merge: `git switch main`, `git pull`.

## Bij samenwerken met Michel
Respecteer de lopende `AI_JOHAN.md`-overdrachtsregels. Stem wijzigingen aan gezamenlijk gebruikte assets en canon af met het bijbehorende projectprotocol. Geen automatische spritespiegeling of promotie van niet-gevalideerde afbeeldingen.
