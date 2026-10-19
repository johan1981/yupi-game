# AGENTS.md — Yupi game

## Werkwijze voor AI-assistenten

Bij **ieder ontwikkelverzoek**, ook in een nieuwe chat:

1. Controleer de actuele standaardbranch, relevante code en tests van deze repository.
2. Lees [de gedeelde AI-samenwerkingsstandaard](docs/AI_COLLABORATION_STANDARD.md) en [de repository-workflow](docs/DEVELOPMENT_WORKFLOW.md).
3. Lees de hieronder genoemde **inhoudelijke projectbronnen**; die gaan boven de generieke samenwerkingstekst voor productinhoud, beveiliging en canon.
4. Maak geen ongevraagde setup, reset, migratie, package-installatie, productie-deploy of ingrijpende refactor.
5. Voor wijzigingen: featurebranch, upstream/tracking, kleine diff, gerichte tests en **geen PR/merge zonder expliciete toestemming van Johan**.
6. Geef de benodigde commando's per werkelijk gebruikte omgeving: lokale Git-terminal, eventuele server, browser/game/testomgeving. Geen stappen verzinnen.

**Belangrijk:** workflow van Livome Intern (PhpStorm op Windows → SFTP → Ubuntu) is **niet automatisch** de workflow van deze repo. Controleer de eigen workflow; onbekende onderdelen blijven te verifiëren.

## Harde product-/assetbronnen

- [docs/YUPI_GAME_BIBLE.md](docs/YUPI_GAME_BIBLE.md): gamecanon.
- [AI_JOHAN.md](AI_JOHAN.md): verplichte handoff Johan-AI ↔ Michel-AI.
- [docs/characters/YUPI_SPEC.md](docs/characters/YUPI_SPEC.md) en [docs/characters/YUPI_SPEC.json](docs/characters/YUPI_SPEC.json): anatomie.
- [docs/IMAGE_GENERATION_PROTOCOL.md](docs/IMAGE_GENERATION_PROTOCOL.md) voor beelden; [docs/YUPI_ASSET_PIPELINE.md](docs/YUPI_ASSET_PIPELINE.md) voor goedkeuren/opslaan.

Geen nieuwe afbeeldingen zonder voorafgaande specificatiecontrole; geen ongekeurde assets als definitief behandelen. Geen automatische spiegeling. GitHub Pages vanaf `main` is onderdeel van de repo, niet een Ubuntu/PHP-runtime.
