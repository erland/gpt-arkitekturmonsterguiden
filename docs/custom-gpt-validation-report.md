# Custom GPT-validering

## Deklarerade gränser

- maximal instruktion: 8 000 tecken
- maximalt antal Knowledge-filer: 20
- instruktionsstrategi: konservativ `compressed`
- Knowledge-strategi: `identical`

## Resultat

- canonical instruktion: 7 010 tecken före deterministisk kompilering
- kärnmarkörer: 4 av 4 bevarade
- Knowledge: 7 av högst 20 filer
- obligatoriska Builder-filer: finns
- förbjudna utvecklingsartefakter: inga i distributionen
- missvisande kärnfunktion: inte identifierad

Resultat: **pass**.
