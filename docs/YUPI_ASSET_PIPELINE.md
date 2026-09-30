# YUPI ASSET PIPELINE

> **STATUS: VERPLICHTE PROJECTWERKWIJZE**
>
> Deze workflow geldt voor **alle Yupi-levensfasen** onder `assets/yupi/<form>/`, momenteel `pup`, `teen` en `adult`.

## 1. Hoofdregel

Een afbeelding die alleen in chat of alleen in ChatGPT Library staat, is **geen volledig beheerde canonieke game-asset**.

Wanneer Michel of Johan expliciet zegt **vastleggen**, **vastzetten** of **opslaan**, wordt het goedgekeurde beeld in dezelfde werkstroom:

1. als exacte bron veiliggesteld;
2. als echte imagebinary onder de juiste canonieke map in GitHub geplaatst;
3. opgenomen in `assets/yupi/<form>/asset-manifest.json`;
4. voorzien van SHA-256;
5. technisch gedecodeerd/gevalideerd;
6. visueel gecontroleerd tegen de relevante goedgekeurde bron;
7. pas daarna op status `approved` gezet.

Library-opslag blijft waardevolle provenance/back-up, maar vervangt de repo-binary niet.

## 2. Statusmodel

### `approved`

Alle voorwaarden zijn waar:

- expliciet goedgekeurd door Michel of Johan;
- de exacte binary staat in GitHub;
- het manifest bevat het echte repo-pad;
- SHA-256 correspondeert met de goedgekeurde bron;
- technische decode is geslaagd;
- relevante anatomische/visuele validatie is geslaagd.

### `approved_pending_binary`

De exacte goedgekeurde bron is teruggevonden en geïdentificeerd, maar de binary staat nog niet correct in GitHub.

Deze status is tijdelijk. Een entry met deze status mag niet als complete canonieke repo-asset worden behandeld.

### `prototype`

Niet canoniek. Niet gebruiken als vaste visuele referentie.

## 3. Canonieke structuur

Iedere levensfase heeft een eigen root:

```text
assets/yupi/
├── pup/
│   ├── asset-manifest.json
│   ├── design/approved/
│   ├── poses/
│   ├── expressions/
│   ├── sprites/
│   ├── sheets/
│   ├── references/
│   └── archive/
├── teen/
│   ├── asset-manifest.json
│   ├── design/approved/
│   ├── poses/
│   ├── expressions/
│   ├── sprites/
│   └── archive/
└── adult/
    ├── asset-manifest.json
    ├── design/approved/
    ├── poses/
    ├── expressions/
    ├── sprites/
    └── archive/
```

Pup, Teen en Adult zijn **afzonderlijke visuele vormen**. Een pose voor Teen wordt gebaseerd op echte Teen-referenties; Adult op Adult; Pup op Pup.

## 4. Visuele bron vóór generatie

Voor iedere nieuwe canonieke Yupi-generatie moet de daadwerkelijke goedgekeurde referentie als beeld beschikbaar zijn.

Voorkeursvolgorde:

1. canonieke repo-binary;
2. exact dezelfde approved binary uit Library;
3. exact opnieuw aangeleverde approved bron.

Alleen JSON, bestandsnamen, hashes, beschrijvingen of chatgeheugen zijn onvoldoende.

**Geen echte visuele bron zichtbaar/toegankelijk = geen nieuwe canonieke Yupi-generatie.**

## 5. Canonieke paden

Voorbeelden:

```text
design/approved/base.png
poses/standing/front.png
poses/standing/right.png
poses/standing/left.png
poses/standing/top.png
expressions/head/happy.png
expressions/head/surprised.png
sprites/walk/right/frame-000.png
sprites/walk/left/frame-000.png
```

Gebruik bij herstel het oorspronkelijke goedgekeurde bestandsformaat wanneer conversie de bytes zou veranderen.

## 6. Naamconventie

- kleine letters;
- Engelse technische slugs;
- koppeltekens tussen woorden;
- frames: `frame-000.png`, `frame-001.png`, enz.;
- geen `final`, `latest`, `new`, `final2` in canonieke namen;
- versiehistorie hoort in Git.

## 7. Source versus runtime sprite

Een goedgekeurde pose is eerst een canonieke bronasset.

Voor gameplay mag daar een runtime sprite van worden afgeleid. Die runtime sprite:

- behoudt exact hetzelfde ontwerp;
- verandert Yupi's anatomie niet;
- heeft binnen één sequence consistente canvasmaat en baseline;
- krijgt een manifestkoppeling naar de bronasset.

## 8. Richtingen en asymmetrie

Yupi is asymmetrisch.

- rechter voorpoot aanwezig;
- linker voorpoot volledig afwezig tot de schouder;
- rechter oor rechtop;
- linker oor hangend;
- geen automatische spiegeling.

`walk/right` en `walk/left` zijn dus afzonderlijke assets wanneer richting relevant is.

## 9. Vier aanzichten en sheets

1. elk aanzicht afzonderlijk maken/herstellen;
2. elk aanzicht afzonderlijk goedkeuren en opslaan;
3. daarna de exacte bestanden compositen;
4. niet opnieuw genereren om een sheet te maken;
5. niet spiegelen.

Een sheet vervangt nooit de losse approved bronnen.

## 10. Manifest

`asset-manifest.json` is de machineleesbare index, niet de visuele bron zelf.

Een canonieke image-entry bevat minimaal:

- uniek `id`;
- `type`;
- betekenis/actie/emotie;
- view/richting indien relevant;
- `path`;
- `status`;
- `sha256`;
- `mime_type`;
- provenance naar de exacte goedgekeurde bron.

## 11. Automatische validatie

Lokaal:

```bash
python scripts/validate_yupi_assets.py
```

CI draait dezelfde controle.

Voor `approved` controleert de validator minimaal:

- repo-pad bestaat;
- bestand is niet leeg;
- image-extensie klopt voor image-assets;
- SHA-256 klopt wanneer in manifest geregistreerd;
- een asset staat niet alleen als Library-verwijzing geregistreerd.

`approved_pending_binary` wordt als herstelstatus gerapporteerd, niet als volledig approved.

Wanneer een manifest `recovery_status: complete` meldt, zijn pending binaries niet meer toegestaan.

## 12. Verplichte repo-check vóór beeldwerk

Altijd raadplegen:

- `docs/YUPI_GAME_BIBLE.md`;
- `AI_JOHAN.md`;
- `docs/IMAGE_GENERATION_PROTOCOL.md`;
- `docs/characters/YUPI_SPEC.md`;
- `docs/characters/YUPI_SPEC.json`;
- het relevante `asset-manifest.json`;
- de echte goedgekeurde visuele referentie.

## 13. Golden rule

> **GOEDGEKEURD = EXPLICIETE GOEDKEURING + ECHTE REPO-BINARY + JUISTE HASH + GESLAAGDE VALIDATIE.**
>
> **JSON/LIBRARY ALLEEN IS NIET GENOEG.**
