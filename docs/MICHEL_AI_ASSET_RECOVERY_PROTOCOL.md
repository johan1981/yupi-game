# MICHEL-AI ASSET RECOVERY & VISUAL CONSISTENCY PROTOCOL

> **Status: herstelprotocol / direct toepassen**
>
> Doel: de goedgekeurde Yupi-assets daadwerkelijk veiligstellen in de repository en voorkomen dat toekomstige beelden visueel afwijken van reeds goedgekeurde ontwerpen.

## 1. Waarom dit bestand bestaat

Op 2026-09-30 is vastgesteld dat een groot deel van de goedgekeurde Teen- en Adult-Yupi-assets in de repository alleen als metadata/JSON is geregistreerd.

De huidige situatie op `main`:

- `assets/yupi/teen/asset-manifest.json` bevat **17 approved assets**;
- onder `assets/yupi/teen/` staan **0 echte PNG/JPG/WebP-afbeeldingen**;
- `assets/yupi/adult/asset-manifest.json` bevat **4 approved assets**;
- onder `assets/yupi/adult/` staan **0 echte PNG/JPG/WebP-afbeeldingen**;
- meerdere `approved-source.json`-bestanden verwijzen naar bestanden in ChatGPT Library;
- `assets/nexus-breuk/session-2026-09-30/README.md` noemt meerdere gegenereerde beelden die eveneens niet als binaries in GitHub staan.

Dit betekent dat **Library-opslag en repo-opslag ten onrechte als hetzelfde zijn behandeld**.

De bestaande projectregel blijft leidend:

> **GOEDGEKEURD IN CHAT = DIRECT BEHEERD IN DE REPO.**

Een Library-bestand is waardevolle bronopslag/provenance, maar vervangt het canonieke imagebestand in GitHub niet.

## 2. Tijdelijke herstelregel

Totdat Teen en Adult volledig zijn hersteld:

**Geen nieuwe canonieke Yupi-designs, poses, expressions, turnaround-views of sprites genereren.**

Technische experimenten mogen alleen wanneer expliciet als prototype benoemd en buiten de approved/canonical folders gehouden.

Reden: eerst de bestaande, reeds goedgekeurde visuele waarheid veiligstellen voordat nieuwe varianten worden toegevoegd.

## 3. Herstelprocedure per ontbrekende approved asset

Voor iedere approved asset in de Teen- en Adult-manifests:

1. Lees de bestaande manifest-entry en/of `approved-source.json`.
2. Haal het **exacte reeds goedgekeurde bronbestand** terug uit de daar geregistreerde ChatGPT Library-bron.
3. **Niet opnieuw genereren.** De oorspronkelijke goedgekeurde bytes hebben voorrang.
4. Bereken SHA-256 van het teruggehaalde bestand.
5. Vergelijk die hash met de SHA-256 die al in het manifest staat.
6. Alleen bij exacte match mag het bestand als dezelfde approved asset worden beschouwd.
7. Commit het daadwerkelijke imagebestand naar een canoniek pad onder `assets/yupi/<form>/...`.
8. Werk het manifest bij met een echte repository-`path`.
9. Behoud Library-pad, `library_file_id`, oorspronkelijke bestandsnaam en hash als provenance/back-up metadata.
10. Controleer na commit dat het genoemde repo-pad werkelijk bestaat.

### Geen vervangende regeneratie

Wanneer een approved bronbestand uit Library nog bereikbaar is, mag ontbrekende repo-opslag **nooit** worden opgelost door een "zo goed mogelijk gelijkende" nieuwe generatie.

Dat zou een nieuwe asset zijn en vereist nieuwe expliciete goedkeuring.

## 4. Statusmodel

Vanaf nu betekent:

### `approved`

Alle onderstaande voorwaarden zijn waar:

- expliciet goedgekeurd door Johan of Michel;
- exacte imagebinary staat in GitHub;
- manifest bevat het echte repo-pad;
- SHA-256 van het repo-bestand correspondeert met de geregistreerde approved bron;
- visuele/anatomische validatie is geslaagd.

### `approved_pending_binary`

De asset is inhoudelijk goedgekeurd en de exacte bron is bekend, maar de imagebinary staat nog niet in GitHub.

Deze status is tijdelijk en moet worden hersteld.

### `prototype`

Niet canoniek. Mag niet als vaste visuele referentie worden gebruikt.

**Een Library-path of JSON-bestand alleen is onvoldoende voor status `approved`.**

## 5. Aanbevolen canonieke structuur

Voorbeeld Teen Yupi:

```text
assets/yupi/teen/
├── asset-manifest.json
├── design/
│   └── approved/
│       └── base.png
├── poses/
│   ├── standing/
│   │   ├── front.png
│   │   ├── right.png
│   │   ├── left.png
│   │   ├── top.png
│   │   └── bottom.png
│   ├── playful-ball-action/
│   │   └── low-front-action.png
│   └── balancing-hindlegs/
│       └── top.png
├── expressions/
│   └── head/
│       ├── emotion-sheet.png
│       ├── happy.png
│       ├── sad.png
│       ├── angry.png
│       ├── surprised.png
│       ├── scared.png
│       ├── determined.png
│       ├── curious.png
│       └── playful.png
└── sprites/
```

De exacte extensie mag het originele goedgekeurde formaat volgen. Niet onnodig converteren als dat de bronbytes verandert.

Voor Adult Yupi dezelfde logica onder `assets/yupi/adult/`.

## 6. Belangrijk: JSON is index, niet asset

De huidige verspreide `approved-source.json`-bestanden zijn nuttig voor herstel omdat ze provenance bevatten.

Tijdens de herstelronde:

- **niet verwijderen**;
- eerst alle originele binaries terughalen;
- hashes controleren;
- repo-paden vastleggen.

Daarna kan worden besloten of de metadata wordt geconsolideerd in één `asset-manifest.json` per levensfase.

Het manifest is de index.  
Het beeldbestand is de visuele bron.

## 7. Visuele consistentie: werkelijk beeld gebruiken

Een bestandsnaam, JSON-beschrijving, hash of herinnering aan een eerder beeld laat een image model **niet zien hoe Yupi er exact uitziet**.

Voor iedere nieuwe Yupi-generatie moet daarom vóór generatie het **werkelijke goedgekeurde beeldmateriaal zichtbaar/toegankelijk zijn als visuele referentie**.

Voorkeursvolgorde:

1. exacte canonieke repo-afbeelding;
2. dezelfde exacte approved binary uit ChatGPT Library;
3. expliciet door Johan/Michel opnieuw aangeleverde approved bron.

Alleen tekstuele metadata gebruiken is onvoldoende voor character consistency.

### Als de generatietool de referentie niet werkelijk als beeld kan gebruiken

Dan mag die sessie geen nieuwe canonieke Yupi-asset genereren.

Eerst de approved afbeelding zo beschikbaar maken dat deze daadwerkelijk visueel kan worden gelezen/gebruikt, of de gebruiker vragen de exacte referentie opnieuw in de actieve chat te plaatsen.

**Niet genereren vanuit geheugen.**

## 8. Referentiehiërarchie per levensfase

Pup, Teen en Adult zijn afzonderlijke visuele vormen.

Voor elke vorm hoort minimaal één canonieke basisreferentie beschikbaar te zijn, aangevuld met goedgekeurde views/poses.

Een nieuwe Teen-pose wordt dus gebaseerd op **Teen Yupi**, niet op Pup of Adult.

Een nieuwe Adult-pose wordt gebaseerd op **Adult Yupi**, niet op een tekstuele beschrijving van Teen plus "maak hem ouder".

Bij meerdere relevante approved beelden moeten de meest directe referenties worden gebruikt:

- character identity/base;
- juiste levensfase;
- dichtstbijzijnde goedgekeurde camerahoek;
- eventueel reeds goedgekeurde pose/expression.

## 9. Voorkeur voor image-to-image / edit boven vrije regeneratie

Wanneer een bestaand approved Yupi-beeld geschikt is als basis:

- gebruik dat beeld als bron/reference;
- verander alleen wat voor de nieuwe pose/view/expression nodig is;
- behoud character identity, kleur, vacht, lichaamsbouw, kopvorm en asymmetrie.

Een volledig vrije text-to-image generatie is alleen geschikt voor experimenten of wanneer expliciet een nieuw ontwerp wordt gezocht.

Voor canonieke voortbouwende assets is maximale continuïteit belangrijker dan creatieve variatie.

## 10. Harde visuele validatie na generatie

Voor iedere nieuwe kandidaat altijd vergelijken met de relevante approved bronbeelden.

Minimaal controleren:

### Anatomie
- exact 3 poten;
- rechter voorpoot aanwezig;
- linker voorpoot volledig afwezig tot de schouder;
- geen stomp/nub;
- beide achterpoten aanwezig;
- rechter oor rechtop;
- linker oor hangend;
- geen automatische spiegeling.

### Character identity
- dezelfde kopvorm;
- dezelfde snuit/neus;
- dezelfde ogen en onderlinge plaatsing;
- dezelfde vachtkleur/markeringen;
- dezelfde staartvorm;
- dezelfde lichaamsverhoudingen voor die levensfase;
- dezelfde algemene 3D-/renderstijl.

### Leeftijdsvorm
- Pup blijft Pup;
- Teen blijft Teen;
- Adult blijft Adult;
- leeftijd mag niet per pose onbedoeld verspringen.

Bij duidelijke afwijking:

**niet opslaan als approved, niet "ongeveer goed" verklaren, maar afkeuren en opnieuw vanuit de echte visuele referentie werken.**

## 11. Turnarounds en sheets

Wanneer meerdere aanzichten afzonderlijk approved zijn:

- deze exacte bestanden gebruiken;
- samenstellen/compositen;
- niet opnieuw genereren om er een sheet van te maken;
- niet automatisch spiegelen.

Een samengestelde sheet mag nooit de losse approved bronnen vervangen.

## 12. Geautomatiseerde repo-validatie

Voeg na de herstelronde een controle toe die CI/lokaal kan draaien.

Minimaal per manifest-entry met `status: approved`:

1. `path` bestaat;
2. path wijst naar een imagebestand waar dat type dat vereist;
3. bestand is niet leeg;
4. SHA-256 komt overeen met manifest;
5. geen approved asset verwijst uitsluitend naar Library zonder repo-binary.

Een fout moet de asset-validatie laten falen.

Zo kan toekomstige AI-output niet opnieuw een "approved" manifest maken zonder daadwerkelijke bestanden.

## 13. Pup als voorbeeld

De Pup-structuur bevat al echte goedgekeurde binaries, bijvoorbeeld:

- `assets/yupi/pup/design/approved/base-reference.jpg`
- `assets/yupi/pup/poses/sitting/front.webp`
- `assets/yupi/pup/poses/standing-bark/front.webp`

Dit is het gewenste principe: metadata **én** het echte visuele bestand samen in de repository.

## 14. Definition of Done voor deze herstelactie

De herstelactie is pas klaar wanneer:

- alle recoverable Teen approved assets als echte binaries in GitHub staan;
- alle recoverable Adult approved assets als echte binaries in GitHub staan;
- hashes zijn gecontroleerd;
- manifests naar de repo-binaries wijzen;
- tijdelijk foutieve `approved` statussen zijn gecorrigeerd;
- visuele basereferenties voor Pup/Teen/Adult duidelijk zijn aangewezen;
- automatische asset-validatie is toegevoegd;
- `docs/YUPI_ASSET_PIPELINE.md` is uitgebreid van alleen Pup naar alle Yupi-levensfasen;
- een korte handoff in `AI_JOHAN.md` het herstel bevestigt.

## 15. Belangrijkste regel

> **Een AI mag pas op een bestaand Yupi-ontwerp voortbouwen als hij de echte goedgekeurde visuele bron kan zien/gebruiken.**
>
> **Geen echte bron zichtbaar = geen canonieke generatie.**
>
> **Approved = expliciete goedkeuring + echte repo-binary + correcte hash + geslaagde validatie.**
