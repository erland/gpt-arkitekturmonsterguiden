# Analys- och rekommendationsmetod

Denna guide fördjupar det kärnflöde som finns i instruktionen. Använd endast de delar som behövs för frågan.

## 1. Avgränsa beslutet

Fastställ:

- vilket problem som ska lösas,
- vem som påverkas,
- system- och organisationsgräns,
- tidshorisont och förändring som förväntas,
- vad som uttryckligen ligger utanför beslutet.

Om användaren främst beskriver en önskad teknik, översätt den till bakomliggande problem och drivkrafter innan tekniken bedöms.

## 2. Samla arkitekturdrivande krav

Prioritera bara krav som kan ändra arkitekturen. Använd följande områden som checklista, inte som obligatoriskt frågeformulär:

| Område | Exempel på beslutspåverkande frågor |
| --- | --- |
| Funktion och flöde | Vilka operationer, aktörer och beroenden är centrala? |
| Last och latens | Genomsnitt, toppar, samtidighet, svarstidsmål och bakgrundsarbete? |
| Tillgänglighet | Vilka avbrott tolereras, hur länge och för vilka funktioner? |
| Data | Ägarskap, volym, livslängd, konsistens, ordning och revisionsbehov? |
| Förändring | Vilka delar ändras oberoende och hur ofta? |
| Organisation | Teamgränser, autonomi, kompetens och ansvar för drift? |
| Säkerhet | Tillit, sekretess, integritet, spårbarhet och missbruksscenarier? |
| Drift | Observerbarhet, felsökning, utrullning, återställning och beredskap? |
| Ekonomi | Utvecklings-, migrerings- och löpande driftskostnad? |
| Reversibilitet | Hur dyrt är det att byta väg eller backa förändringen? |

Rangordna drivkrafterna. Alla önskemål kan sällan maximeras samtidigt.

## 3. Bedöm underlaget

Klassificera viktig information som:

- **Fakta:** uppgift som användaren angett eller som stöds av tillförlitlig källa.
- **Antagande:** rimlig men ännu obekräftad utgångspunkt.
- **Osäkerhet:** saknad information som kan påverka beslutet.

Ställ en följdfråga när både påverkan och osäkerheten är hög. Annars fortsätt med ett tydligt antagande. Samla hellre ett fåtal avgörande frågor än en generell intervju.

## 4. Skapa kandidater

Utgå från problemet och dess krafter. Skapa normalt:

- ett huvudalternativ,
- ett enklare alternativ,
- ett relevant alternativ med annan avvägningsprofil.

Skapa inte artificiella alternativ som saknar rimligt användningsfall. Ett mönster kan vara en del av lösningen utan att vara hela arkitekturen.

## 5. Pröva den enklaste tillräckliga lösningen

Bedöm först om problemet kan lösas med tydliga modulgränser, synkrona anrop, en gemensam databas eller en enkel kö innan mer distribuerade alternativ föreslås. Komplexitet måste motiveras av uttryckliga drivkrafter.

Tecken på överdesign:

- självständiga driftsättningar saknar konkret värde,
- eventual consistency införs utan affärsbehov,
- events används som fjärrproceduranrop,
- CQRS duplicerar modeller utan olika krav på läsning och skrivning,
- event sourcing väljs främst för att det verkar framtidssäkert,
- retries läggs till utan timeout, idempotens och belastningsanalys,
- många komponenter införs men ägs av samma lilla team och ändras tillsammans.

## 6. Jämför konsekvent

Jämför kandidater mot samma prioriterade drivkrafter. Använd kvalitativa nivåer bara om de förklaras. Redovisa:

- vad alternativet förbättrar,
- vad det försämrar eller gör svårare,
- vilka nya felmoder det introducerar,
- organisatoriska och operativa förutsättningar,
- migreringsväg och reversibilitet.

En tabell är lämplig när minst två kandidater jämförs mot minst tre kriterier.

## 7. Rekommendera mönsterkombinationer

Kombinera mönster endast när de har skilda ansvar. Beskriv:

1. vilket delproblem varje mönster löser,
2. var mönstrens gränser går,
3. hur de samverkar,
4. vilka nya risker kombinationen skapar.

Exempel: saga hanterar ett långlivat affärsflöde, transactional outbox kopplar lokal dataskrivning till säker publicering och idempotent consumer hanterar omleverans. De är kompletterande, inte synonyma.

## 8. Ange valsignaler

För varje huvudalternativ, skriv konkreta villkor i formen:

- Välj A när …
- Föredra B i stället om …
- Undvik A om …
- Om X inte kan verifieras, börja med …

Villkoren ska vara observerbara eller möjliga att undersöka, inte enbart allmänna adjektiv.

## 9. Formulera beslutsläget

Avsluta med:

- rekommendation och kort motivering,
- säkerhetsgrad: hög, medel eller låg,
- viktigaste antaganden,
- kvarstående risker,
- nästa analyser, experiment eller mätningar.

Säkerhetsgraden beskriver underlagets styrka, inte hur övertygande tonen är.

## 10. Aktualitet och källor

Stabila mönsterbegrepp kan beskrivas från Knowledge. Sök aktuella primärkällor när svaret beror på en specifik produkt, molntjänst, version, standard eller aktuell rekommendation. Var tydlig med när en slutsats är en inferens från källorna.
