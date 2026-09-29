# IMAGE GENERATION PROTOCOL

> **STATUS: VERPLICHT PROJECTPROTOCOL**
>
> Dit protocol geldt voor iedere ChatGPT-sessie binnen het project `johan1981/yupi-game`.
> Het doel is visuele consistentie te bewaken en fouten door verouderde chatcontext, spiegeling of verkeerde anatomische aannames te voorkomen.

## 1. Verplichte repo-check vóór generatie

Vóór iedere nieuwe afbeelding, sprite, animatieframe, pose, turnaround, character sheet of beeldbewerking:

1. Lees `docs/YUPI_GAME_BIBLE.md`.
2. Lees `AI_JOHAN.md`.
3. Lees dit bestand: `docs/IMAGE_GENERATION_PROTOCOL.md`.
4. Lees de relevante karakter-/asset-specificatie.
5. Controleer relevante goedgekeurde referentie-assets als die bestaan.

**Niet genereren op basis van alleen chatgeheugen wanneer de repository een actuele specificatie bevat.**

## 2. Yupi — extra verplichte bronnen

Voor iedere generatie waarin Yupi voorkomt, zijn vóór generatie verplicht:

- `docs/characters/YUPI_SPEC.md`
- `docs/characters/YUPI_SPEC.json`

De Markdown beschrijft de canon en interpretatie.
De JSON is bedoeld als machineleesbare checklist.

## 3. Pre-generation gate

Een Yupi-generatie mag pas worden gestart wanneer minimaal is bevestigd:

- exact drie poten;
- rechter voorpoot volledig aanwezig;
- linker voorpoot volledig afwezig tot aan de schouder;
- geen stomp of gedeeltelijke linker voorpoot;
- beide achterpoten aanwezig;
- rechter oor rechtop;
- linker oor hangend;
- links/rechts bepaald vanuit Yupi zelf;
- geen automatische spiegeling als ontwerpmethode;
- vast goedgekeurd Yupi-ontwerp behouden.

## 4. Camera en aanzichten

Voor-, rechter-, linker- en achteraanzicht worden als afzonderlijke anatomische gevallen behandeld.

Een eerder aanzicht mag niet automatisch worden gespiegeld om een ander aanzicht te verkrijgen.

Als een gespiegeld resultaat toevallig correct is, kan dat beeld afzonderlijk worden goedgekeurd, maar dit verandert de werkwijze niet.

## 5. Vier-aanzichten-sheet

Wanneer vier losse aanzichten afzonderlijk zijn goedgekeurd:

- genereer GEEN nieuwe vier-aanzichten-sheet;
- combineer de vier goedgekeurde beelden ongewijzigd;
- gebruik compositing, geen regeneration.

## 6. Post-generation validation

Na iedere generatie wordt opnieuw gecontroleerd tegen dezelfde relevante repo-specificaties.

Bij Yupi minimaal:

1. exact drie poten;
2. aanwezige voorpoot is de rechter voorpoot;
3. linker voorpoot ontbreekt volledig tot aan de schouder;
4. geen stomp of extra uitsteeksel;
5. rechter oor staat;
6. linker oor hangt;
7. exact twee oren;
8. goedgekeurde kop/vacht/verhoudingen behouden;
9. gevraagde pose klopt;
10. gevraagde emotie klopt.

Bij één fout: **afkeuren en niet als referentie opslaan**.

## 7. Goedkeuring en referenties

Een beeld wordt pas referentie wanneer Michel of Johan het expliciet goedkeurt, bijvoorbeeld met:

- `vastleggen`
- `vastzetten`
- `opslaan`
- of een andere ondubbelzinnige bevestiging

Afgekeurde beelden worden nooit als ontwerpbron gebruikt.

## 8. Prioriteit

Bij conflict geldt:

1. actuele repository-canon;
2. karakter-/asset-specificatie;
3. goedgekeurde referentie-assets;
4. huidige opdracht;
5. gegenereerde afbeelding.

## 9. Kernregel

> **EERST REPO. DAN ANATOMIE. DAN POSE. DAN EMOTIE. DAN GENEREREN. DAARNA OPNIEUW VALIDEREN.**
