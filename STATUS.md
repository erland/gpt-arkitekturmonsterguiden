# Status

Version 1.0.0 är fortsatt stabil baslinje.

**Migrering till GPT Byggaren 1.5.0 pågår – steg 19.**

## Verifierat i steg 18

- Chat ZIP har explicit 1.5-runtime-kontrakt,
- Custom GPT har explicit 1.5-runtime-kontrakt,
- Claude Projects byggs som aktiv peer-runtime,
- Claude-paketet innehåller Project Instructions, Knowledge och runtime-contract,
- Claude Projects kräver inte `CLAUDE.md` eller andra Claude Code-konventioner,
- alla tre aktiva runtimes bär samma kritiska canonical kärnbeteende,
- CI och release bygger Chat, Custom GPT och Claude Projects,
- full CI-kedja: PASS.

## Nästa rekommenderade steg

**19 – Generaliserad runtime parity och release readiness.**

Behavior, capability, artifact, workspace_state och tool ska jämföras över alla fem registrerade runtimes. Chat, Custom GPT och Claude Projects är aktiva; OpenCode och OpenAI Plugin förblir reducerade/inaktiva.
