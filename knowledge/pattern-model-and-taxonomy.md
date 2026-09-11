# Mönstermodell och taxonomi

## Vad som räknas som ett mönster

Ett arkitekturmönster är en återanvändbar lösningsidé för ett återkommande problem i en viss kontext. Det är inte en färdig arkitektur, produkt eller universell bästa praxis. Samma lösning kan vara ett mönster på en nivå och en implementationsteknik på en annan.

## Gemensam modell

Varje mönsterbeskrivning bör innehålla följande fält när de är relevanta:

| Fält | Innebörd |
| --- | --- |
| Namn | Rekommenderat namn och vedertagna alternativa namn |
| Kategori | Primär plats i taxonomin |
| Problem | Det återkommande problem som ska lösas |
| Kontext | Miljö och förutsättningar där problemet uppstår |
| Krafter | Motstridiga kvalitetskrav och begränsningar |
| Lösning | Mönstrets grundidé och huvudkomponenter |
| Passar när | Observerbara valsignaler |
| Undvik när | Kontraindikationer och enklare alternativ |
| Fördelar | Förbättringar som kan förväntas i rätt kontext |
| Nackdelar | Kostnader, komplexitet och försämrade egenskaper |
| Felmoder | Vanliga sätt som implementation eller användning misslyckas |
| Förutsättningar | Kompetens, organisation, drift och teknik som krävs |
| Alternativ | Mönster som löser samma problem med annan avvägning |
| Kompletterar | Mönster som löser angränsande delproblem |
| Antimönster | När namnet används men avsikten inte uppfylls |
| Verifiering | Mätning, experiment eller analys före beslut |
| Källläge | Stabil kunskap eller uppgift som behöver aktuell källa |

Alla fält behöver inte återges i varje användarsvar. Modellen säkerställer att viktiga avvägningar finns tillgängliga.

## Taxonomi

### A. Applikations- och tjänstestruktur

Mönster för ansvarsfördelning, beroenderiktning, modulgränser och självständig leverans.

- Layered architecture
- Hexagonal architecture / ports and adapters
- Clean architecture
- Modular monolith
- Microservices
- Service-based architecture
- Microkernel / plugin architecture
- Vertical slice architecture

### B. Integration och meddelanden

Mönster för kommunikation, kontrakt, koppling, asynkronitet och migration mellan system.

- Request/reply och API-baserad integration
- Messaging och publish/subscribe
- Event notification
- Event-carried state transfer
- Competing consumers
- Message router, filter och translator
- Anti-corruption layer
- Strangler fig
- API gateway
- Backend for frontend

### C. Data och distribuerade arbetsflöden

Mönster för dataägande, konsistens, historik, transaktioner och härledda läsmodeller.

- Shared database
- Database per service
- Saga: orkestrering och koreografi
- Transactional outbox
- Idempotent consumer / inbox
- CQRS
- Event sourcing
- Materialized view
- Change data capture
- Cache-aside

### D. Resiliens och belastningsskydd

Mönster för att begränsa, absorbera och återhämta sig från fel.

- Timeout
- Retry med backoff och jitter
- Circuit breaker
- Bulkhead
- Rate limiting
- Load shedding
- Queue-based load leveling
- Health endpoint

### E. Skalning och cloud-native struktur

Mönster för horisontell skalning, tillstånd, isolering och distribution.

- Stateless service och externalized state
- Autoscaling
- Leader election
- Sharding / partitioning
- Sidecar
- Deployment stamps / cells

## Relationstyper

- **Alternativ till:** löser huvudsakligen samma problem med annan avvägning.
- **Kompletterar:** löser ett annat delproblem och kan kombineras.
- **Förutsätter:** kräver ett annat beteende eller en annan mekanism för att vara säkert.
- **Motverkar:** kan ge negativa interaktioner eller konkurrerande egenskaper.
- **Övergång till:** kan användas som migrationsväg mot en annan struktur.

## Regler för jämförelser

Jämför inte mönster på olika nivåer som om de vore direkta alternativ. Exempelvis är transactional outbox inte ett alternativ till saga; outbox kan stödja meddelandepubliceringen i en saga. CQRS förutsätter inte event sourcing och event sourcing förutsätter inte microservices.

## Namn och variationer

Använd det etablerade engelska namnet när svensk översättning är tvetydig, men förklara innebörden på svenska. Om olika källor använder samma namn för olika lösningar ska den avsedda varianten anges.

## Aktualitet

Mönstrens grundidéer är normalt stabila. Produktspecifika gränser, tjänstenamn, garantier, priser och versionsbeteenden ska verifieras mot aktuella primärkällor.
