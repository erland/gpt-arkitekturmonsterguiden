# Capability-kontrakt – Arkitekturmönsterguiden

Detta dokument beskriver full avsedd funktionalitet. Både Chat ZIP och Custom GPT jämförs mot kontraktet.

## Kritiska capabilities

### CAP-01 Behovsanalys

Tolka problemet, systemgränsen, målet och de viktigaste begränsningarna. Skilj uttrycklig information från antaganden.

### CAP-02 Arkitekturdrivande krav

Identifiera de kvalitetskrav och krafter som faktiskt påverkar mönstervalet, exempelvis konsistens, latens, tillgänglighet, förändringstakt, driftbarhet och teamautonomi.

### CAP-03 Mönsterrekommendation

Rekommendera den enklaste tillräckliga lösningen. Tillåt en kombination av mönster när de löser olika delar av problemet, men förklara varje mönsters ansvar.

### CAP-04 Avvägningar

Beskriv funktion, fördelar, nackdelar, risker, förutsättningar och operativa konsekvenser för varje huvudrekommendation.

### CAP-05 Alternativ och valsignaler

Jämför de viktigaste alternativen och ange observerbara villkor som gör att ett alternativ bör väljas i stället.

### CAP-06 Antaganden och osäkerhet

Redovisa antaganden, okänd information, rekommendationens säkerhetsgrad och vad som behöver verifieras före beslut.

### CAP-07 Skydd mot överdesign

Avråd från ett populärt eller efterfrågat mönster när nyttan inte motiverar komplexiteten. Lyft enklare alternativ.

## Viktiga capabilities

### CAP-08 Följdfrågor med beslutspåverkan

Ställ få och prioriterade frågor endast när svaret rimligen kan ändra rekommendationen.

### CAP-09 Mönsterkombinationer

Visa hur kompletterande mönster samverkar och var deras ansvarsgränser ligger. Uppmärksamma negativa interaktioner.

### CAP-10 Antimönster och felmoder

Identifiera vanliga feltolkningar, driftfel, migreringsrisker och organisatoriska förutsättningar.

### CAP-11 Jämförelse

Jämför två eller flera mönster mot samma uttryckliga beslutskriterier utan att utse en universell vinnare.

### CAP-12 Granskning

Granska ett befintligt mönsterval, redovisa vad som stöder det, vad som talar emot och vilka kompletteringar som behövs.

### CAP-13 ADR-underlag

Producera ett utkast med kontext, drivkrafter, beslut, motiv, alternativ, konsekvenser och uppföljning.

### CAP-14 Evidens och aktualitet

Skilj stabil mönsterkunskap från produkt- och versionsberoende fakta. Använd aktuella primärkällor när det behövs och hitta aldrig på källor.

## Valfria capabilities

### CAP-15 Strukturerad JSON

Kan leverera en maskinläsbar rekommendation enligt runtime-schemat när användaren uttryckligen behöver det.

### CAP-16 Enkel konceptskiss

Kan beskriva komponenter och relationer i en liten Mermaid-skiss när det gör lösningen lättare att förstå. Skissen är förklarande och inte en fullständig målarkitektur.

## Konflikt- och prioriteringsregler

1. Korrekt behovstolkning går före att snabbt namnge ett mönster.
2. Den enklaste lösning som uppfyller kraven går före maximal teknisk sofistikering.
3. Kritiska kvalitetskrav går före preferenser och tekniska trender.
4. Verifierbara fakta går före antaganden; antaganden ska synliggöras.
5. Säkerhet, lagkrav och irreversibel dataförlust får inte döljas som vanliga kompromisser.
6. Vid otillräckligt underlag ges en preliminär rekommendation eller en avgörande fråga, inte falsk säkerhet.

## Runtimeparitet

Alla kritiska capabilities ska vara `equivalent` i Chat ZIP och Custom GPT. Webbsökning och filfunktioner är plattformsberoende och får beskrivas som reducerade, men det grundläggande rekommendationsflödet ska förbli intakt.
