# Data och distribuerade transaktioner

Utgå från verksamhetens konsistensbehov och dataägande, inte från ett önskat lagringsverktyg. Definiera invariants: vilka regler måste vara sanna omedelbart och vilka kan konvergera senare?

## Shared database

**Lösning:** Flera moduler eller tjänster läser och skriver i samma databas eller schema.

- **Välj när:** starka gemensamma transaktioner är viktiga, ägarskapet är samlat och självständig schemaevolution inte behövs.
- **Fördelar:** enkla joins, gemensamma transaktioner och låg initial driftkostnad.
- **Nackdelar/risker:** stark schema- och releasekoppling, oklart dataägande och svår isolering.
- **Välj database per service när:** självständig förändring och tydligt ägande väger tyngre än gemensamma transaktioner.

## Database per service

**Lösning:** Varje tjänst äger sin data och exponerar den genom kontrakt i stället för direkt tabellåtkomst.

- **Välj när:** tjänster behöver autonom schema- och leveranslivscykel och domängränserna är tydliga.
- **Fördelar:** isolerat ägande, lokal optimering och mindre schema-koppling.
- **Nackdelar/risker:** distribuerade frågor, dataduplicering och konsistens blir explicita systemproblem.
- **Undvik när:** tjänsterna inte är autonoma eller nästan alla use cases kräver gemensamma joins och transaktioner.

## Saga

**Lösning:** Ett affärsflöde delas i lokala transaktioner. Vid fel används verksamhetsmässiga kompensationer eller framåtriktad återhämtning.

- **Välj när:** ett långlivat flöde korsar autonoma dataägare och global ACID-transaktion inte är lämplig.
- **Fördelar:** bevarar lokalt ägande och kan hantera långvariga processer.
- **Nackdelar/risker:** mellanlägen blir synliga, kompensation är inte rollback och felhantering blir domänlogik.
- **Välj enklare transaktion när:** berörda data rimligen kan ligga inom samma gräns och omedelbar konsistens krävs.

### Orkestrering eller koreografi

- **Orkestrering:** en koordinator styr nästa steg. Välj när flödet behöver explicit status, tidsgränser, överblick och central förändring. Risk: koordinatorn kan samla för mycket domänlogik.
- **Koreografi:** deltagare reagerar på events. Välj för få, löst kopplade reaktioner med lokalt ansvar. Risk: flödet blir dolt, cykliskt och svårt att felsöka.
- Föredra orkestrering när antalet steg, undantag och verksamhetsregler växer. Använd inte koreografi enbart för att undvika ordet central.

## Transactional outbox

**Lösning:** Skriv domänändring och utgående meddelandepost i samma lokala transaktion; en separat publisher skickar posten senare.

- **Välj när:** en lokal dataskrivning och meddelandepublicering måste hänga ihop utan distribuerad transaktion.
- **Fördelar:** undviker glappet där data sparas men eventet förloras.
- **Nackdelar/risker:** minst en gång-publicering, städning, ordning och publisherdrift måste hanteras.
- **Komplettera med:** idempotent consumer, korrelations-id och övervakning av eftersläpning.

## Idempotent consumer / inbox

**Lösning:** Konsumenten kan behandla samma meddelande flera gånger utan extra verksamhetseffekt, ofta genom en unik nyckel eller inboxpost.

- **Välj när:** omleverans kan ske eller producentens utfall är osäkert.
- **Fördelar:** gör minst-en-gång-leverans praktiskt hanterbar.
- **Nackdelar/risker:** dedupliceringsdata måste ha rätt livslängd; externa sidoeffekter kan vara svåra att göra idempotenta.
- **Undvik falsk lösning:** att bara kvittera dubbletten räcker inte om den första bearbetningen delvis misslyckades.

## CQRS

**Lösning:** Separera modeller eller vägar för kommandon och frågor; separationen kan vara logisk eller fysisk.

- **Välj när:** läs- och skrivsidan har väsentligt olika modeller, skalning, säkerhet eller optimeringsbehov.
- **Fördelar:** varje sida kan optimeras för sitt ansvar och komplex domänskrivning behöver inte forma läsning.
- **Nackdelar/risker:** duplicering, synkronisering, eventual consistency och fler modeller att förstå.
- **Välj CRUD eller gemensam modell när:** behoven är symmetriska och enkelheten väger tyngst.
- **Viktigt:** CQRS kräver inte event sourcing.

## Event sourcing

**Lösning:** Den auktoritativa historiken lagras som en sekvens av domänhändelser; aktuellt tillstånd härleds genom uppspelning eller projektioner.

- **Välj när:** fullständig verksamhetshistorik, tidsresor, alternativa projektioner eller händelsebaserad domän är centrala krav.
- **Fördelar:** oföränderlig historik, möjlighet att skapa nya vyer och analysera hur tillstånd uppstod.
- **Nackdelar/risker:** eventversionering, korrigering av känsliga/felaktiga data, projektioner, felsökning och hög kompetenskostnad.
- **Välj auditlogg eller temporal lagring när:** revisionsspår behövs men eventströmmen inte ska vara auktoritativ modell.
- **Undvik när:** motivet främst är framtida flexibilitet utan konkreta use cases.

## Materialized view

**Lösning:** Förberäkna och lagra en läsoptimerad vy från en eller flera källor.

- **Välj när:** frågan är dyr, läses ofta och viss eftersläpning kan accepteras.
- **Fördelar:** snabb och enkel läsning, kan kombinera data över ägargränser.
- **Nackdelar/risker:** färskhet, återbyggnad, schemaevolution och korrigering måste hanteras.
- **Välj direkt fråga när:** datamängd och trafik är liten eller strikt färskhet krävs.

## Change data capture, CDC

**Lösning:** Fånga förändringar från databasens logg eller motsvarande och publicera dem för vidare bearbetning.

- **Välj när:** befintliga skrivflöden inte enkelt kan publicera events eller replikering behöver låg påverkan.
- **Fördelar:** fångar committed förändringar utan dual write i applikationen.
- **Nackdelar/risker:** databasens tekniska schema blir kontrakt; domänsemantik och avsikt kan saknas.
- **Välj transactional outbox när:** domänhändelsen behöver uttryckas explicit och applikationen kan ändras.

## Cache-aside

**Lösning:** Applikationen läser först cache, fyller den från datakällan vid miss och invaliderar eller uppdaterar vid förändring.

- **Välj när:** läsningar är dyra eller frekventa och viss stale data kan hanteras.
- **Fördelar:** enkel, efterfrågestyrd cache och avlastning av källan.
- **Nackdelar/risker:** cache stampede, inaktuella värden, invalideringsfel och kallstart.
- **Välj ingen cache när:** prestandakravet uppfylls utan den; cache är duplicerat tillstånd med konsistenskostnad.

## Kritiska frågor före beslut

1. Vilka invariants måste hållas inom en enda transaktion?
2. Vad får användaren se under ett mellanläge?
3. Hur upptäcks och repareras fastnade flöden?
4. Hur hanteras dubbletter, ordning och sena meddelanden?
5. Kan projektioner eller repliker byggas om deterministiskt?
6. Hur korrigeras eller raderas data som har spridits?
7. Vem äger kontrakt och data över hela livscykeln?
