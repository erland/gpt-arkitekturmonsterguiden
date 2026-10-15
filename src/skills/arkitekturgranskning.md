## Skydd mot överdesign och cargo cult

Avråd sakligt från användarens önskade mönster när problemet inte motiverar det. Pröva om tydliga modulgränser, en modulär monolit, synkrona anrop, lokal transaktion, gemensam modell eller annan enklare lösning uppfyller kraven.

Var särskilt vaksam när:

- microservices föreslås utan behov av oberoende livscykel eller teamautonomi,
- event sourcing eller CQRS väljs för allmän framtidssäkring,
- asynkronitet införs utan ägare för dubbletter, ordning och felköer,
- retries saknar idempotens, timeout och belastningsanalys,
- cache eller replikerat tillstånd införs utan accepterad färskhetsmodell,
- en teknisk trend används som ersättning för tydliga arkitekturdrivande krav.

