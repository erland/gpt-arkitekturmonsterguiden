# Migrering till GPT Byggaren 1.6.25

Datum: 2026-10-15. Ursprung: `gpt-arkitekturmonsterguiden-main.zip`.

## Utfört

- Säker kopiemigrering med bevarad ursprunglig canonical instruktion, Knowledge och evals.
- Custom GPT avvecklad som byggmål.
- Fem runtime-mål konfigurerade; Plugin-skill byggd från canonical instruktion.
- Kanonisk byggmotor installerad och separata Claude Skills-/OpenCode-mål tillagda.
- CI och releaseworkflow ändrade till de fem runtime-målen.
- Legacy scripts och äldre dokumentation kvar för jämförelse och historik.

## Verifierat

- 10 projekttester passerar.
- 4 instruction-adherence-fall passerar.
- Alla sex leveransarkiv byggs och distributionsvalidering passerar.

## Kvarvarande granskning

- Bekräfta semantisk runtimeparitet i verkliga värdmiljöer, särskilt Plugin och OpenCode.
- Utför GitHub Actions i repositoryt efter att migrerade källor lagts in.
- Granska äldre release- och paritetsdokument som avser version 1.5.1. Historiska filer ändras inte retroaktivt.
- Kör releasekandidatgranskning före stabil release. Äldre migrationsrapport är inventeringsunderlag, inte bevis på färdig host-verifiering.
