# Status

Version 1.0.0 är fortsatt stabil baslinje.

**Migrering till GPT Byggaren 1.5.0 pågår – steg 20.**

## Verifierat i steg 19

- runtime parity omfattar alla fem registrerade runtimes,
- paritetskategorier: behavior, capability, artifact, workspace_state och tool,
- ChatGPT Chat, ChatGPT Custom och Claude Projects är aktiva,
- OpenCode och OpenAI Plugin är explicit reducerade/inaktiva,
- aktiva runtime-kontrakt verifieras mot samma plattformsneutrala kontrakt,
- canonical kärnmarkörer verifieras i alla tre aktiva runtimes,
- release-readiness verifierar delivery manifest, checksummor och ZIP-integritet,
- parity/readiness är blockerande i både CI och release,
- full CI-kedja: PASS.

## Nästa rekommenderade steg

**20 – Slutvalidera migreringen och releasekedjan.**

Kontrollera full regression, CI/release-paritet, releaseartefakter och dokumentation innan migreringen markeras klar.
