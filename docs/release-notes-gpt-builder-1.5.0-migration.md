# Arkitekturmönsterguiden – migrering till GPT Byggaren 1.5.0

Migreringen bevarar domänbeteendet men moderniserar runtime-, capability- och releasekontrakten.

- guided modellrobusthet utan onödigt persistent state
- plattformsneutrala capability-, artifact-, workspace_state- och tool-kontrakt
- ChatGPT Chat, ChatGPT Custom och Claude Projects som aktiva peer runtimes
- OpenCode och OpenAI Plugin explicit reducerade/inaktiva
- runtime-kontrakt i alla aktiva distributioner
- fem-runtime parity som blockerande gate
- release-readiness för tre aktiva runtimeartefakter
- CI/release workflow parity
- oförändrade kärnregler för enklaste tillräckliga lösning, avvägningar, antaganden och osäkerhet
