# Projekt – Arkitekturmönsterguiden

## Syfte

Hjälpa användaren att analysera ett arkitekturproblem, identifiera arkitekturdrivande krav och välja ett eller flera lämpliga mönster med öppet redovisade avvägningar.

## Omfattning

Första versionen täcker applikations- och tjänstearkitektur, integration och meddelanden, data och distribuerade transaktioner samt resiliens, skalning och cloud-native-mönster.

## Målgrupp

IT-, lösnings- och systemarkitekter, seniora utvecklare och tekniska ledare.

## Distribution

Chat ZIP, Custom GPT, Claude Projects och OpenAI Plugin byggs från samma canonical instruktion och Knowledge-bas.


## GPT Byggaren 1.5-arkitektur

Projektet är guided och kräver inte persistent state för kärnuppgiften.

Aktiva peer runtimes:
- ChatGPT Chat
- ChatGPT Custom
- Claude Projects
- OpenAI Plugin

Bedömd men inaktiv:
- OpenCode

De aktiva distributionerna bär samma plattformsneutrala capability-, artifact-, workspace_state- och tool-kontrakt. Claude Projects använder Project Instructions och Knowledge utan Claude Code-specifika konventioner. OpenAI Plugin använder en skills-first-adapter med Knowledge som references och ADR-mallen som asset; inga runtime-skript eller MCP-wrapper krävs.
