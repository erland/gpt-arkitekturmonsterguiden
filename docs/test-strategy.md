# Test- och evalstrategi

## Deterministiska tester

Pytest verifierar projektkontrakt, paths, kärnmarkörer, instruktionsgräns, Knowledge-filgräns, katalogtäckning, JSON Schemas, evalstruktur och CI/release-paritet.

## Instruktionsefterlevnad

Fyra kritiska eller viktiga evalfall verifierar att kärnflödet finns i instruktionen, fungerar utan obligatorisk Knowledge-hämtning och behålls över flera turer.

## Domänevals

Kvalitativa evalfall anger nödvändiga och förbjudna egenskaper i rekommendationer. De är avsedda för modellbaserad bedömning i en miljö som kan köra GPT:n. Kritiska evalfel blockerar release; viktiga fel kräver bedömning.

Varje reproducerbart beteendefel ska få ett regressionstest eller evalfall.
