# Yupi's Game — Game Bible

> **Status:** officiële werkcanon voor verdere ontwikkeling  
> **Repository:** `johan1981/yupi-game`  
> **Doel:** alle gemaakte afspraken over verhaal, personages, stijl, gameplay en technische richting op één plek bewaren.

---

# 1. Projectoverzicht

## Hoofdreeks

De gamewereld bestaat uit twee grote delen:

1. **Yupi — deel 1**
   - oorsprongsverhaal van Yupi
   - begint wanneer Yupi nog een pup is
   - introduceert de futuristische wereld, het ongeluk en de eerste mysteries

2. **Yupi: Nexus Breuk**
   - vervolg
   - multiversumverhaal
   - meerdere versies van Yupi bestaan
   - niet elke versie van Yupi is goedhartig
   - de Nexus, tijdlijnen en alternatieve werelden worden centrale onderdelen

De huidige browsergame begint met deel 1.

---

# 2. Genre en gameplayrichting

De game wordt ontwikkeld als een:

**cinematische 2.5D side-scrolling adventure**

De speler beweegt hoofdzakelijk links en rechts, maar de wereld moet veel dieper aanvoelen door:

- parallax-achtergronden
- bewegende voorgrondlagen
- licht, mist en deeltjes
- cinematische camerabewegingen
- cutscenes
- verticale momenten
- tunnels, doorgangen en instortingen
- korte scènes waarin de wereld visueel om Yupi heen verandert

De game moet geen simpele Mario-achtige platformer worden.

## Kernmechanieken

- lopen
- rennen
- springen
- snuffelen
- blaffen
- ontdekken
- lichte puzzels
- stealth
- omgevingsinteractie
- cinematische actie
- emotionele verhaalmomenten

De besturing moet geschikt blijven voor **iPhone in landscape-modus**.

---

# 3. Visuele richting

## Algemene stijl

De game gebruikt een warme, filmische, hoogwaardige game/animatiestijl.

Belangrijk:

- personages zijn altijd duidelijk leesbaar
- hoofdpersonages blijven scherp
- achtergronden mogen zachter of iets vervaagd zijn
- diepte ontstaat met meerdere lagen
- expressieve ogen en duidelijke silhouetten
- omgevingen mogen groot en spectaculair zijn zonder de personages te overschaduwen

## Vaste asset-aanpak

Voor elk belangrijk personage maken we:

- character sheet
- idle pose / idle animatie
- lopen
- rennen
- springen
- speciale actie
- schrik/pijnreactie
- emotionele poses
- portrait / cutscene artwork indien nodig

De goedgekeurde **Pup Yupi**-assets vormen de kwaliteits- en stijlbasis voor de overige gamepersonages.

Bestaande locatie:

`assets/yupi/pup/`

---

# 4. Yupi — vaste canon

Yupi is het centrale personage van de reeks.

## Onveranderlijke kenmerken

Deze regels gelden voor Yupi en moeten in alle relevante versies bewust worden bewaakt:

> **Verplichte visuele/anatomische detailbron:** `docs/characters/YUPI_SPEC.md`  
> Machineleesbare equivalent: `docs/characters/YUPI_SPEC.json`  
> Bij ieder nieuw Yupi-beeld, sprite, animatie, model-sheet of pose moeten deze specificaties vóór én na generatie worden gecontroleerd.

- Yupi is een reu
- Yupi is bruin in zijn hoofdvorm
- Yupi heeft **exact drie poten**: twee achterpoten en één rechter voorpoot
- Yupi mist zijn **linker voorpoot volledig tot aan de schouder**
- er is **geen stompje, gedeeltelijke poot of extra uitsteeksel** aan de linker voorzijde
- zijn beperking wordt niet als zielig of als hoofdidentiteit behandeld
- Yupi is nieuwsgierig, eigenwijs, warm en moedig
- Yupi moet een herkenbaar silhouet hebben
- het **rechter oor staat rechtop**
- het **linker oor hangt**
- zijn gezicht is expressief en goed leesbaar tijdens gameplay

De driepotige beweging moet natuurlijk aanvoelen.

Hij beweegt niet alsof hij "kapot" is. Zijn manier van lopen is gewoon zijn normale manier van bewegen.

## Bewegingsreferentie — echte Yupi-video's

De aangeleverde video's van Yupi zijn de vaste referentie voor zijn gamebeweging.

- De enige rechter voorpoot draagt het voorlichaam centraal.
- Bij de opvang zakt de schouder/voorhand zichtbaar en veert daarna weer omhoog.
- De achterpoten leveren relatief veel afzet en voortstuwing.
- Hoofd en nek bewegen mee met het pasritme.
- De staart ondersteunt balans bij draaien en snelle richtingswisselingen.
- Versnellen, stoppen en omkeren hebben een korte gewichtsverplaatsing; Yupi mag niet als een stijve sprite schuiven.
- De animatieset omvat minimaal idle, snuffelen, wandelen, draven, sprinten, stoppen, draaien, speels bewegen, Nexus-puls, geraakt en herstellen.
- Een standaard vierpotige hondenloop met alleen één poot weggehaald geldt niet als correcte Yupi-beweging.

De huidige videoreferentie-walktest staat als technisch prototype onder `assets/yupi/pup/sprites/_prototype/walk-right/`. Deze sequence is een bewegingsproef en geldt niet automatisch als definitieve canonieke sprite.

---

# 5. Het Yupi-DNA en de varianten

Omdat er meerdere vormen van Yupi bestaan, ontwerpen we niet telkens een willekeurig nieuw karakter.

Alle Yupi-varianten delen een herkenbaar **Yupi-DNA**.

## Vaste herkenningspunten

- verwante kopvorm
- herkenbare oorvorm
- verwant silhouet
- emotionele leesbaarheid
- duidelijk visueel verband met Yupi Prime

De speler moet direct kunnen denken:

> "Dat is Yupi... maar niet dezelfde Yupi."

De varianten mogen verschillen in:

- vachtkleur
- energie
- proporties
- houding
- effecten
- gedrag
- krachten
- animatiestijl

---

# 6. Pup Yupi

## Rol

Pup Yupi is de speelbare Yupi aan het begin van de game.

Hij is het hoofdpersonage van:

**Level 1 — De Laatste Rit**

## Ontwerp

- kleine bruine pup
- compact lichaam
- grote expressieve ogen
- warme lichte accenten rond snuit en borst
- **rechter oor staat rechtop**
- **linker oor hangt**
- exact drie poten: twee achterpoten en één rechter voorpoot
- linker voorpoot ontbreekt volledig tot de schouder
- geen stompje of gedeeltelijke linker voorpoot
- vriendelijk en nieuwsgierig uiterlijk

## Karakter

- nieuwsgierig
- speels
- gevoelig
- moedig
- onschuldig
- trouw
- intuïtief

## Gameplay

Pup Yupi leert de speler:

- lopen
- springen
- snuffelen
- blaffen
- reageren op de omgeving

Hij is in deze fase nog geen geavanceerde vechter en beschikt nog niet over alle latere Nexus-vaardigheden.

## Bestaande assets

De canonieke Pup Yupi-assetroot is:

`assets/yupi/pup/`

De verplichte assetworkflow staat in:

`docs/YUPI_ASSET_PIPELINE.md`

De actuele goedgekeurde visuele basis staat in:

`assets/yupi/pup/design/approved/base-sheet.png`

Goedgekeurde poses, expressies en sprites worden gestructureerd opgeslagen en geregistreerd in:

`assets/yupi/pup/asset-manifest.json`

Oude losse sprites en eerdere walk-experimenten staan onder `assets/yupi/pup/archive/` en gelden niet automatisch als actuele canon. Technische tests die nog door de browserdemo worden gebruikt staan onder `assets/yupi/pup/sprites/_prototype/`.

---

# 7. Yupi Prime

Yupi Prime is de centrale volwassen/latere hoofdversie van Yupi.

## Karakter

- moedig
- zorgzaam
- koppig
- nieuwsgierig
- sterk moreel hart
- beschermend tegenover vrienden

## Visuele richting

- bruine basis
- herkenbaar als de oudere versie van Pup Yupi
- krachtigere houding
- subtiel heldhaftiger silhouet
- linker voorpoot blijft volledig ontbreken
- eventuele Nexus-details moeten aanvullend zijn en Yupi niet veranderen in een generieke sci-fi held

Yupi Prime is de belangrijkste visuele referentie voor andere varianten.

---

# 8. Echo Yupi

Echo Yupi is een alternatieve multiversumversie.

## Visuele identiteit

- koelere uitstraling
- holografische of lichtachtige fragmenten
- energie kan van het lichaam loskomen
- herkenbare Yupi-basis blijft aanwezig

## Mogelijke gameplay-identiteit

- kort fragmenteren
- tijdelijke echo's creëren
- zeer korte verplaatsingen / teleportachtige beweging
- puzzels gebaseerd op meerdere posities of reflecties

Echo moet mysterieus voelen, niet simpelweg "blauwe Yupi".

---

# 9. Schaduw-Yupi

Schaduw-Yupi is een donkere, krachtige Yupi-variant.

## Visuele identiteit

- donkere vacht / schaduwvorm
- rode of donkere Nexus-energie
- hoekiger en agressiever silhouet
- herkenbare Yupi-kop en houding blijven zichtbaar

## Karakterrichting

Schaduw-Yupi moet niet als simpele "evil Yupi" worden behandeld.

Hij mag:

- dreigend
- intens
- bitter
- agressief
- tragisch

zijn.

## Gameplay

Schaduw-Yupi kan:

- zeer snel zijn
- Yupi's bewegingen spiegelen
- dash-aanvallen gebruiken
- als spiegelboss functioneren

Een belangrijke verhaallijn is dat de confrontatie niet uitsluitend door geweld hoeft te worden opgelost.

---

# 10. Y-00 en Y.V.

Y-00 behoort tot de oorsprong van het grotere Nexus-mysterie.

In bestaand conceptmateriaal wordt Y-00 verbonden met de eerste / oorspronkelijke Yupi-versie.

Y.V. is verbonden met deze oorsprong en verschijnt later als een grotere, instabielere en dreigendere vorm.

## Richting

Y-00 / Y.V. moeten:

- herkenbaar verband houden met Yupi
- meer vervreemdend zijn dan Echo of Schaduw
- de oorsprong en manipulatie van de Nexus symboliseren
- emotionele en verhalende betekenis hebben, niet alleen boss-design zijn

De exacte onthulling en chronologie kan tijdens verdere uitwerking worden aangescherpt, maar mag niet willekeurig worden herschreven zonder de game-bible bij te werken.

---

# 11. Nox

Nox is een **robothond**.

Dit is belangrijk: Nox is geen robotmens, drone of zwevend apparaat.

## Rol

- bondgenoot van Yupi
- technologische ondersteuning
- vaste vriend in latere delen van het avontuur

## Ontwerp

- mechanische hond
- compact en herkenbaar hondensilhouet
- futuristische metalen panelen
- heldere lichtaccenten / ogen
- vriendelijk genoeg om als bondgenoot te lezen
- duidelijk anders dan Yupi

## Gameplay

Nox kan onder andere:

- systemen activeren
- deuren openen
- technologie analyseren
- puzzels ondersteunen
- Yupi volgen
- in bepaalde situaties zelfstandig reageren

Nox verschijnt **niet als vaste partner in Level 1**.

De ontmoeting met Nox komt later.

---

# 12. Yuno

Yuno is een belangrijke bondgenoot in **Yupi: Nexus Breuk**.

## Kenmerken

- lichte vacht
- futuristische / multiversum uitstraling
- beschadigde of gebroken tijdsband aan de voorpoot

De tijdsband is een belangrijk visueel en verhalend element.

## Karakter

- bedachtzaam
- in eerste instantie gereserveerd
- kennis van tijd / realiteiten
- ontwikkelt een hechte band met Yupi

## Gameplay

Yuno kan bijdragen aan:

- tijdmechanieken
- tijdelijke bruggen
- gestabiliseerde portals
- gebeurtenissen terugzien
- omgevingen tijdelijk herstellen

---

# 13. Deel 1 — begin van het verhaal

Yupi's avontuur begint wanneer hij nog een pup is.

Hij is samen met:

- zijn ouders
- zijn broertje

onderweg in een futuristisch voertuig tijdens een verhuizing.

De wereld lijkt aanvankelijk veilig.

Yupi is speels en nieuwsgierig.

Dan merkt hij iets vreemds.

Een onbekende energie begint zich te manifesteren.

Daarmee begint het mysterie dat uiteindelijk leidt naar de Nexus.

---

# 14. Level 1 — De Laatste Rit

**Officiële titel:**

# DE LAATSTE RIT

Dit is de opening van de speelbare game.

## Scène 1 — De verhuiswagen

Yupi bevindt zich met zijn familie in een futuristische verhuiswagen.

De speler leert:

- links/rechts bewegen
- springen
- onderzoeken
- snuffelen
- blaffen

De sfeer is warm en veilig.

Buiten beweegt een futuristische stad voorbij.

De achtergrond werkt met parallax en mag zachter worden weergegeven zodat Yupi centraal blijft.

---

## Scène 2 — Iets klopt niet

Yupi ruikt iets vreemds.

De snuffelmechaniek introduceert een subtiel lichtspoor.

Bij een paneel of ventilatierooster verschijnt voor het eerst een korte:

**paarse gloed**

Het verschijnsel verdwijnt voordat Yupi het kan onderzoeken.

Dit is de eerste echte aanwijzing dat de rit niet normaal is.

---

## Scène 3 — De storing

De buitenwereld wordt donkerder.

Een felle paarse flits verschijnt.

De verhuiswagen begint te schudden.

- lampen knipperen
- dozen schuiven
- technologie valt uit
- Yupi moet obstakels ontwijken
- hij probeert terug naar zijn familie te komen

Een systeemmelding kan kort verschijnen:

**SIGNAL UNKNOWN**

---

## Scène 4 — De crash

De storing escaleert.

De verhuiswagen raakt onbestuurbaar.

De speler rent terwijl:

- de omgeving harder beweegt
- onderdelen losschieten
- de camera schudt
- paarse energie het beeld vult

Dan volgt de crash.

Belangrijk voor presentatie:

- korte zwarte overgang
- geluid van metaal
- glas
- zware impact
- daarna stilte

---

## Scène 5 — Alleen

Yupi wordt wakker tussen de brokstukken.

De warme sfeer van het begin is verdwenen.

Hij zoekt:

- zijn ouders
- zijn broertje

De speler onderzoekt de omgeving.

Er is weinig of geen muziek.

Geluid bestaat vooral uit:

- wind
- krakend metaal
- verre omgevingsgeluiden

Blaffen levert geen antwoord op.

Dit moet één van de emotionele momenten van Level 1 zijn.

---

## Scène 6 — Het spoor

Yupi verlaat het wrak.

Hier ziet de speler voor het eerst de grotere wereld na de crash:

- kapotte infrastructuur
- futuristische ruïnes
- mist
- verre stad
- vreemde energie

Yupi gebruikt zijn neus.

Het paarse spoor verschijnt opnieuw.

De speler volgt het via een eerste echte platformsectie richting een donkere tunnel.

---

# 15. Einde van Level 1

Yupi bereikt de tunnel.

De paarse energie beweegt naar binnen.

Vanuit het donker klinkt een vervormde stem:

> "...Yupi..."

Een vreemd symbool verschijnt.

Daarna:

**LEVEL COMPLETE**

**DE LAATSTE RIT**

Volgend level:

**HET SPOOR**

Dit eindpunt is bedoeld als cliffhanger.

---

# 16. Verhaallijn na Level 1

Na De Laatste Rit wordt langzaam duidelijk dat het ongeluk geen gewone crash was.

Yupi ontdekt:

- vreemde technologie
- verlaten faciliteiten
- onbekende signalen
- Nexus-sporen

Later ontmoet hij Nox.

Vanaf dat moment groeit de game van een persoonlijk mysterie naar een groter sciencefictionavontuur.

---

# 17. Overgang naar Nexus Breuk

In het vervolg wordt duidelijk dat er meerdere werkelijkheden bestaan.

Daar bestaan meerdere Yupi-versies.

Niet iedere realiteit is stabiel.

Niet iedere Yupi heeft hetzelfde pad gevolgd.

Belangrijke thema's:

- identiteit
- vrije wil
- verlies
- vriendschap
- oorsprong
- de vraag wat iemand tot zichzelf maakt
- realiteiten die uit elkaar vallen

---

# 18. Aqua-X

Aqua-X is een bestaande wereld binnen het Nexus Breuk-universum.

## Identiteit

- mysterieuze oceaanwereld
- vergeten technologie
- oude energiebronnen
- onderwater / waterachtige sfeer
- Nexus-geschiedenis ligt er verborgen

Aqua-X mag niet als gewone tropische waterwereld worden ontworpen.

De sfeer moet oud, technologisch en mysterieus zijn.

---

# 19. Arqion

Arqion is een belangrijke wereld / stad in Nexus Breuk.

Bestaande visuele concepten tonen onder andere:

- zwevende architectuur
- drijvende straten
- enorme constructies
- watervallen en water in onmogelijke richtingen
- beelden van verschillende Yupi-varianten
- Nexus-archieven
- de Prime-status
- Variant Hunters
- Nexus-poorten

Arqion heeft een grootse, oude maar futuristische identiteit.

---

# 20. Nexus-poorten en tijdskristallen

In bestaand verhaalconcept worden Nexus-poorten gebruikt om realiteiten te verbinden.

Ook bestaan er tijdskristallen.

De poorten mogen onderdeel zijn van:

- leveldoelen
- puzzels
- verhaalovergangen
- eindsequenties

Een bestaande verhaallijn bevat drie tijdskristallen die uit verschillende realiteiten moeten worden gehaald.

Voorbeelden:

- instortende tijdrealiteit
- spiegelwereld
- realiteit bewaakt door een krachtige Yupi-variant

---

# 21. Variant Hunters

Variant Hunters zijn vijandelijke mechanische wezens die via Nexus-poorten kunnen verschijnen.

## Richting

- technologisch
- dreigend
- gebouwd voor jacht op varianten
- duidelijk ander silhouet dan Nox
- rode / vijandige energieaccenten zijn mogelijk

Ze moeten herkenbaar zijn als een specifieke vijandklasse en niet als generieke robots.

---

# 22. De Tijdboom / oorsprong van de Nexus

Een latere kernlocatie is de oorsprong van de Nexus.

Daar bestaat conceptueel een oorspronkelijke Tijdboom / Nexus-kern waar verschillende Yupi-realiteiten mee verbonden zijn.

Hier kunnen:

- Yupi-varianten zichtbaar zijn
- opgeslagen / slapende versies bestaan
- realiteiten worden gevolgd
- de oorsprong van Y-00 worden onthuld

Dit behoort tot de late verhaalontwikkeling en moet groots en mysterieus blijven.

---

# 23. Bestaande illustraties als canon

Eerdere Yupi-game illustraties worden niet genegeerd.

Ze dienen als:

- character reference
- wereldreference
- art direction
- cutscene inspiratie
- level moodboards
- bron voor bestaande lore

Bestaande ontwerpen van onder andere:

- Yupi Prime
- Echo Yupi
- Schaduw-Yupi
- Nox
- Yuno
- Y-00 / Y.V.
- Arqion
- Nexus-poorten
- tijdskristallen

moeten worden meegenomen wanneer nieuwe assets worden ontworpen.

Nieuwe ontwerpen mogen worden verbeterd voor gameplay, maar mogen niet zonder reden de herkenbaarheid van bestaande ontwerpen verliezen.

---

# 24. Gamepersonages eerst ontwerpen

Voor verdere levelontwikkeling geldt:

**eerst de hoofdpersonages visueel vastzetten, daarna levels definitief uitbouwen.**

Prioriteitsvolgorde:

1. Pup Yupi
2. Yupi Prime
3. Echo Yupi
4. Schaduw-Yupi
5. Nox
6. Yuno
7. Y-00 / Y.V.

Pup Yupi is inmiddels als eerste vastgelegd.

---

# 25. Technische richting

De huidige game is een webgame in:

`index.html`

De repository wordt gepubliceerd via GitHub Pages.

Doelplatform:

- Safari op iPhone
- daarnaast bruikbaar op desktopbrowser

## Besturing mobiel

- links
- rechts
- springen
- snuffelen
- blaffen
- later aanvullende actieknoppen indien noodzakelijk

De interface moet op landscape-schermen goed zichtbaar blijven.

---

# 26. Belangrijke technische les uit de prototypefase

De eerste prototypes gebruikten eenvoudige canvasvormen en een geïmproviseerde Yupi.

Dat is niet langer de gewenste richting.

Vanaf nu:

- gebruiken we echte character-assets
- worden personages geladen als afbeeldingen / sprites
- blijven placeholders uitsluitend tijdelijk
- moet game-schaal correct reageren op iPhone-schermhoogte
- worden visuele assets opgeslagen in de repository

---

# 27. Assetstructuur

Voorgestelde structuur:

```
assets/
  yupi/
    pup/
    prime/
    echo/
    shadow/
    y00/
  nox/
  yuno/
  enemies/
  worlds/
    level-01/
    aqua-x/
    arqion/
  ui/
```

Elke hoofdmap mag een eigen README krijgen met vaste karakter- of wereldregels.

---

# 28. Bron van waarheid

Dit document is vanaf nu de centrale werkcanon voor de game.

Als we samen een belangrijke wijziging afspreken, moet dit document worden aangepast.

Voorbeelden:

- naam van een level verandert
- nieuwe Yupi-variant
- karakterontwerp wordt definitief
- verhaalonthulling verandert
- gameplaymechaniek wordt toegevoegd
- wereldregels veranderen

Dat voorkomt dat verhaal, GitHub-code en illustraties uiteen gaan lopen.

---

# 29. Huidige ontwikkelstatus

## Vastgelegd

- side-scroller / 2.5D richting
- iPhone als belangrijk doelplatform
- Level 1 heet **De Laatste Rit**
- Pup Yupi character design v2 (`assets/yupi/pup/design/approved/base-sheet.png`)
- harde anatomische regel: exact 3 poten — 2 achter, 1 rechter voor, links voor volledig afwezig tot aan de schouder
- Pup Yupi sprite-assets
- meerdere Yupi-vormen maken deel uit van het grotere verhaal
- Nox is een robothond
- Nox verschijnt niet als vaste partner in Level 1
- Yuno en zijn tijdsband behoren tot Nexus Breuk
- bestaande illustraties worden als visuele canon gebruikt

## Nog uit te werken

- definitieve Yupi Prime game-assets
- Echo Yupi game-assets
- Schaduw-Yupi game-assets
- Nox character sheet + sprites
- Yuno character sheet + sprites
- Y-00 / Y.V. definitieve designs
- familie van Pup Yupi
- definitieve achtergronden van Level 1
- cutscene artwork van De Laatste Rit
- Level 2 — Het Spoor
- exacte overgang tussen deel 1 en Nexus Breuk
- volledige levelvolgorde van de uiteindelijke game

---

# 30. Ontwikkelprincipe

Bij iedere volgende toevoeging geldt:

**verhaal → character/world design → game-asset → implementatie**

Niet andersom.

Zo blijft Yupi's game één samenhangend spel in plaats van een verzameling losse prototypes.

---

*Laatste grote canon-update: september 2026.*
