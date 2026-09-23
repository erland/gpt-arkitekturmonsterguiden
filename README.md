# Arkitekturmönsterguiden

GPT-projekt för beslutsorienterade rekommendationer om arkitekturmönster för system, integration, distribuerade lösningar och moln.

Projektet bygger tre aktiva peer-distributioner från samma canonical kontrakt:

- Chat ZIP för användning som GPT-kontext i en konversation
- Custom GPT-paket för konfigurering i GPT Builder
- Claude Projects-paket med Project Instructions och Knowledge

## Lokal validering

```bash
python -m pip install -r requirements-dev.txt
python scripts/lint_gpt_project.py --project-root .
python scripts/run_tests.py
python scripts/validate_instruction_adherence.py --project-root .
python scripts/build_distributions.py --project-root . --version 0.0.0-dev
python scripts/validate_distributions.py --project-root .
python scripts/validate_runtime_parity.py
python scripts/validate_release_readiness.py
python scripts/validate_workflow_parity.py
```

## Release

CI körs vid push, pull request och manuell start. En publicerad GitHub Release bygger projekt-, Chat-, Custom GPT- och Claude Projects-artefakter. Release-taggen är versionskälla.
