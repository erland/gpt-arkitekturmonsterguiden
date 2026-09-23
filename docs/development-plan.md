# Utvecklingsplan – Arkitekturmönsterguiden

## 1. Projektmål

Arkitekturmönsterguiden ska hjälpa användaren att välja arkitekturmönster för system, integration, distribuerade lösningar och molnmiljöer. GPT:n ska utgå från ett beskrivet problem eller behov, synliggöra arkitekturdrivande krav och rekommendera ett eller flera mönster med tydliga avvägningar.

GPT:n ska vara beslutsorienterad. Den ska inte bara återge en mönsterkatalog, utan förklara varför ett mönster passar, vilka nackdelar och risker det medför samt när alternativa mönster bör väljas.

## 2. Målgrupp

Primär målgrupp:

- IT-arkitekter och lösningsarkitekter
- systemarkitekter och seniora utvecklare
- tekniska ledare som förbereder eller granskar arkitekturbeslut

Sekundär målgrupp:

- utvecklare som behöver förstå ett mönsterval
- produkt- och projektroller som behöver ett begripligt beslutsunderlag

## 3. Avgränsning för första versionen

Följande områden ingår:

- applikationsarkitektur
- integrationsmönster
- distribuerade system
- eventdriven arkitektur
- microservices och modulära monoliter
- datahantering, transaktioner och konsistens
- resiliens och feltolerans
- skalbarhet och prestanda
- moln- och cloud-native-mönster

Följande områden behandlas endast när de direkt påverkar ett systemmönster:

- verksamhetsarkitektur
- informationsarkitektur på organisationsnivå
- organisations- och styrmodeller
- detaljerad produktspecifik konfiguration
- fullständig hotmodellering eller säkerhetsgranskning

## 4. Önskat kärnbeteende

GPT:n ska:

1. tolka problemet och återge sin förståelse,
2. identifiera relevanta arkitekturdrivande krav och begränsningar,
3. skilja fakta, antaganden och situationsberoende bedömningar,
4. ställa frågor endast när svaret kan förändra rekommendationen väsentligt,
5. rekommendera ett mönster eller en motiverad kombination av mönster,
6. beskriva mönstrens funktion, fördelar, nackdelar och risker,
7. jämföra de viktigaste alternativen,
8. ange konkreta villkor som talar för att välja ett alternativ i stället,
9. varna för antimönster, överdesign och olämplig användning,
10. avsluta med rekommendation, kvarstående osäkerheter och lämpliga nästa analyser.

## 5. Rekommenderad projektarkitektur

- **Projektprofil:** `standard`
- **Canonical källa:** en gemensam instruktion och ett gemensamt capability-kontrakt
- **Distributioner:** Chat ZIP och Custom GPT
- **Knowledge:** strukturerad mönsterkatalog med gemensam mall och tvärgående beslutsstöd
- **Webbsökning:** rekommenderas för aktuella, produktberoende eller versionsberoende frågor; grundfunktionen ska fungera utan webben
- **Dataanalys:** inte nödvändig för kärnflödet
- **Bildgenerering:** inte nödvändig
- **GitHub:** README, CI och release-workflow ingår som standard
- **Versionering:** GitHub Release-taggen styr releaseartefakternas version

## 6. Planerade utvecklingssteg

Varje genomförandesteg ska kunna utföras med en separat begäran av typen ”Gör nästa steg”. Efter varje steg ska status, relevanta tester och filhygien uppdateras och en komplett projekt-ZIP byggas.

### Steg 1 – Analysera idé och målbild

**Status:** Klar

**Mål:** Fastställa syfte, målgrupp, ämnesmässig omfattning och önskat arbetssätt.

**Klart när:**

- mål och målgrupp är definierade,
- omfattningen är avgränsad till system, integration, distribuerade lösningar och moln,
- önskat svars- och rekommendationsbeteende är beskrivet,
- projektprofil och normala distributioner är rekommenderade.

### Steg 2 – Skapa utvecklingsplan

**Status:** Klar

**Mål:** Skapa en projektspecifik plan med små, verifierbara utvecklingssteg.

**Klart när:**

- planen finns som Markdown,
- varje steg har mål och klart-kriterier,
- beroenden, tester, distribution och release ingår.

### Steg 3 – Skapa projektgrund och första projekt-ZIP

**Status:** Klar

**Mål:** Skapa ett komplett, återupptagningsbart GPT-projekt.

**Leveranser:**

- `gpt-project.yaml`
- `project-status.yaml`
- `PROJECT.md`
- `STATUS.md`
- `README.md`
- `docs/development-plan.md`
- grundstruktur för instruktion, Knowledge, tester, evals, schemas och scripts
- grundläggande GitHub Actions för CI och release
- första kompletta projekt-ZIP

**Klart när:**

- projektet kan valideras strukturellt,
- projektstatus motsvarar utfört arbete,
- projekt-ZIP:en räcker för att återuppta utvecklingen.

### Steg 4 – Definiera capability-kontrakt och instruktionsarkitektur

**Status:** Klar

**Mål:** Definiera GPT:ns funktionella förmågor, prioriteringar och obligatoriska kärnflöde.

**Klart när:**

- kritiska, viktiga och valfria capabilities är dokumenterade,
- kärnbeteendet kan förstås utan obligatoriska Knowledge-filshopp,
- konflikthantering och prioriteringsregler är definierade,
- Chat ZIP och Custom GPT kan härledas från samma kontrakt.

### Steg 5 – Utforma analys- och rekommendationsmetoden

**Status:** Klar

**Mål:** Skapa en reproducerbar metod för att gå från problem till mönsterrekommendation.

Metoden ska bland annat bedöma:

- funktionella behov och systemgränser,
- tillgänglighet, resiliens och återställning,
- prestanda, lastprofil och skalbarhet,
- konsistens, transaktioner och datalivscykel,
- koppling, förändringstakt och teamautonomi,
- säkerhet, integritet och regelefterlevnad när relevant,
- driftbarhet, observerbarhet, kostnad och kompetens,
- reversibilitet och migrationsrisk.

**Klart när:**

- analysordningen är tydlig,
- regler finns för när följdfrågor behövs,
- GPT:n kan uttrycka antaganden och osäkerhet,
- kombinationer av mönster kan rekommenderas utan att avvägningarna döljs.

### Steg 6 – Definiera mönstermodell och taxonomi

**Status:** Klar

**Mål:** Skapa ett gemensamt format för alla mönster och en användbar klassificering.

Varje mönsterpost ska minst kunna beskriva:

- namn och alternativa namn,
- problem och kontext,
- påverkande krafter,
- lösning och huvudkomponenter,
- lämpliga och olämpliga användningsfall,
- fördelar, nackdelar och risker,
- förutsättningar och konsekvenser,
- relaterade, kompletterande och alternativa mönster,
- signaler för att välja ett alternativ,
- vanliga feltolkningar och antimönster,
- källor och aktualitetsbehov.

**Klart när:**

- taxonomin täcker projektets avgränsning,
- mallen är konsekvent och maskinellt validerbar där det ger nytta,
- korsreferenser kan användas för jämförelser och mönsterkombinationer.

### Steg 7 – Skapa kärnkatalog för applikations- och tjänstearkitektur

**Status:** Klar

**Mål:** Bygga första delen av Knowledge-basen.

Exempel på innehåll:

- layered architecture
- hexagonal architecture, ports and adapters
- clean architecture
- modular monolith
- microservices
- service-based architecture
- microkernel/plugin architecture
- vertical slice architecture

**Klart när:**

- mönstren följer den gemensamma modellen,
- alternativ och valsignaler är dokumenterade,
- överlapp och begreppsskillnader förklaras,
- relevanta evalfall finns eller är förberedda.

### Steg 8 – Skapa kärnkatalog för integration och meddelanden

**Status:** Klar

**Mål:** Bygga beslutsstöd för synkron, asynkron och eventdriven integration.

Exempel på innehåll:

- request/reply och API-baserad integration
- messaging, publish/subscribe och message broker
- event notification och event-carried state transfer
- competing consumers
- message routing, filtering och transformation
- anti-corruption layer
- strangler fig
- API gateway och backend for frontend

**Klart när:**

- mönstren kan jämföras utifrån koppling, latens, leveransgarantier och förändringstakt,
- vanliga kombinationer och risker är dokumenterade,
- GPT:n skiljer integrationsstil från enskild produktteknik.

### Steg 9 – Skapa kärnkatalog för data och distribuerade transaktioner

**Status:** Klar

**Mål:** Bygga beslutsstöd för dataägande, konsistens och transaktioner.

Exempel på innehåll:

- database per service och shared database
- saga med orkestrering respektive koreografi
- transactional outbox och inbox/idempotent consumer
- CQRS
- event sourcing
- materialized view
- change data capture
- cache-aside och andra relevanta cachemönster

**Klart när:**

- konsistens- och transaktionskonsekvenser framgår,
- CQRS och event sourcing behandlas som separata val,
- alternativ för enklare behov lyfts fram,
- risker kring dataduplicering, ordning och idempotens täcks.

### Steg 10 – Skapa kärnkatalog för resiliens, skalning och moln

**Status:** Klar

**Mål:** Bygga beslutsstöd för robusta och skalbara lösningar.

Exempel på innehåll:

- timeout, retry med backoff och jitter
- circuit breaker
- bulkhead
- rate limiting och load shedding
- health endpoint och sidecar
- stateless service och externalized state
- autoscaling och queue-based load leveling
- leader election och sharding/partitioning
- deployment stamps/cells

**Klart när:**

- mönsterinteraktioner och felmoder förklaras,
- GPT:n varnar för exempelvis retry storms och kaskadfel,
- kostnad, driftkomplexitet och observerbarhet ingår i avvägningarna.

### Steg 11 – Utforma svarsmallar och beslutsunderlag

**Status:** Klar

**Mål:** Ge konsekventa men situationsanpassade svar.

Planerade svarslägen:

- snabb rekommendation,
- fördjupad analys,
- jämförelse mellan angivna mönster,
- granskning av ett befintligt mönsterval,
- underlag till Architecture Decision Record, ADR.

**Klart när:**

- standardsvaret följer det definierade kärnbeteendet,
- korta frågor inte automatiskt ger onödigt långa svar,
- jämförelser använder explicita beslutskriterier,
- ADR-underlag skiljer beslut, motiv, alternativ och konsekvenser.

### Steg 12 – Skapa canonical instruktion och runtimeanpassningar

**Status:** Klar

**Mål:** Implementera det samlade beteendet i GPT:ns canonical instruktion.

**Klart när:**

- kärnworkflow, avgränsningar och säkerhetsregler finns i instruktionen,
- Knowledge används som referensmaterial och inte som dold beteendestyrning,
- Custom GPT-instruktionen ryms inom deklarerad plattformsgräns,
- eventuella funktionsskillnader dokumenteras i `COMPATIBILITY.md`.

### Steg 13 – Skapa tester och kvalitativa evals

**Status:** Klar

**Mål:** Verifiera både strukturell korrekthet och kvaliteten i rekommendationerna.

Testfallen ska omfatta bland annat:

- ofullständigt problem som kräver en avgörande följdfråga,
- enkelt behov där GPT:n ska undvika överdesign,
- behov som kräver flera samverkande mönster,
- konflikt mellan konsistens, tillgänglighet och latens,
- jämförelse mellan modulär monolit och microservices,
- jämförelse mellan saga-orkestrering och koreografi,
- olämpligt önskemål om event sourcing eller CQRS,
- resiliensfall där retries riskerar att förvärra felet,
- produktberoende fråga där aktuell källa behövs,
- ADR-underlag med tydligt redovisade antaganden.

**Klart när:**

- kritiska kärnförmågor har test- eller evaltäckning,
- acceptanskriterierna bedömer resonemang och inte bara förekomst av nyckelord,
- reproducerbara fel kan läggas till som regressionstest.

### Steg 14 – Bygg och validera båda distributionerna

**Status:** Klar

**Mål:** Skapa fungerande Chat ZIP och Custom GPT från samma canonical projekt.

**Klart när:**

- båda distributionerna kan byggas reproducerbart,
- Chat ZIP endast innehåller runtime-material,
- Custom GPT håller sig inom instruktion- och Knowledge-gränserna,
- deklarerade capabilities har jämförts per runtime,
- distributionsvalideringen passerar utan blockerande fel.

### Steg 15 – Slutgranskning och release candidate

**Status:** Klar

**Mål:** Göra projektet redo för praktisk användarprovning.

**Klart när:**

- lint, tester, evals, build och distributionsvalidering passerar,
- final project hygiene är godkänd,
- release readiness är `ready` eller motiverat `ready_with_warnings`,
- Project ZIP, Chat ZIP och Custom GPT ZIP byggs med RC-version,
- checksummor och delivery manifest skapas.

### Steg 16 – Stabil version 1.0.0

**Status:** Klar

**Mål:** Införa återkoppling från RC och skapa första stabila releasen.

**Klart när:**

- identifierade RC-brister är åtgärdade eller uttryckligen accepterade,
- alla blockerande kvalitetsgrindar passerar,
- slutliga distributioner och projekt-ZIP är byggda,
- GitHub Release kan använda taggen som versionskälla,
- projektet övergår till förvaltningsläge.

## 7. Övergripande kvalitetskriterier

Projektet är framgångsrikt när GPT:n:

- kopplar rekommendationer till uttryckliga krav och begränsningar,
- kan säga att ett efterfrågat mönster inte är motiverat,
- beskriver verkliga nackdelar och inte enbart fördelar,
- anger när ett alternativ blir bättre,
- undviker onödigt teknik- och leverantörsberoende,
- hanterar kombinationer utan att blanda ihop mönstrens ansvar,
- redovisar antaganden och osäkerheter,
- producerar begripligt beslutsunderlag för både tekniska och mindre tekniska läsare.

## 8. Risker att bevaka

- **För stor ämnesbredd:** hanteras genom tydlig avgränsning och konsekvent taxonomi.
- **Ytliga katalogsvar:** hanteras genom den obligatoriska analys- och rekommendationsmetoden.
- **Överdesign:** hanteras genom evalfall där den enklaste tillräckliga lösningen ska föredras.
- **Mönster som behandlas isolerat:** hanteras genom relationer, kombinationer och konfliktanalys.
- **Föråldrad produktinformation:** hanteras genom att skilja stabil mönsterkunskap från aktuella produktfakta.
- **Falsk säkerhet:** hanteras genom tydliga antaganden, osäkerheter och frågor som återstår före beslut.

## 9. Närmast rekommenderade steg

Samtliga planerade steg är genomförda. Projektet är i förvaltningsläge efter stabil version 1.0.0.


---

### Steg 17 – GPT Byggaren 1.5-kontrakt och guided modellrobusthet

**Mål:** Migrera Arkitekturmönsterguidens canonical kontrakt till GPT Byggaren 1.5.0 utan att ändra domänmetoden.

**Leveranser:**
- capability-, artifact-, workspace/state- och tool-kontrakt,
- guided modellrobust profil,
- kort operativ kärna,
- fyra modellkompatibilitetsscenarier,
- explicit bedömning av fem registrerade runtimes.

**Klart när:**
- befintlig CI är grön,
- Custom GPT håller sig under 8 000 tecken,
- befintliga kvalitativa evals och distributionsvalideringar inte regresserar.

### Steg 18 – Anpassa distributioner och bygg Claude Projects

**Mål:** Låta Chat, Custom GPT och Claude Projects härledas från samma 1.5-kontrakt.

**Klart när:**
- alla tre aktiva distributioner bär samma kritiska kärnbeteende,
- runtime-kontrakt finns i aktiva distributioner,
- Claude Projects innehåller Project Instructions, Knowledge och kompatibilitetsbeskrivning.

### Steg 19 – Generaliserad runtime parity och release readiness

**Mål:** Utöka parity/readiness till fem registrerade peer runtimes.

**Klart när:**
- behavior, capability, artifact, workspace_state och tool jämförs,
- Chat, Custom GPT och Claude Projects verifieras som aktiva,
- OpenCode och OpenAI Plugin har explicit reducerad/inaktiv status,
- release-readiness blockerar runtime- eller artefaktdrift.

### Steg 20 – Slutvalidera migreringen och releasekedjan

**Mål:** Verifiera full regression, CI/release-paritet, releaseartefakter och dokumentation.

**Klart när:**
- samtliga aktiva distributioner och kvalitetsgrindar passerar,
- dokumentationen beskriver 1.5-arkitekturen,
- projektet är redo att mergeas och releasas.
