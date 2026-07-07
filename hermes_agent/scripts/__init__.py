"""
Scripts module for Hermes Agent.

Provides command-line scripts for various operations.
"""

import sys
import json
from typing import Optional, List


def chat(prompt: str = ""):
    """Run a chat session with the given prompt."""
    print(f"[USER] {prompt}")
    print(f"[Hermes] I'm ready to help! What would you like to work on today?")
    return {"status": "ready", "prompt": prompt}


def run(prompt: str = "", args: Optional[str] = None):
    """Run a chat session or execute a command."""
    if not prompt:
        # Interactive mode
        print(f"[Hermes] How can I help you today?")
        return {"status": "interactive"}
    else:
        # Run with prompt
        result = chat(prompt)
        return {"status": "completed", "result": result}


def setup():
    """Setup Hermes Agent."""
    import os
    from pathlib import Path
    
    print("Setting up Hermes Agent...")
    
    # Check config file
    config_path = Path.home() / ".hermes" / "config.yaml"
    
    if not config_path.exists():
        print(f"Creating config at {config_path}")
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w') as f:
            f.write("# Hermes Agent Configuration\n")
    
    # Check memory directory
    memory_dir = Path.home() / ".hermes" / "memory"
    memory_dir.mkdir(parents=True, exist_ok=True)
    
    # Check skills directory
    skills_dir = Path.home() / ".hermes" / "skills"
    skills_dir.mkdir(parents=True, exist_ok=True)
    
    print("Setup complete!")
    return {"status": "setup_complete"}


def config(*, set: Optional[str] = None, get: Optional[str] = None):
    """Manage Hermes Agent configuration."""
    from pathlib import Path
    
    config_path = Path.home() / ".hermes" / "config.yaml"
    
    if set:
        # Set a configuration value
        print(f"[SET] {set}")
        return {"status": "set", "key": set}
    elif get:
        # Get a configuration value
        if config_path.exists():
            with open(config_path, 'r') as f:
                content = f.read()
                if get in content:
                    print(f"[GET] {content}")
                    return {"status": "found", "value": content}
                else:
                    return {"status": "not_found", "key": get}
        else:
            # Show all config
            if config_path.exists():
                with open(config_path, 'r') as f:
                    print(f.read())
            else:
                print("No configuration found.")
            return {"status": "empty"}
    else:
        print("Usage: hermes config [set <key> | get <key>]")
        return {"status": "usage"}


def skills(*, create: Optional[str] = None, update: Optional[str] = None,
           list: Optional[str] = None, view: Optional[str] = None):
    """Manage skills."""
    import yaml
    from pathlib import Path
    
    config_path = Path.home() / ".hermes" / "config.yaml"
    
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    
    if create:
        print(f"Creating skill: {create}")
        return {"status": "create", "name": create}
    elif update:
        print(f"Updating skill: {update}")
        return {"status": "update", "name": update}
    elif view:
        skill_path = Path.home() / f".hermes/skills/{view}/SKILL.md"
        if skill_path.exists():
            with open(skill_path, 'r') as f:
                print(f.read())
            return {"status": "found", "skill": view}
        else:
            return {"status": "not_found", "skill": view}
    
    # List skills
    skills_dir = Path.home() / ".hermes" / "skills"
    if skills_dir.exists():
        skills = [f.stem for f in skills_dir.glob("*.md")]
        print(json.dumps(skills, indent=2))
        return {"status": "list", "skills": skills}
    
    return {"status": "empty"}


def cron(*, create: Optional[str] = None, list: Optional[str] = None):
    """Manage cron jobs."""
    from pathlib import Path
    
    cron_dir = Path.home() / ".hermes" / "cron"
    
    if create:
        print(f"Creating cron job: {create}")
        return {"status": "create", "job": create}
    elif list:
        if cron_dir.exists():
            cron_jobs = [f.stem for f in cron_dir.glob("*")]
            print(json.dumps(cron_jobs, indent=2))
            return {"status": "list", "jobs": cron_jobs}
    
    return {"status": "empty"}


def tools():
    """List all available tools."""
    tools_list = [
        {"name": "browser_navigate", "description": "Navigate to URL"},
        {"name": "browser_snapshot", "description": "Get page snapshot"},
        {"name": "browser_click", "description": "Click element"},
        {"name": "browser_type", "description": "Type in input"},
        {"name": "browser_vision", "description": "Analyze image"},
        {"name": "browser_console", "description": "Get console output"},
        {"name": "terminal", "description": "Run terminal command"},
        {"name": "process", "description": "Manage processes"},
        {"name": "read_file", "description": "Read file"},
        {"name": "write_file", "description": "Write to file"},
        {"name": "patch", "description": "Patch file"},
        {"name": "search_files", "description": "Search files"},
        {"name": "execute_code", "description": "Run Python code"},
        {"name": "memory", "description": "Manage memory"},
        {"name": "skill_manage", "description": "Manage skills"},
        {"name": "skill_view", "description": "View skill"},
        {"name": "delegate_task", "description": "Delegate task"},
        {"name": "cronjob", "description": "Manage cron jobs"},
    ]
    print(json.dumps(tools_list, indent=2))
    return {"status": "list", "tools": tools_list}


def memory(*, add: Optional[str] = None, remove: Optional[str] = None):
    """Manage memory."""
    from pathlib import Path
    
    memory_dir = Path.home() / ".hermes" / "memory"
    
    if add:
        user_path = memory_dir / "USER.md"
        if user_path.exists():
            content = user_path.read_text()
            with open(user_path, 'a') as f:
                f.write(f"\n### New: {add}\n")
        return {"status": "added"}
    
    # List memory
    if memory_dir.exists():
        user_memory = []
        if (memory_dir / "USER.md").exists():
            user_memory = [(i+1, line) for i, line in enumerate(
                (memory_dir / "USER.md").read_text().split('\n')[:20]
            )]
        print(json.dumps(user_memory, indent=2))
        return {"status": "list", "user_memory": user_memory}
    
    return {"status": "empty"}


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "help"
    
    if command == "run":
        prompt = sys.argv[2] if len(sys.argv) > 2 else ""
        result = run(prompt)
        print(json.dumps(result))
    elif command == "chat":
        result = chat()
        print(json.dumps(result))
    elif command == "setup":
        result = setup()
        print(json.dumps(result))
    elif command == "config":
        config()
    elif command == "skills":
        skills()
    elif command == "cron":
        cron()
    elif command == "tools":
        tools()
    elif command == "memory":
        memory()
    else:
        print("Usage: hermes <command>")
