# Instruktionsarkitektur

## Lager

1. `src/instructions/system.md` är canonical källa för identitet, kärnworkflow, prioriteringsregler, svarsbeteende och avgränsningar.
2. `src/runtime-policy/` innehåller korta kompletterande runtime-regler som inte får krävas för att förstå kärnflödet.
3. `knowledge/` innehåller mönsterbeskrivningar, taxonomi och beslutsstöd men inte dold beteendestyrning.
4. `runtime/` innehåller valfria schemas och mallar för strukturerade leveranser.

## Hoppbudget

Kärnflödet har noll obligatoriska filhopp. Modellen får använda Knowledge för djup och precision men ska kunna genomföra en grundläggande analys från canonical instruktionen.

## Distribution

Chat ZIP får full Knowledge och kompletterande runtime-material. Custom GPT får samma Knowledge så länge fil- och instruktionsgränserna hålls. Kritiska capabilities verifieras efter kompilerad instruktion.
