# Integration och meddelanden

Välj integrationsstil från verksamhetsflöde, koppling, tidskrav och felhantering. En broker eller ett API löser inte automatiskt kontrakts-, ägar- eller konsistensproblem.

## Request/reply och API-baserad integration

**Lösning:** Konsumenten skickar en begäran och väntar på ett svar, ofta via HTTP eller RPC.

- **Välj när:** svaret behövs för att fortsätta, latensen är förutsägbar och beroendet kan vara tillgängligt inom flödets tidsbudget.
- **Fördelar:** enkel mental modell, omedelbar återkoppling och ofta enkel felsökning.
- **Nackdelar/risker:** tids- och tillgänglighetskoppling, kaskadfel och långa beroendekedjor.
- **Välj asynkront när:** arbetet kan slutföras senare, toppar behöver absorberas eller producent och konsument inte bör vara tillgängliga samtidigt.

## Messaging

**Lösning:** Producenten skickar ett beständigt meddelande till en kanal eller kö; en konsument bearbetar det separat.

- **Välj när:** tidsmässig frikoppling, buffring, omleverans eller bakgrundsarbete behövs.
- **Fördelar:** lastutjämning och minskad samtidig tillgänglighetskoppling.
- **Nackdelar/risker:** eventual consistency, dubbletter, ordningsfrågor, svårare spårning och felköer.
- **Förutsätter:** idempotens, observerbarhet, tydligt felansvar och genomtänkta leveransgarantier.

## Publish/subscribe

**Lösning:** En producent publicerar till ett ämne; flera oberoende prenumeranter får var sin kopia.

- **Välj när:** flera konsumenter reagerar självständigt på samma information.
- **Fördelar:** producenten behöver inte känna alla konsumenter; nya reaktioner kan läggas till.
- **Nackdelar/risker:** dold systemomfattning, svår konsekvensanalys och många oberoende felbanor.
- **Välj punkt-till-punkt när:** exakt en arbetare ska utföra uppgiften.

## Event notification

**Lösning:** Ett tunt event meddelar att något har hänt; konsumenten hämtar mer data från ägaren.

- **Välj när:** ägaren ska förbli auktoritativ och händelsen bara triggar en reaktion.
- **Fördelar:** små events och mindre dataduplicering.
- **Nackdelar/risker:** extra anrop, läsbelastning och risk att källans aktuella tillstånd inte motsvarar eventögonblicket.
- **Välj event-carried state transfer när:** konsumenten behöver lokal autonomi eller källan inte bör belastas efter varje event.

## Event-carried state transfer

**Lösning:** Eventet innehåller den information mottagare behöver för att uppdatera en lokal vy.

- **Välj när:** konsumenter ska kunna arbeta utan synkrona återanrop och accepterar replikerat tillstånd.
- **Fördelar:** lägre runtime-koppling och snabba lokala läsningar.
- **Nackdelar/risker:** större kontrakt, duplicerad eller känslig data, korrigering och schemaevolution.
- **Välj notification när:** dataägarskap och färsk hämtning väger tyngre än konsumentautonomi.

## Competing consumers

**Lösning:** Flera instanser konsumerar från samma arbetskö och varje meddelande hanteras av en av dem.

- **Välj när:** oberoende jobb kan parallelliseras och genomströmning behöver skalas.
- **Fördelar:** enkel horisontell arbetarskalning och lastfördelning.
- **Nackdelar/risker:** global ordning försvinner, heta partitioner och samtidighetskonflikter kan uppstå.
- **Välj partitionerad konsumtion när:** ordning måste bevaras per nyckel.

## Message router, filter och translator

**Lösning:** Separata integrationskomponenter dirigerar, väljer och transformerar meddelanden.

- **Välj när:** routing och formatöversättning är verklig integrationslogik som behöver styras och observeras centralt.
- **Fördelar:** producenter och konsumenter slipper känna alla format och vägar.
- **Nackdelar/risker:** integrationslagret kan bli en central verksamhetslogikmotor och flaskhals.
- **Undvik när:** enkel routing kan uttryckas tydligare i producentens kontrakt eller konsumentens adapter.

## Anti-corruption layer

**Lösning:** Ett översättande lager isolerar den lokala domänmodellen från ett externt eller äldre systems begrepp.

- **Välj när:** modellerna skiljer sig semantiskt och den externa modellen annars skulle spridas internt.
- **Fördelar:** skyddar språk, regler och förändringstakt.
- **Nackdelar/risker:** extra mappning och risk att översättningen döljer verkliga informationsförluster.
- **Välj enkel adapter när:** skillnaden främst är protokoll eller format, inte semantik.

## Strangler fig

**Lösning:** Led trafik gradvis till nya funktioner runt ett äldre system tills berörda delar kan avvecklas.

- **Välj när:** big-bang-ersättning är riskfylld och funktioner kan migreras inkrementellt.
- **Fördelar:** begränsad förändringsrisk, tidig nytta och möjlighet att lära.
- **Nackdelar/risker:** långvarig dubbel drift, komplicerad routing och delat dataansvar.
- **Välj annat när:** systemet saknar separerbara gränser eller övergångsarkitekturen blir dyrare än en kontrollerad ersättning.

## API gateway

**Lösning:** En gemensam extern ingång hanterar routing och tvärgående API-frågor.

- **Välj när:** flera bakomliggande tjänster behöver en stabil yta, gemensam autentisering, kvotering eller protokollanpassning.
- **Fördelar:** förenklad klientkontakt och central policytillämpning.
- **Nackdelar/risker:** kritisk beroendepunkt, central flaskhals och risk för verksamhetslogik i gatewayen.
- **Välj direkt API när:** få stabila tjänster och klienter inte motiverar mellanlagret.

## Backend for frontend, BFF

**Lösning:** Varje klienttyp får ett anpassat backendlager som sammanställer data och flöden.

- **Välj när:** web, mobil eller andra kanaler har väsentligt olika behov och förändringstakt.
- **Fördelar:** klientanpassade kontrakt och mindre klientorkestrering.
- **Nackdelar/risker:** duplicering, fler driftsättningar och oklar gräns mellan kanal- och domänlogik.
- **Välj gemensamt API när:** klientbehoven i praktiken är lika.

## Avgörande avvägningar

- Asynkronitet flyttar felhantering; den tar inte bort den.
- ”Exactly once” på affärsnivå kräver vanligtvis idempotens och deduplicering även om infrastrukturen har starka garantier.
- Events ska namnge något som har hänt. Kommandon uttrycker en önskan att något ska ske.
- Ett publicerat event blir ett kontrakt. Planera ägarskap, versionering, sekretess och avveckling.
- Långa synkrona kedjor bör analyseras som en gemensam tillgänglighets- och latensbudget.
