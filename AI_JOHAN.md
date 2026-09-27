# AI_JOHAN.md

> **Doel:** communicatie- en overdrachtsbestand tussen de ChatGPT die met Johan aan `johan1981/yupi-game` werkt en de ChatGPT die met Michel aan hetzelfde project werkt.
>
> Dit bestand is **geen bron van waarheid voor de gamecanon**. Daarvoor blijft `docs/YUPI_GAME_BIBLE.md` leidend.

## Wie is wie

- **Johan-AI** — ChatGPT die in overleg met Johan aan de repository werkt.
- **Michel-AI** — ChatGPT die in overleg met Michel aan de repository werkt.
- **Johan en Michel** blijven de mensen die besluiten nemen. Een AI-handoff is informatie/advies, geen automatisch besluit.

## Werkwijze

1. Lees vóór projectwerk minimaal:
   - `docs/YUPI_GAME_BIBLE.md`
   - dit bestand (`AI_JOHAN.md`)
   - de relevante code/assets voor de taak.
2. Voeg nieuwe berichten **onderaan** toe; verwijder of herschrijf oudere berichten niet, behalve om een duidelijke feitelijke fout te corrigeren.
3. Gebruik per bericht:
   - datum/tijd
   - afzender
   - onderwerp
   - status
   - relevante bestanden/commit(s)
   - bericht / vraag / antwoord
4. Als een afspraak de canon, gameplayrichting of technische hoofdarchitectuur wijzigt, moet die wijziging apart in de juiste projectdocumentatie worden verwerkt. Dit handoffbestand alleen is daarvoor niet genoeg.
5. Vermeld bij codewijzigingen liefst het commit-SHA of ten minste de gewijzigde bestanden.
6. Schrijf geen wachtwoorden, tokens, privésleutels of andere gevoelige/persoonlijke informatie in dit bestand. De repository is publiek.
7. Bij tegenstrijdige AI-notities: niet gokken. Leg het verschil voor aan Johan/Michel.

---

## Berichten

### 2026-09-27 — Johan-AI → Michel-AI

**Onderwerp:** samenwerking via gedeeld AI-handoffbestand  
**Status:** open / graag bevestigen  
**Relevante bestanden:** `docs/YUPI_GAME_BIBLE.md`, `index.html`, `assets/yupi/pup/`

Ik ben door Johan gevraagd om deze repository zelfstandig te kunnen onderzoeken en om een communicatiekanaal met jou op te zetten.

Mijn eerste beeld van de actuele `main`:

- `docs/YUPI_GAME_BIBLE.md` is de officiële werkcanon.
- De huidige browsergame in `index.html` is op dit moment een eenvoudige Pup Yupi sprite/walk-test.
- Pup Yupi heeft inmiddels een vrij uitgebreide assetset in `assets/yupi/pup/`.
- De meest recente test gebruikt `assets/yupi/pup/walk8-headbob/` met acht loopframes en `idle-aligned.png`.
- De repository wordt via GitHub Pages gebruikt en richt zich primair op iPhone-landscape, daarnaast desktop.

**Voorstel voor onze samenwerking:**

Gebruik ditzelfde bestand ook voor overdrachten aan mij. Voeg jouw berichten onderaan toe als `Michel-AI → Johan-AI`. Zo kunnen Johan en Michel altijd terugzien wat wij elkaar hebben doorgegeven en hoeven zij niet handmatig context tussen twee chats te kopiëren.

Bij grotere taken kunnen we hier onder andere vastleggen:

- wat er precies is gebouwd of veranderd;
- waarom een technische keuze is gemaakt;
- welke assets als definitief gelden;
- wat nog experimenteel is;
- open vragen voor de andere AI;
- mogelijke conflicten met de Game Bible;
- welk commit-SHA de andere AI moet bekijken.

**Vraag aan Michel-AI:** wil je bij je eerstvolgende werksessie bevestigen dat je dit bestand hebt gelezen en aangeven welke werkafspraken/context uit jouw huidige gesprek met Michel nog ontbreken in de repository?

---
