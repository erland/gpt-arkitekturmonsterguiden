import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(relative):
    return yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))


def test_project_contract_and_paths_exist():
    cfg = load_yaml("gpt-project.yaml")
    assert cfg["project"]["id"] == "arkitekturmonsterguiden"
    required = [
        "README.md", "PROJECT.md", "STATUS.md", "project-status.yaml",
        "docs/development-plan.md", cfg["instructions"]["canonical"],
        cfg["knowledge_architecture"]["canonical_root"],
    ]
    for relative in required:
        assert (ROOT / relative).exists(), relative


def test_canonical_instruction_preserves_core_contract_and_limit():
    cfg = load_yaml("gpt-project.yaml")
    text = (ROOT / cfg["instructions"]["canonical"]).read_text(encoding="utf-8")
    for marker in cfg["instructions"]["core_contract"]["required_markers"]:
        assert marker in text
    assert len(text) <= cfg["runtime"]["custom_gpt"]["instruction"]["max_characters"]
    assert cfg["instructions"]["core_contract"]["required_runtime_dependencies"] == []


def test_knowledge_package_fits_custom_gpt_limit():
    cfg = load_yaml("gpt-project.yaml")
    root = ROOT / cfg["knowledge_architecture"]["canonical_root"]
    files = [p for p in root.rglob("*") if p.is_file() and p.name != "KNOWLEDGE.md"]
    assert len(files) <= cfg["runtime"]["custom_gpt"]["knowledge"]["max_files"]


def test_catalogs_cover_planned_patterns_and_choice_signals():
    expected = {
        "knowledge/application-and-services.md": ["Modular monolith", "Microservices", "Hexagonal architecture"],
        "knowledge/integration-and-messaging.md": ["Publish/subscribe", "Anti-corruption layer", "Strangler fig"],
        "knowledge/data-and-transactions.md": ["Saga", "Transactional outbox", "CQRS", "Event sourcing"],
        "knowledge/resilience-scaling-cloud.md": ["Retry", "Circuit breaker", "Bulkhead", "Autoscaling"],
    }
    for relative, terms in expected.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for term in terms:
            assert term.lower() in text.lower(), f"{term} missing in {relative}"
        assert "Välj" in text
        assert "risk" in text.lower()


def test_runtime_json_schemas_are_valid():
    for path in (ROOT / "runtime" / "schemas").glob("*.json"):
        schema = json.loads(path.read_text(encoding="utf-8"))
        assert schema.get("type") == "object"
        assert isinstance(schema.get("properties"), dict)


def test_all_evals_conform_to_schema():
    json.loads((ROOT / "schemas" / "eval-case.schema.json").read_text(encoding="utf-8"))
    paths = list((ROOT / "evals" / "instruction-adherence").glob("*.yaml"))
    paths += list((ROOT / "evals" / "domain").glob("*.yaml"))
    assert len(paths) >= 12
    ids = set()
    for path in paths:
        case = yaml.safe_load(path.read_text(encoding="utf-8"))
        for key in ["id", "title", "criticality", "input", "expected"]:
            assert key in case, f"{key} missing in {path}"
        assert case["criticality"] in {"critical", "important", "optional"}
        assert case["id"] not in ids
        ids.add(case["id"])


def test_distribution_workflows_share_local_toolchain():
    ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    release = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
    for command in ["lint_gpt_project.py", "run_tests.py", "build_distributions.py", "validate_distributions.py"]:
        assert command in ci
        assert command in release
    assert "github.event.release.tag_name" in release
