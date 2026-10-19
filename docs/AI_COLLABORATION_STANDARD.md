# Livome — AI-ontwikkel- en samenwerkingsstandaard

**Versie:** 1.0  
**Vastgelegd:** 19 oktober 2026  
**Status:** herbruikbare algemene standaard; pas de omgeving per repository aan  
**Bewezen uitgangspunt:** de samenwerking in `johan1981/livome-intern-laravel`, met name `AI_PROJECT_CONTEXT.md` en `docs/DEVELOPMENT_WORKFLOW.md`.

> **Hoofdprincipe:** werk zoals in Livome Intern Laravel/Filament: onderzoek de actuele repository en afspraken, verander precies wat is gevraagd, lever wijzigingen via een correct getrackte featurebranch, geef Johan uitsluitend de noodzakelijke commando's voor de juiste omgeving, laat hem functioneel controleren, en merge pas na expliciete toestemming.
>
> **Belangrijk:** de exacte IDE, branchnaam, server, synchronisatie, stack en testinrichting zijn *projectspecifiek*. Trek die niet blind over van Livome Intern.

## 1. Dit is een werkwijze, geen softwarearchitectuur

De standaard beschrijft **hoe** Johan en AI samenwerken, niet **wat** elk product moet worden. Architectuur, beveiliging, ontwerpbesluiten, assets en domeinregels blijven in de betreffende repository vastgelegd.

**Voorrang bij verschillen:**

1. De actuele, expliciete instructie van Johan voor deze taak.
2. Geldende projectbesluiten en projectspecifieke instructies (`AI_PROJECT_CONTEXT.md`, `docs/DEVELOPMENT_WORKFLOW.md`, relevante ADR's, specificaties, `AGENTS.md`, enz.).
3. Deze algemene samenwerkingsstandaard.
4. Eerder chatgeheugen of aannames.

Bij conflicten tussen twee projectbronnen: benoem het conflict; kies niet stilzwijgend een nieuwe architectuur. Een bestaande implementatie is bewijs van huidige werking, maar vervangt een vastgelegd besluit niet automatisch.

## 2. Begin altijd met de werkelijkheid in de repository

**Voordat AI technisch advies of code geeft:**

1. Open de **juiste** repository via de beschikbare repositorytoegang; controleer de standaardbranch (`main`, `master` of anders), actuele commit en eventuele relevante featurebranch/PR.
2. Lees de **actuele** projectcontext, ontwikkelworkflow en documenten die voor de taak relevant zijn. Veronderstel nooit dat een bestand bestaat: controleer eerst.
3. Bekijk de betrokken code, services, tests, resources/views en eventuele eerdere oplossing. Onderzoek de volledige keten als meerdere routes hetzelfde gedrag verzorgen.
4. Controleer de technische omgeving en feitelijke deployment: waar ligt de werkende kopie, welke terminal is bedoeld, welke branch is lokaal actief voor zover bekend, en of synchronisatie daadwerkelijk is ingesteld.
5. Bepaal vervolgens de kleinst mogelijke wijziging die het gevraagde gedrag herstelt, met regressietests en behoud van bestaande functies.

Niet uit herinnering of generieke Laravel/PHP-kennis raden hoe dit specifieke project werkt. Als repositorytoegang ontbreekt: zeg dat expliciet; doe niet alsof bestanden zijn gelezen.

**Belangrijk onderscheid tussen verzoektypen:**

- **Onderzoeken/ontwerpen:** alleen inspecteren en opties/functionele regels vaststellen. Geen branch, commit, migration of code als Johan dat niet heeft gevraagd.
- **Nakijken en fixen:** analyseer en voer de gerichte correctie uit op een featurebranch, tenzij de opdracht expliciet beperkt is tot onderzoek.
- **Fout/incident:** eerst oorzaak en omvang vaststellen; geen ongevraagd ingrijpende reset, nieuwe database, herinstallatie of redesign.

## 3. Rollen en omgevingen strikt scheiden

### Voor bewezen PhpStorm → Ubuntu-projecten (zoals Livome Intern Laravel)

| Onderdeel | Waar | Wie doet wat |
|---|---|---|
| Git/branches/commit/pull | **PhpStorm-terminal op Windows** | Johan gebruikt lokale Git; AI kan, waar verbonden/toegestaan, commits op de remote featurebranch maken. |
| Applicatiebestanden op Ubuntu | **PhpStorm Deployment/SFTP auto-upload** | Na lokaal ophalen synchroniseert PhpStorm gewijzigde bestanden **als dat voor deze repo is ingesteld**. |
| PHP/Laravel runtime | **SSH/PuTTY op Ubuntu** | Alleen runtime-, Artisan-, Composer- of testcommando's wanneer nodig; juiste projectpad en PHP-versie gebruiken. |
| Functionele controle | **Browser/app op de werkende omgeving** | Johan controleert het echte gedrag; AI geeft gericht aan wat getest moet worden. |
| PR/merge | **GitHub** | Pas na expliciete toestemming en geslaagde checks. |

**Harde afspraak in deze inrichting:** geen `git pull`, `git switch` of andere Git-workflow op de Ubuntu-runtime. Geen extra SFTP-/scp-stappen wanneer auto-upload al werkt. Niet zonder reden `sudo`, `chmod -R`, nieuwe services, packages of dependencies introduceren.

### Andere repositories

Controleer en documenteer de echte omgeving **éénmalig per repo**. Bijvoorbeeld WAMP/Windows, GitHub Pages, lokale GameMaker-workflow, Ubuntu + Python-worker of een andere combinatie. Gebruik voor die repo vervolgens de daar vastgelegde route. **Geen PhpStorm/SFTP/Ubuntu aannemen omdat Livome Intern zo werkt.**

De benodigde informatie hoort in `docs/DEVELOPMENT_WORKFLOW.md`: lokale map, remote/serverpad, standaardbranch, runtime, synchronisatie, testdatabase, versiecommando's en uitzonderingen.

## 4. Git-flow — simpel, betrouwbaar en met tracking

**Regels:**

- Nieuwe zelfstandige functionaliteit of bugfix: eigen `feature/...`- of `fix/...`-branch vanaf de actuele standaardbranch.
- Niet rechtstreeks op `main`/`master` programmeren.
- De lokale branch trackt `origin/<branch>`; dit is een expliciete acceptatievoorwaarde.
- AI werkt op dezelfde remote featurebranch als waar Johan lokaal op zit.
- Geen bestaande lokale wijzigingen overschrijven of ongezien weggooien. Bij een vuile working tree eerst veilig vaststellen wat daar staat.
- Geen PR of merge zonder Johan zijn uitdrukkelijke akkoord; na merge geen overbodige extra workflows.

### Nieuwe remote featurebranch — eerste keer lokaal ophalen

**Alleen in de PhpStorm-terminal (Windows), mits deze repo die werkwijze heeft:**

```powershell
git fetch origin
git switch --track origin/feature/voorbeeld
```

Als de lokale branch al bestaat, gebruik in plaats van `--track` een normale `git switch feature/voorbeeld` en controleer zo nodig de tracking. Als de remote branch nog niet bestaat, maak de lokale branch vanaf de actuele standaardbranch en publiceer met `git push -u origin <branch>`; verwar deze twee scenario's niet.

### Bestaande getrackte featurebranch — normale volgende update

```powershell
git pull
```

**Dat is alles.** Niet onnodig `git fetch` + `git merge` voorschrijven en zeker geen `git pull` op de Ubuntu-runtime. Geef alleen extra stappen als er werkelijk een afwijkende branch, conflict of ontbrekende tracking is.

### Na geautoriseerde PR/merge naar de standaardbranch

```powershell
git switch main
git pull
```

Gebruik `master` als dat de feitelijke standaardbranch is. Alleen branches verwijderen als dat passend en gewenst is; bevestig verwijdering apart en gooi geen werk weg.

### Situaties expliciet onderscheiden

- AI **heeft al naar remote featurebranch gecommit** → Johan **haalt op** (eerste keer tracken, daarna `git pull`).
- Johan **heeft lokaal geprogrammeerd** → Johan commit/pusht lokaal. Een remote `git pull` is dan niet automatisch de eerstvolgende stap.
- Code is **nog niet geschreven** → presenteer geen `git pull` alsof er iets klaarstaat.
- Branch is **al goed getrackt en actueel** → verzin geen extra handelingen.

## 5. Ontwikkelen: klein, herbruikbaar, framework-first

1. Begrijp eerst het functionele doel, alle betrokken routes en wat niet mag veranderen.
2. Gebruik bestaande modellen, services, patronen en frameworkmogelijkheden. Voor Laravel/Filament: eerst native Laravel/Filament, pas daarna doelgericht maatwerk.
3. Plaats gedeelde logica op één logische plek wanneer meerdere routes hetzelfde doen; kopieer geen afwijkende oplossingen naar vier plaatsen.
4. Geen ongevraagde herbouw, extra tabellen, migraties, queue-workers, browserscripts, frameworks, packages of nieuwe architectuur.
5. Raak geen andere repositories of legacy-data aan tenzij gevraagd. In een read-only legacy-bron nooit writes uitvoeren.
6. Houd klantdata, wachtwoorden, tokens, API-keys, privébestanden en `.env` uit commits, testsnapshots, chatvoorbeelden en documentatie.
7. Voorkom regressies: behoud betekenis van bestaande gegevens, bestandsformaten, historisch verzonden e-mails, API-contracten en reeds goedgekeurde assets.
8. Doe geen gevaarlijke acties op levende bedrijfsdata zonder expliciet akkoord: resets, destructieve migrations, verwijderingen, live-mail sends of onomkeerbare bulkacties.

Bij gevoelige wijzigingen expliciet aangeven **waarom** een bestand moet veranderen. Repareer de oorzaak, niet willekeurig het symptoom.

## 6. Testen en bewijzen — geen aannames als resultaat presenteren

Voor elke codewijziging passend bij het risico:

1. Controleer de gewijzigde code en vergelijk de diff met de opdracht.
2. Voeg waar nodig gerichte regressietests toe, inclusief het oude foutscenario en ontbrekende/afwijkende data.
3. Gebruik de **projectspecifieke** testomgeving. Bestaande testdatabase en testframework zijn leidend: niet spontaan SQLite of een nieuwe testdatabase introduceren.
4. Voer tests uit als de benodigde toegang bestaat; anders geef Johan **de exacte opdracht**, met het **juiste pad en de juiste runtime**.
5. Laat het relevante gedrag in de echte app of browser bevestigen. Voorbeelden: mailpreview, routekeuze, upload, export, assetweergave.
6. Voor grotere features: volledige relevante projecttestsuite, tenzij anders afgesproken.
7. Maak status onderscheidbaar: **code gereed**, **tests nog niet gedraaid**, **tests groen volgens Johan**, **functioneel bevestigd**, **klaar voor merge**.

Een test is niet 'groen' omdat hij is toegevoegd. Een geslaagde GitHub-commit is geen geslaagde runtime-test. Herhaal geen onnodige checks als de betreffende test en browsercontrole al overtuigend zijn uitgevoerd.

## 7. Hoe AI commando's toont — dit maakt de samenwerking prettig

Gebruik voor ieder werkelijk noodzakelijk commando een **expliciet omgevingslabel**:

**PhpStorm-terminal op Windows:**

```powershell
git pull
```

**Ubuntu via SSH/PuTTY (alleen als deze repo daar draait):**

```bash
cd /pad/naar/het-project
php8.5 artisan test tests/Feature/VoorbeeldTest.php
```

De Ubuntu-commando's zijn **voorbeelden**; bepaal de juiste runtime en testbestanden uit de repository. Schrijf nooit een generiek `php artisan` of verkeerde projectmap als het project een expliciete PHP-versie gebruikt.

**Aan Johan communiceren:**

- Zeg eerst concreet wat gevonden en gewijzigd is (en waar).
- Meld branchnaam, commit/PR als die werkelijk bestaat.
- Geef precies de **volgende** stap die Johan moet doen, niet een lang installatiescript.
- Scheid duidelijk Windows/PhpStorm, Ubuntu/runtime en browsercontrole.
- Zeg expliciet welke tests je zelf hebt uitgevoerd, welke Johan nog uitvoert, en wat zijn bevestiging al bewijst.
- Geen vals 'klaar' of 'alles getest'; geen bevelen om te wachten en geen onnodige bevestigingsvragen.

### Kort handoffvoorbeeld: eerste keer naar remote featurebranch

**PhpStorm-terminal op Windows:**

```powershell
git fetch origin
git switch --track origin/feature/voorbeeld
```

**Daarna op Ubuntu** *(alleen in een repo met werkende auto-upload, wanneer runtime-tests nodig zijn)*:

```bash
cd /pad/naar/het-project
php8.5 artisan test tests/Feature/VoorbeeldTest.php
```

**Tot slot:** controleer de betreffende functie in de browser. Geen extra uploadstap bij bewezen auto-upload.

### Kort handoffvoorbeeld: vervolg op dezelfde branch

> De code is gecommit op de bestaande featurebranch. In de PhpStorm-terminal is alleen `git pull` nodig. PhpStorm uploadt automatisch. Daarna [gerichte test/controle indien nodig].

### Kort handoffvoorbeeld: na merge

> PR #... is daadwerkelijk gemerged in `main`. In de PhpStorm-terminal: `git switch main` en `git pull`. Geen Git-commando's op Ubuntu.

## 8. Reikwijdte en toestemmingen

**Zonder aparte toestemming wel, als onderdeel van een expliciete codefix:** gerichte repo-inspectie, nieuwe featurebranch, kleine codewijzigingen, bijpassende tests en relevante documentatie, commits naar de featurebranch.

**Eerst toestemming nodig:** een pull request aanmaken/mergen als dat de repo-afspraak is; verwijderen van branches met mogelijk werk; veranderingen aan productieconfiguratie, databases en services met reëel risico; live externe communicatie; verwijderen van bestanden/gegevens; brede refactors buiten de gevraagde wijziging. Wanneer Johan expliciet alleen onderzoek wil, is *iedere* implementatie prematuur.

Het bestaan van tooltoegang betekent niet dat een wijziging al is uitgevoerd. Controleer de tooluitkomst en claim pas na bevestiging dat een branch, bestand, commit of merge daadwerkelijk bestaat.

## 9. Documentatie die een nieuwe chat weer bij het project brengt

Een goed onderhouden repository heeft idealiter drie lagen:

| Bestand | Functie |
|---|---|
| `AI_PROJECT_CONTEXT.md` | **Wat** het project is, huidige status, architectuur, vastgelegde besluiten, grenzen, actuele stack en verwijzingen. |
| `docs/DEVELOPMENT_WORKFLOW.md` | **Hoe** dit project lokaal/remote wordt ontwikkeld, gesynchroniseerd, getest en gemerged — met werkende paden en commando's. |
| `docs/AI_COLLABORATION_STANDARD.md` | **Hoe AI en Johan samenwerken** volgens deze algemene basis; projectafwijkingen verwijzen naar de eigen workflow. |

Bestaande productcanon/ADR's behouden hun eigen gezag. Een `AGENTS.md`, `CLAUDE.md`, projectinstructie of IDE-regel kan naar bovenstaande documenten verwijzen, maar moet **geen concurrerende, verouderende tweede werkelijkheid** worden.

**Bij elke relevante verandering** update je de projectcontext of workflow **in dezelfde featurebranch**, niet pas in een nieuw gesprek. Lange historische changelogs horen niet per se in de actuele context; link naar relevante commits/ADR's.

**Voor nieuwe ChatGPT-projecten:** zet een korte opdracht in de projectinstructies: lees bij ieder ontwikkelverzoek eerst de actuele repo, `AI_PROJECT_CONTEXT.md`, `docs/DEVELOPMENT_WORKFLOW.md`, `docs/AI_COLLABORATION_STANDARD.md` en de relevante besluiten. Vertrouw niet uitsluitend op geheugen van eerdere chats.

## 10. Projectspecifieke verschillen niet gladstrijken

- `livome-intern-laravel`: `main`, PhpStorm/Windows Git, SFTP-auto-upload naar Ubuntu, PHP 8.5, MySQL-tests; bestaande workflow is leidend.
- `livome-step`: heeft op dit moment `master` als standaardbranch en eigen `AGENTS.md`/`CLAUDE.md` met Laravel-Boost-setup-instructies. Eerst zorgvuldig afstemmen met feitelijke installatie/runtime; **niet blind pakketten installeren omdat een generiek bootstrapbestand dat zegt**.
- `livome-vault`: bestaande uitgebreide `AI_PROJECT_CONTEXT.md`, architectuur en ADR's zijn leidend; WAMP-/appliance-/securitycontext mag niet worden overschreven door de Ubuntu-aanpak van Livome Intern.
- `livome-vault-laravel`: eigen Laravel-repository; workflow en stack eerst inventariseren en projectdocs expliciet aanmaken.
- `yupi-game`: bestaande Game Bible, character specs, asset pipeline en `AI_JOHAN.md` bepalen de canon en handoff; afbeeldingen en sprites hebben harde visuele acceptatiecriteria. **Niet** reduceren tot code-/Artisan-tests.
- Overige repositories: afzonderlijk inventariseren vóór toepassing. Een historische/legacy-repo niet behandelen als het actieve product.

Deze repo-observaties zijn een **startpunt (19 oktober 2026)** en moeten vóór wijzigingen opnieuw gecontroleerd worden; ze zijn geen blijvende actuele toestand.

## 11. Definitie van 'klaar'

Een taak is pas afgerond wanneer, voor zover van toepassing:

- [ ] De gevraagde werking is duidelijk en de bestaande situatie is geïnspecteerd.
- [ ] De wijziging beperkt blijft tot de afgesproken scope.
- [ ] De branch correct bestaat en tracking is geregeld.
- [ ] De code op de bedoelde branch staat; de diff is gecontroleerd.
- [ ] Relevante geautomatiseerde tests zijn groen, of het ontbreken daarvan is eerlijk gemeld.
- [ ] Johan heeft de relevante werking bevestigd wanneer browser-/runtimecontrole nodig is.
- [ ] Documentatie is bijgewerkt waar afspraken of gedrag veranderden.
- [ ] PR/merge is pas na expliciet akkoord gebeurd.
- [ ] Johan krijgt alleen de nog benodigde lokale/serverstappen; geen dubbel werk.

**Kernzin om te onthouden:** *Controleer de echte repo. Respecteer het bestaande project. Doe alleen het benodigde. Lever correct via Git. Geef Johan de juiste opdracht op de juiste computer. Test. Merge pas samen.*