import importlib.util
from pathlib import Path


def test_app_module_imports_without_runtime_config():
    app_path = Path(__file__).resolve().parents[1] / 'app.py'
    spec = importlib.util.spec_from_file_location('agentic_app', app_path)
    module = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # pragma: no cover - regression guard for import-time issues
        raise AssertionError(f'app.py failed to import: {exc}') from exc
