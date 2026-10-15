# Arkitekturmönsterguiden

GPT-projekt för beslutsorienterade rekommendationer om arkitekturmönster för system, integration, distribuerade lösningar och moln.

Projektet bygger fem likvärdiga runtime-distributioner från samma canonical instruktion:

- Chat ZIP
- ChatGPT Plugin (Skills utan MCP eller separat Engine)
- Claude Project
- Claude Skills
- OpenCode

Custom GPT är avvecklad som distributionsmål; dess äldre konfiguration är bevarad för spårbarhet.

## Lokal validering

```bash
python -m pip install -r requirements-dev.txt
python scripts/run_tests.py
python scripts/validate_instruction_adherence.py --project-root .
python scripts/lint_gpt_project.py --project-root .
python scripts/build_distributions.py --project-root . --version 0.0.0-dev
python scripts/validate_distributions.py --project-root .
```

## Migrering 2026-10-15

Byggmotorn är uppdaterad från GPT Byggaren 1.5.1 till 1.6.25. Domaininstruktion, Knowledge, evals och projektspecifika tester har bevarats. Befintlig GitHub-historik och äldre migrationsrapport följer med. Se `docs/migration-1.6.25.md`.

## Release

GitHub Release-taggen bestämmer versionen. CI och release genererar sex ZIP-arkiv: projekt samt fem runtimes. Verifiering i faktiska värdmiljöer återstår före stabil release.
