# Resiliens, skalning och moln

Resiliens skapas av en sammanhängande felstrategi. Lägg inte till retry, circuit breaker och autoscaling som en checklista; analysera feltyp, tidsbudget, idempotens och systemets totala återkopplingsloopar.

## Timeout

**Lösning:** Begränsa hur länge en operation får använda väntande resurser.

- **Välj när:** ett externt eller distribuerat anrop kan bli långsamt eller fastna.
- **Fördelar:** skyddar trådar, anslutningar och användarens totala tidsbudget.
- **Nackdelar/risker:** det underliggande arbetet kan fortsätta; för kort timeout skapar egna fel.
- **Verifiera:** härled från end-to-end-budget, mät latensfördelning och definiera vad som händer efter timeout.

## Retry med backoff och jitter

**Lösning:** Försök igen vid sannolikt övergående fel, med växande väntan och slumpvariation.

- **Välj när:** operationen är idempotent eller säkert deduplicerad och felet har rimlig chans att försvinna inom tidsbudgeten.
- **Fördelar:** döljer korta nätverks- och kapacitetsstörningar.
- **Nackdelar/risker:** förstärker belastning, förlänger svarstid och kan upprepa sidoeffekter.
- **Undvik när:** felet är permanent, beroendet redan är överlastat eller operationens utfall är okänt och inte idempotent.

## Circuit breaker

**Lösning:** Stoppa tillfälligt anrop till ett beroende efter återkommande fel och pröva kontrollerat om det återhämtat sig.

- **Välj när:** ett långsamt eller felande beroende annars förbrukar resurser och felet kan detekteras meningsfullt.
- **Fördelar:** snabbare fel, minskad kaskadbelastning och utrymme för återhämtning.
- **Nackdelar/risker:** trösklar är svåra, delad respektive lokal brytarstatus ger olika beteende och fallback kan bli farligt inaktuell.
- **Välj enbart timeout när:** felvolymen är låg och brytarens tillstånd inte ger extra skydd.

## Bulkhead

**Lösning:** Dela resurspooler eller kapacitetsbudgetar så att en funktion eller kund inte kan tömma allt.

- **Välj när:** arbetslaster har olika kritikalitet eller riskerar att blockera varandra.
- **Fördelar:** begränsar blast radius och bevarar prioriterad kapacitet.
- **Nackdelar/risker:** sämre total resursutnyttjande och risk för felaktig dimensionering.
- **Välj enkel gemensam pool när:** lasten är homogen och isolering inte motiverar reserverad kapacitet.

## Rate limiting

**Lösning:** Begränsa antal eller kostnad av operationer per tid, identitet eller resurs.

- **Välj när:** rättvis användning, avtalad kvot eller skydd mot oavsiktlig/missbrukande trafik behövs.
- **Fördelar:** förutsägbar belastning och tydlig återkoppling till klienten.
- **Nackdelar/risker:** distribuerad räknarstatus, bursts och felaktiga nycklar kan ge orättvisa avslag.
- **Komplettera med:** svar som anger återförsök, klientbackoff och separat skydd för dyr intern fan-out.

## Load shedding

**Lösning:** Avvisa eller degradera lågprioriterat arbete när systemet närmar sig ohälsosam mättnad.

- **Välj när:** kontrollerad försämring är bättre än total kollaps.
- **Fördelar:** skyddar kärnfunktion och kan hålla latensen stabil.
- **Nackdelar/risker:** kräver prioriteringar och kan ge oproportionerlig påverkan om signalerna är dåliga.
- **Välj kö när:** arbetet kan slutföras senare och kökapaciteten är begränsad och övervakad.

## Queue-based load leveling

**Lösning:** Placera arbete i en kö och låt konsumentkapaciteten bearbeta det i hållbar takt.

- **Välj när:** toppar kan jämnas ut och användaren inte behöver omedelbart slutresultat.
- **Fördelar:** absorberar variation och separerar inmatningstakt från bearbetning.
- **Nackdelar/risker:** köer kan dölja överlast, växa utan gräns och förvandla korta fel till långa eftersläpningar.
- **Verifiera:** maximal köålder, kapacitet, prioritering, dead-letter-hantering och återställningstid.

## Health endpoint

**Lösning:** Exponera separata signaler för processens liv, beredskap att ta trafik och relevant startstatus.

- **Välj när:** orkestrering eller lastbalansering behöver fatta automatiska trafik- och restartbeslut.
- **Fördelar:** snabbare automatisk återhämtning och bättre routing.
- **Nackdelar/risker:** en tung kontroll kan skapa belastning; felaktig liveness kan orsaka restart-loopar.
- **Regel:** liveness ska normalt inte bero på alla externa tjänster. Readiness kan vara selektivt beroende av vad instansen måste kunna göra.

## Stateless service och externalized state

**Lösning:** Håll instanser utbytbara och lagra beständigt eller delat tillstånd i avsedda externa tjänster.

- **Välj när:** horisontell skalning, snabb ersättning och flexibel placering behövs.
- **Fördelar:** enklare lastfördelning och återstart.
- **Nackdelar/risker:** externa tillståndstjänster blir kritiska; nätverkslatens och konsistens flyttas utanför processen.
- **Välj lokalt tillstånd när:** datalokalitet och specialiserad partitionering är viktigare och systemet kan hantera ägarskap och återbalansering.

## Autoscaling

**Lösning:** Anpassa instans- eller resurskapacitet från mätbara belastningssignaler.

- **Välj när:** lasten varierar, instanser kan läggas till inom relevant tid och flaskhalsen faktiskt skalar horisontellt.
- **Fördelar:** kapacitet följer behov och kan minska kostnad.
- **Nackdelar/risker:** fördröjda signaler, oscillation, kallstart och skalning mot ett redan mättat beroende.
- **Välj fast kapacitet när:** lasten är stabil, starttiden lång eller kostnaden för variation är större än besparingen.

## Leader election

**Lösning:** Flera instanser deltar men endast en utför ett visst koordinerande ansvar åt gången.

- **Välj när:** ett periodiskt eller exklusivt arbete måste ha en aktiv ägare men instansen ska kunna ersättas.
- **Fördelar:** automatiskt övertagande utan fast server.
- **Nackdelar/risker:** split brain, lease-förnyelse, klock- och nätverkspartitioner; fencing kan krävas.
- **Välj partitionerat ägande när:** arbetet kan delas och en global ledare blir flaskhals.

## Sharding / partitioning

**Lösning:** Dela data och arbete efter en nyckel så att varje partition kan lagras eller bearbetas separat.

- **Välj när:** en enda nod eller databas inte möter kapacitetskrav och åtkomst har en användbar partitioneringsnyckel.
- **Fördelar:** horisontell kapacitet och möjlighet till isolering.
- **Nackdelar/risker:** heta nycklar, tvärpartitionella frågor, återbalansering och mer komplicerade transaktioner.
- **Välj vertikal skalning eller repliker när:** gränsen ännu inte är nådd eller problemet främst gäller läsning.

## Sidecar

**Lösning:** Kör en hjälpprocess nära applikationen för tvärgående nätverks-, säkerhets- eller observationsfunktioner.

- **Välj när:** samma tekniska förmåga måste appliceras konsekvent över flera teknikstackar och den lokala nätverksgränsen är meningsfull.
- **Fördelar:** separerad livscykel från applikationskod och gemensam implementering.
- **Nackdelar/risker:** resurskostnad per instans, fler felmoder och svårare felsökning av anropsvägen.
- **Välj bibliotek eller plattformstjänst när:** en enklare in-process- eller central lösning ger tillräcklig standardisering.

## Deployment stamps / cells

**Lösning:** Replikera en komplett uppsättning tjänster och dataresurser för en avgränsad grupp kunder, region eller belastning.

- **Välj när:** blast radius, geografisk placering, tenant-isolering eller mycket stor skala kräver oberoende celler.
- **Fördelar:** fel- och kapacitetsisolering samt stegvis utrullning.
- **Nackdelar/risker:** högre driftkostnad, global routing, flercellsdata och ojämnt utnyttjande.
- **Välj gemensam plattform när:** isoleringskravet inte motiverar duplicerad infrastruktur.

## Systemiska varningar

- Summera retry-försök över hela anropskedjan; tre lager med tre försök kan ge kraftig multiplikation.
- Autoscaling botar inte databaslåsning, extern kvot eller algoritmisk ineffektivitet.
- Fallback ska vara verksamhetsmässigt säker, inte bara tekniskt tillgänglig.
- Köer, circuit breakers och caches skapar tillstånd som måste observeras, testas och återställas.
- Testa degradering och återhämtning, inte enbart normal kapacitet.
