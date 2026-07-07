# Hermes Agent Skill

Helper skill for interacting with the Hermes Agent system.

## Use This Skill When

You need to:
- Configure or setup Hermes Agent
- Run a chat session with the agent
- Manage tools, skills, memory, or cron jobs
- Use background processes or delegate tasks
- Generate documentation or analyze code

## Hermes Agent Overview

**Hermes Agent** is an intelligent AI agent powered by Nous Research, designed for:
- **Multi-modal capabilities**: text, code, images, audio, vision
- **Persistent memory**: cross-session context retention
- **Background processes**: intelligent task execution in background
- **Tool registry**: 20+ tools including browser, terminal, file, API
- **Skill system**: reusable skills for common workflows
- **Conversation memory**: auto-pruning and compression

## Quick Start

```bash
# Check Hermes is installed
hermes --version

# Start a chat session
hermes -s "Your question here"

# Interactive mode
hermes
```

## Commands

### Run a Chat Session

```bash
hermes -s "Your prompt" -m "model_name" -p "provider"
```

Options:
- `-s, --prompt`: The prompt to send to the agent
- `-m, --model`: Model name (default: Qwen3.6-35B-A3B-4bit)
- `-p, --provider`: Provider name (default: omlx)
- `--verbose`: Enable verbose output
- `--max-turns`: Maximum conversation turns (default: 60)

### Interactive Mode

```bash
hermes
```

Then type your prompt and press Enter.

### Setup

```bash
hermes setup
```

Creates/updates configuration files in `~/.hermes/`.

### Configuration

```bash
# Set a config value
hermes config set key=value

# Get a config value
hermes config get key

# View all config
hermes config
```

### Skills

```bash
# List all skills
hermes skills list

# View a skill
hermes skills view <skill_name>

# Create a skill
hermes skills create <name> --category <category> --content "<content>"

# Update a skill
hermes skills update <name> --old-text --new-text

# Delete a skill
hermes skills delete <name>
```

### Memory

```bash
# Add to memory
hermes memory add --target <user|memory> --content "<content>"

# List memory
hermes memory list
```

### Cron Jobs

```bash
# List cron jobs
hermes cron list

# Create a cron job
hermes cron create --name "<name>" --schedule "<schedule>" --prompt "<prompt>"

# Run a cron job
hermes cron run --job_id "<job_id>"

# Update, pause, resume, remove a cron job
hermes cron update --job_id "<job_id>"
```

### Tools

```bash
hermes tools list [--toolsets <t1,t2,...>]
```

## Available Tools

### browser_*
- `browser_navigate`: Navigate to URL
- `browser_snapshot`: Get page snapshot
- `browser_click`: Click element
- `browser_type`: Type text
- `browser_vision`: Take screenshot and analyze
- `browser_console`: Get console output
- `browser_scroll`: Scroll page

### terminal_*
- `terminal`: Run shell command
- `process`: Manage background processes

### file_*
- `read_file`: Read file
- `write_file`: Write to file
- `patch`: Edit file (find & replace)
- `search_files`: Search files by content/name

### execute_code
- `execute_code`: Run Python script

### memory_*
- `memory`: Manage persistent memory

### skill_*
- `skill_manage`: Manage skills (CRUD)
- `skill_view`: View skill content

### delegate_task
- `delegate_task`: Spawn subagents for tasks

### cronjob
- `cronjob`: Manage scheduled cron jobs

## Authentication

### GitHub Token

```bash
# Export token
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Verify auth
curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/user
```

### OMLX Provider

Uses `GITHUB_TOKEN` environment variable for authentication when configured with `omlx` provider.

## Background Processes

Started with:
```bash
terminal(command="...", background=true)
```

Manage with:
```bash
process list          # List all processes
process wait          # Wait for completion
process poll          # Check status
process log           # View log
process kill          # Kill process
```

## Memory System

### Memory Types

- **user**: User preferences and profile
- **memory**: Project-specific notes and configuration

### Memory Actions

```bash
# Add new entry
hermes memory add --target <target> --content "<entry>"

# Replace entry
hermes memory replace --target <target> --old-text "<text>" --new-text "<text>"

# Remove entry
hermes memory remove --target <target> --old-text "<text>"
```

### Auto-Pruning

When memory reaches limit (~2500 chars), oldest entries are automatically removed.

## Tool Loop Guardrails

The agent uses guardrails to prevent harmful tool usage:

- **exact_failure**: Stop after 5 consecutive tool failures
- **same_tool_failure**: Stop after 8 consecutive same tool failures
- **idempotent_no_progress**: Stop after 5 iterations with no progress
- **protect_first_n**: Always keep first 3 turns (context)
- **protect_last_n**: Always keep last 20 turns (resolution)

## Tips for Best Results

1. **Be specific**: Clear instructions reduce ambiguity
2. **Provide context**: Share relevant files and information
3. **Use appropriate tools**: Choose the right tool for the task
4. **Be patient**: Complex tasks may need multiple iterations
5. **Review outputs**: Verify tool results before proceeding

## Common Patterns

### Quick File Edit

```bash
hermes -s "Read the file, then replace X with Y, then show the changed section"
```

### Run Tests

```bash
hermes -s "Run the tests in the project, report failures"
```

### Debug Issue

```bash
hermes -s "Analyze the error, read relevant files, propose and implement a fix"
```

### Explore Code

```bash
hermes -s "Give me an overview of the project structure, main files, and tech stack"
```

### Generate Code

```bash
hermes -s "Create a Python script that does X with error handling and documentation"
```

## Configuration

Edit `~/.hermes/config.yaml`:

```yaml
model:
  provider: omlx
  model: Qwen3.6-35B-A3B-4bit

memory:
  max_chars: 2500

tools:
  enable: ["browser", "terminal", "file"]

display:
  language: en
  streaming: true
```

## References

- **Documentation**: https://hermes-agent.nousresearch.com/docs
- **GitHub**: https://github.com/nousresearch/hermes-agent
- **Docker Hub**: https://hub.docker.com/r/nousresearch/hermes-agent

## Examples

### Generate Comic Art

```bash
hermes -s "Create high-quality comic art of a basketball player in 'basketball boy' style, transforming this photo into a manga-style illustration with dynamic action pose" --image-url <photo_url>
```

### GitHub PR Workflow

```bash
hermes -s "Create a new branch, make changes, and submit a PR"
```

### Background Build

```bash
hermes -s "Run tests in background, notify when complete" --args='{"background": true, "notify_on_complete": true}'
```

---

**Tip**: For complex tasks, consider splitting them into smaller, sequential steps or using cron jobs for automation.
