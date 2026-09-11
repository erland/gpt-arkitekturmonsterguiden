# Applikations- och tjänstearkitektur

Mönstren i detta dokument påverkar olika nivåer. Kombinera dem bara när ansvar och nivå är tydliga; en microservice kan exempelvis ha hexagonal intern struktur.

## Layered architecture

**Problem:** Organisera en applikation så att presentation, applikationslogik, domän och teknisk åtkomst inte blandas godtyckligt.

**Lösning:** Dela ansvar i lager med uttalade beroenderegler.

- **Välj när:** domänen är relativt enkel, teamet behöver en välkänd struktur och flöden ofta passerar samma lager.
- **Fördelar:** lätt att förstå, etablerat verktygsstöd, tydlig första separation.
- **Nackdelar/risker:** lager kan bli tunna passager; tekniska lager kan splittra en sammanhängande funktion; beroenden läcker lätt åt båda håll.
- **Välj annat när:** oberoende use cases eller stark domänisolering är viktigare; överväg vertical slices eller hexagonal struktur.

## Hexagonal architecture / Ports and adapters

**Problem:** Domän- och applikationslogik blir beroende av databas, ramverk, UI och externa tjänster.

**Lösning:** Kärnan uttrycker portar; adaptrar kopplar tekniska gränssnitt till portarna. Beroenden pekar mot kärnan.

- **Välj när:** domänlogiken behöver testas isolerat, externa beroenden kan bytas eller flera gränssnitt använder samma kärna.
- **Fördelar:** tydliga gränser, testbarhet, mindre ramverkskoppling.
- **Nackdelar/risker:** fler abstraktioner och mappningar; mekanisk användning ger ceremonier utan värde.
- **Välj annat när:** applikationen främst är enkel datalagring med låg förändring; en måttlig lagerindelning kan räcka.

## Clean architecture

**Problem:** Affärsregler påverkas av leveransmekanismer och tekniska detaljer.

**Lösning:** Ordna ansvar i koncentriska nivåer och låt källkodsberoenden peka inåt mot stabilare regler.

- **Välj när:** långlivad och komplex domänlogik behöver skyddas från teknisk förändring.
- **Fördelar:** explicit beroenderiktning och stark separation mellan policy och mekanism.
- **Nackdelar/risker:** många lager och modeller kan ge hög kognitiv kostnad; begreppet tillämpas ofta dogmatiskt.
- **Välj annat när:** en mindre hexagonal variant ger samma nödvändiga isolering med färre delar.

## Modular monolith

**Problem:** En monolit behöver tydliga förändrings- och ägargränser utan distribuerad drift.

**Lösning:** En driftsättningsenhet delas i sammanhållna moduler med explicita API:er och kontrollerade data- och kodberoenden.

- **Välj när:** domängränser kan identifieras men självständig skalning och driftsättning inte är avgörande.
- **Fördelar:** transaktionell enkelhet, lokal felsökning, lägre operativ kostnad och möjlighet till senare extraktion.
- **Nackdelar/risker:** gränser kan eroderas; hela systemet driftsätts och ofta skalas tillsammans.
- **Välj microservices när:** oberoende livscykel, teamautonomi, isolering eller olika skalningsprofiler har bevisat värde som överstiger distributionskostnaden.

## Microservices

**Problem:** Delar av ett stort system behöver utvecklas, driftsättas, skalas eller isoleras oberoende.

**Lösning:** Dela systemet i autonoma tjänster kring tydliga förmågor, med egna livscykler och normalt eget dataägande.

- **Välj när:** stabila domängränser finns, flera team behöver autonomi och organisationen klarar distribuerad drift.
- **Fördelar:** oberoende leverans och skalning, bättre felisolering när systemet utformas för det, lokal teknisk utveckling.
- **Nackdelar/risker:** nätverksfel, eventual consistency, svårare testning, observerbarhet, säkerhet och hög plattformskostnad.
- **Undvik när:** ett litet team äger allt, gränserna är okända, delarna ändras tillsammans eller problemet främst är dålig intern modularitet.
- **Välj service-based architecture när:** ett fåtal grövre tjänster ger tillräcklig autonomi med lägre komplexitet.

## Service-based architecture

**Problem:** En enda driftsättningsenhet begränsar självständig leverans, men finfördelade microservices är omotiverade.

**Lösning:** Dela lösningen i ett mindre antal grövre tjänster, ofta med färre data- och integrationsgränser.

- **Välj när:** vissa delar behöver olika livscykel eller skala, men team och domän gynnas av grövre gränser.
- **Fördelar:** balans mellan autonomi och hanterbar drift.
- **Nackdelar/risker:** delade databaser kan skapa dold koppling; tjänster kan bli osammanhängande mini-monoliter.
- **Välj modular monolith när:** självständig driftsättning saknar konkret nytta.

## Microkernel / Plugin architecture

**Problem:** En stabil kärna behöver kunna utökas med varierande eller tredjepartsfunktioner.

**Lösning:** Håll minsta gemensamma beteende i en kärna och anslut tillägg genom ett stabilt plugin-kontrakt.

- **Välj när:** produktvarianter, kundspecifika tillägg eller ett ekosystem är centrala.
- **Fördelar:** isolerad utbyggbarhet och möjlighet att distribuera funktioner separat.
- **Nackdelar/risker:** kontraktsversionering, livscykel, säkerhet och kompatibilitet blir kärnproblem.
- **Välj annat när:** variationen är intern och liten; modulär monolit eller feature toggles kan räcka.

## Vertical slice architecture

**Problem:** Tekniska lager gör varje verksamhetsförändring tvärgående och skapar hög samordningskostnad.

**Lösning:** Organisera kod kring användningsfall eller funktionella snitt som innehåller nödvändiga delar från gränssnitt till dataåtkomst.

- **Välj när:** funktioner förändras relativt oberoende och team arbetar use-case-orienterat.
- **Fördelar:** lokal förändring, mindre korskoppling och tydligare leveransflöde.
- **Nackdelar/risker:** duplicering kan öka; gemensamma regler kan spridas om gränserna missförstås.
- **Välj lager eller hexagonal kärna när:** många use cases delar komplexa domänregler som behöver en gemensam modell.

## Viktiga kombinationer och beslut

- Börja ofta med en modulär monolit och extrahera endast moduler som får bevisat behov av autonomi.
- Använd inte hexagonal eller clean architecture som argument för fler driftsättningsenheter; de beskriver främst intern beroendestruktur.
- Vertical slices och hexagonal struktur kan kombineras, men undvik dubbla abstraktionslager utan konkret nytta.
- Mät förändringskoppling: om två delar nästan alltid ändras och driftsätts tillsammans är en distribuerad gräns misstänkt.
