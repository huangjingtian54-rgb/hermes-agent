"""
Configuration module for Hermes Agent.

Manages all runtime configuration including models, tools, memory,
skills, and agent settings.
"""

import yaml
import os
from pathlib import Path
from typing import Dict, Any, Optional, List


class Config:
    """Hermes Agent configuration manager."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize configuration from file or default."""
        self.config_path = config_path or Path.home() / ".hermes" / "config.yaml"
        self._config: Dict[str, Any] = {}
        self._load()
    
    def _load(self) -> None:
        """Load configuration from file."""
        if not self.config_path.exists():
            self._config = self._default_config()
            return
        
        with open(self.config_path, 'r') as f:
            self._config = yaml.safe_load(f)
    
    def _default_config(self) -> Dict[str, Any]:
        """Return default configuration."""
        return {
            "model": {
                "default": "Qwen3.6-35B-A3B-4bit",
                "max_tokens": 32768,
                "provider": "omlx",
                "base_url": "http://127.0.0.1:8000/v1",
                "context_length": 65274,
            },
            "providers": {
                "omlx": {
                    "api_key": os.getenv("GITHUB_TOKEN") or "1234",
                    "api_mode": "chat_completions",
                    "base_url": "http://127.0.0.1:8000/v1",
                    "default_model": "Qwen3.6-35B-A3B-4bit",
                    "name": "oMLX",
                }
            },
            "toolsets": ["hermes-cli", "web"],
            "agent": {
                "max_turns": 60,
                "service_tier": "normal",
                "reasoning_effort": "none",
                "verbose": False,
                "personalities": {},
            },
            "terminal": {
                "backend": "local",
                "cwd": ".",
                "timeout": 180,
                "home_mode": "auto",
                "container_cpu": 1,
                "container_memory": 5120,
                "container_disk": 51200,
                "container_persistent": True,
            },
            "browser": {
                "inactivity_timeout": 120,
            },
            "file": {
                "read_max_chars": 5000,
            },
            "tool_output": {
                "max_lines": 3000,
                "max_line_length": 3000,
            },
            "tool_loop_guardrails": {
                "warnings_enabled": True,
                "hard_stop_enabled": False,
                "warn_after": {
                    "exact_failure": 2,
                    "same_tool_failure": 3,
                    "idempotent_no_progress": 2,
                },
                "hard_stop_after": {
                    "exact_failure": 5,
                    "same_tool_failure": 8,
                    "idempotent_no_progress": 5,
                },
                "protect_first_n": 3,
                "protect_last_n": 20,
                "target_ratio": 0.3,
                "threshold": 0.6,
            },
            "compression": {
                "enabled": True,
                "threshold": 0.55,
                "target_ratio": 0.3,
                "protect_last_n": 20,
                "protect_first_n": 4,
            },
            "prompt_caching": {
                "cache_ttl": "5m",
            },
            "display": {
                "compact": False,
                "busy_input_mode": "interrupt",
                "bell_on_complete": False,
                "show_reasoning": False,
                "streaming": True,
                "language": "en",
            },
            "memory": {
                "enabled": True,
                "max_chars": 2500,
                "user_max_chars": 800,
                "flush_min_turns": 6,
            },
            "delegation": {
                "max_iterations": 30,
                "max_spawn_depth": 1,
            },
            "security": {
                "redact_secrets": True,
            },
        }
    
    @property
    def model(self) -> Dict[str, Any]:
        """Get model configuration."""
        return self._config.get("model", {})
    
    @property
    def providers(self) -> Dict[str, Any]:
        """Get providers configuration."""
        return self._config.get("providers", {})
    
    @property
    def toolsets(self) -> List[str]:
        """Get enabled toolsets."""
        return self._config.get("toolsets", [])
    
    @property
    def agent(self) -> Dict[str, Any]:
        """Get agent configuration."""
        return self._config.get("agent", {})
    
    @property
    def terminal(self) -> Dict[str, Any]:
        """Get terminal configuration."""
        return self._config.get("terminal", {})
    
    @property
    def browser(self) -> Dict[str, Any]:
        """Get browser configuration."""
        return self._config.get("browser", {})
    
    @property
    def display(self) -> Dict[str, Any]:
        """Get display configuration."""
        return self._config.get("display", {})
    
    @property
    def memory(self) -> Dict[str, Any]:
        """Get memory configuration."""
        return self._config.get("memory", {})
    
    @property
    def tool_loop_guardrails(self) -> Dict[str, Any]:
        """Get tool loop guardrails configuration."""
        return self._config.get("tool_loop_guardrails", {})
    
    def save(self) -> None:
        """Save configuration to file."""
        Path(self.config_path).parent.mkdir(parents=True, exist_ok=True)
        with open(self.config_path, 'w') as f:
            yaml.dump(self._config, f, default_flow_style=False)
    
    def update(self, **kwargs) -> None:
        """Update configuration with new values."""
        for key, value in kwargs.items():
            if key in self._config:
                self._config[key].update(value)
            else:
                self._config[key] = value
        self.save()
