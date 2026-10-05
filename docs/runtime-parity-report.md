# Runtimeparitetsrapport

## Bedömning

Chat ZIP, Custom GPT, Claude Projects och OpenAI Plugin är aktiva peer runtimes och jämförs mot samma canonical capability-kontrakt.

| Capability | Kritikalitet | Chat ZIP | Custom GPT | OpenAI Plugin |
| --- | --- | --- | --- | --- |
| Behovsanalys | critical | equivalent | equivalent | equivalent |
| Arkitekturdrivande krav | critical | equivalent | equivalent | equivalent |
| Mönsterrekommendation | critical | equivalent | equivalent | equivalent |
| Avvägningar och alternativ | critical | equivalent | equivalent | equivalent |
| Antaganden och osäkerhet | critical | equivalent | equivalent | equivalent |
| Skydd mot överdesign | critical | equivalent | equivalent | equivalent |
| Jämförelse och granskning | important | equivalent | equivalent | equivalent |
| ADR-underlag | important | equivalent | equivalent | equivalent |
| Strukturerad JSON | optional | equivalent | equivalent | equivalent |
| Aktuell produktresearch | important | platform_dependent | platform_dependent | platform_dependent |
| Hantering av uppladdade underlag | important | platform_dependent | platform_dependent | platform_dependent |

## Slutsats

Ingen kritisk capability saknas i de aktiva distributionerna. OpenAI Plugin bär samma canonical kärnbeteende i en skills-first skill och samma mönsterkunskap som references. Aktuell produkt-/standardresearch och hantering av uppladdade filer är `platform_dependent`; pluginen använder explicita fallbacks när hostcapability saknas. Inget persistent state, runtime-script eller MCP-wrapper krävs.
