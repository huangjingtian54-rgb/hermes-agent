"""Smoke tests for the Hermes Agent CLI and library."""

from pathlib import Path

from hermes_agent import Agent, Config
from hermes_agent.cli import main


def test_package_imports():
    import hermes_agent

    assert hermes_agent.__version__ == "0.18.0"


def test_agent_run():
    result = Agent(max_turns=1).run("ping")
    assert result.success is True
    assert result.summary == "Agent completed after 1 turns"


def test_config_loads_string_path():
    config_path = Path(__file__).resolve().parents[1] / ".hermes" / "config.yaml"
    config = Config(str(config_path))
    assert config.model["default"] == "Qwen3.6-35B-A3B-4bit"
    assert "hermes-cli" in config.toolsets


def test_config_empty_file_uses_defaults(tmp_path):
    config_path = tmp_path / "config.yaml"
    config_path.write_text("# Hermes Agent Configuration\n")
    config = Config(str(config_path))
    assert config.model["provider"] == "omlx"
    assert config.agent["max_turns"] == 60


def test_cli_version(capsys):
    assert main(["--version"]) == 0
    assert capsys.readouterr().out.strip() == "0.18.0"


def test_cli_tools(capsys):
    assert main(["tools"]) == 0
    assert "browser_navigate" in capsys.readouterr().out


def test_cli_run(capsys):
    assert main(["run", "List the tools you can use"]) == 0
    output = capsys.readouterr().out
    assert "List the tools you can use" in output
    assert '"status": "completed"' in output


def test_cli_setup(capsys, monkeypatch, tmp_path):
    home = tmp_path / "home"
    home.mkdir()
    monkeypatch.setattr(Path, "home", lambda: home)
    assert main(["setup"]) == 0
    assert (home / ".hermes" / "config.yaml").is_file()
    assert (home / ".hermes" / "memory").is_dir()
    assert (home / ".hermes" / "skills").is_dir()
    assert "setup_complete" in capsys.readouterr().out
