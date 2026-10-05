# Arkitekturmönsterguiden – OpenAI Plugin enligt GPT Byggaren 1.5.1

OpenAI Plugin aktiveras som skills-first peer-runtime utan att ändra projektets domänbeteende.

- canonical instruktion ligger i huvudskillen och är fortsatt auktoritativ
- Knowledge paketeras som skill references
- runtime/templates/adr.md paketeras som asset
- aktuell produkt-, standard- och versionsresearch använder hostens webbförmåga när den behövs
- filanalys används bara när hosten faktiskt ger åtkomst till uppladdat material
- inget persistent state krävs
- inga runtime-skript eller custom tools paketeras
- ingen MCP-wrapper genereras
- plugin-ZIP ingår i checksummor, delivery manifest, runtime parity, release readiness och CI/release workflow parity
