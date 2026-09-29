# YUPI ASSET PIPELINE

> **STATUS: VERPLICHTE PROJECTWERKWIJZE**
>
> Deze workflow geldt voor alle Yupi Pup-assets in `assets/yupi/pup/`.

## 1. Hoofdregel

Een afbeelding die alleen in een chat staat, is **geen beheerde game-asset**.

Wanneer Michel of Johan expliciet zegt **vastleggen**, **vastzetten** of **opslaan**, wordt het goedgekeurde beeld in dezelfde werksessie:

1. als goedgekeurde bron in de juiste map onder `assets/yupi/pup/` geplaatst;
2. opgenomen of bijgewerkt in `assets/yupi/pup/asset-manifest.json`;
3. indien bedoeld voor gameplay, omgezet naar of gekoppeld aan een game-ready sprite/sequence;
4. indien onderdeel van een vier-aanzichten-set, gekoppeld aan de andere afzonderlijk goedgekeurde aanzichten.

Een goedgekeurde asset mag dus niet alleen in chatgeheugen blijven bestaan.

## 2. Canonieke structuur

```text
assets/yupi/pup/
├── README.md
├── asset-manifest.json
├── design/
│   └── approved/
│       └── base-sheet.png
├── poses/
├── expressions/
├── sprites/
│   └── _prototype/
├── sheets/
└── archive/
    ├── legacy-v1/
    └── experiments/
```

### design/approved
Alleen het actuele goedgekeurde basisontwerp.

### poses
Goedgekeurde volledige poses per betekenis en camerastandpunt:

```text
poses/determined/front.png
poses/determined/right.png
poses/determined/left.png
poses/determined/back.png
```

### expressions
Goedgekeurde hoofd-/emotie-assets:

```text
expressions/head/happy.png
expressions/head/surprised.png
```

Voor emoties met meerdere camerastandpunten:

```text
expressions/angry-bark/front.png
expressions/angry-bark/right.png
expressions/angry-bark/left.png
expressions/angry-bark/back.png
```

### sprites
Definitieve game-ready animatieframes:

```text
sprites/walk/right/frame-000.png
sprites/walk/right/frame-001.png
sprites/walk/left/frame-000.png
sprites/run/right/frame-000.png
sprites/run/left/frame-000.png
```

Links en rechts zijn afzonderlijke assets. **Nooit automatisch spiegelen.**

### sprites/_prototype
Technische tests die nog niet als definitieve sprite zijn goedgekeurd. Prototype is nadrukkelijk geen canon.

### sheets
Overzichten die door compositing uit reeds goedgekeurde losse beelden worden opgebouwd. **Geen regeneration.**

### archive
Oude of experimentele bestanden. Niet automatisch als actuele referentie gebruiken.

## 3. Naamconventie

- kleine letters;
- Engelse technische slugs;
- koppeltekens tussen woorden;
- frames: `frame-000.png`, `frame-001.png`, enzovoort;
- geen `final`, `latest`, `new`, `final2` of losse versienummers in canonieke namen.

Versiehistorie hoort in Git.

## 4. Goedkeuring

De woorden **vastleggen**, **vastzetten** en **opslaan** betekenen bij een duidelijk benoemd beeld dat de asset is goedgekeurd.

| Type | Canonieke plek |
|---|---|
| basisontwerp | `design/approved/` |
| statische pose | `poses/<pose>/<view>.png` |
| hoofd/emotie | `expressions/...` |
| animatieframes | `sprites/<action>/<direction>/frame-NNN.png` |
| samengesteld overzicht | `sheets/` |

## 5. Source versus runtime sprite

Een goedgekeurde pose is eerst een canonieke bronasset.

Als die pose in gameplay wordt gebruikt, mag daar een runtime sprite van worden afgeleid. De runtime sprite:
- gebruikt PNG met transparante achtergrond waar mogelijk;
- behoudt exact hetzelfde ontwerp;
- heeft binnen één sequence dezelfde canvasmaat;
- gebruikt een consistente grond-/voetbaseline;
- verandert de anatomie niet;
- wordt in het manifest aan de bronasset gekoppeld.

## 6. Animaties

Iedere richting krijgt een eigen sequence wanneer richting relevant is.

Voor Yupi:
- `walk/right` en `walk/left` zijn afzonderlijk;
- `run/right` en `run/left` zijn afzonderlijk;
- draaien kan eigen overgangsframes krijgen;
- definitieve Yupi-characterart gebruikt geen CSS-`scaleX` als vervanging voor een ontbrekende richting.

## 7. Manifest

`asset-manifest.json` is de machineleesbare index.

Elke canonieke goedgekeurde asset krijgt minimaal:
- uniek `id`;
- `type`;
- betekenis/actie/emotie;
- view of direction;
- pad;
- status `approved`;
- bron/runtime-relatie indien relevant.

## 8. Vier aanzichten

1. front los maken → goedkeuren → opslaan;
2. right los maken → goedkeuren → opslaan;
3. left los maken → goedkeuren → opslaan;
4. back los maken → goedkeuren → opslaan;
5. daarna exact deze vier bestanden compositen.

## 9. Verplichte repo-check

Voor nieuwe Yupi-assets gelden ook:
- `docs/IMAGE_GENERATION_PROTOCOL.md`
- `docs/characters/YUPI_SPEC.md`
- `docs/characters/YUPI_SPEC.json`

## 10. Golden rule

> **GOEDGEKEURD IN CHAT = DIRECT BEHEERD IN DE REPO.**
>
> **CANONIEKE ASSET = VASTE NAAM + VASTE MAP + MANIFEST-ENTRY.**
