# Hermes Agent

**Hermes Agent** is an intelligent AI agent powered by Nous Research, designed for productivity, automation, and complex task execution.

## 🚀 Features

- **Multi-Modal Capabilities**: Text, code, images, audio, and vision analysis
- **Persistent Memory**: Cross-session memory for context retention
- **Background Processes**: Run background tasks with intelligent monitoring
- **Skill System**: Reusable skills for common workflows
- **Smart Tools**: Browser automation, terminal, file operations, API integration
- **Conversation Memory**: Session-aware with auto-pruning and compression
- **Plugin Architecture**: Extendable with custom tools and integrations
- **Multi-Provider Support**: Flexible model routing across providers

## 📋 Quick Start

```bash
# Install Hermes CLI
pip install hermes-agent

# Start a new session
hermes --session

# Or use in desktop app
# Open Hermes Desktop app
```

## 🛠️ Tools Available

| Tool | Description |
|------|-------------|
| `browser_navigate` | Navigate to URLs, load web pages |
| `browser_snapshot` | Get page accessibility tree snapshot |
| `browser_click` | Click on interactive elements |
| `browser_type` | Type text into input fields |
| `browser_vision` | Take screenshots, analyze visual content |
| `browser_console` | Get browser console output and errors |
| `terminal` | Execute shell commands |
| `process` | Manage background processes |
| `read_file` | Read text files |
| `write_file` | Write to files |
| `patch` | Edit files with find-and-replace |
| `search_files` | Search files by content or pattern |
| `execute_code` | Run Python scripts |
| `memory` | Save/load persistent memory |
| `skill_manage` | Manage skills (CRUD) |
| `skill_view` | View skill content and linked files |
| `delegate_task` | Spawn subagents for complex tasks |
| `cronjob` | Schedule and manage cron jobs |
| And many more... |

## 📖 Usage

### Chat with Hermes

```bash
# Start a chat session
hermes -c "Your question or instruction"

# Use in desktop app (Hermes GUI)
```

### Tips for Best Results

1. **Be Specific**: Clear, detailed instructions work best
2. **Provide Context**: Share relevant files, errors, or background info
3. **Use Tools Appropriately**: Choose the right tool for the task
4. **Be Patient**: Complex tasks may require multiple iterations
5. **Check Outputs**: Verify tool results before proceeding

## 🧠 Memory System

- **User Memory**: Your preferences, settings, and profile info
- **Persistent Memory**: Project notes, environment config, tool quirks
- **Auto-Pruning**: Session content auto-summarized when memory fills
- **Context Management**: Automatic compression to preserve important context

## 🎯 Skills System

Skills are reusable workflows for common tasks:

```bash
# List available skills
hermes skills list

# View a skill
hermes skills view <skill-name>

# Create a new skill
hermes skills create <name> --category <category>

# Patch an existing skill
hermes skills patch <name> --old-text --new-text

# Delete a skill
hermes skills delete <name>
```

### Popular Skills by Category

| Category | Skills |
|----------|--------|
| `devops` | `github-auth-setup`, `github-pr-workflow`, `github-code-review` |
| `creative` | `ascii-art`, `baoyu-infographic`, `architecture-diagram`, `p5js` |
| `mlops` | `huggingface-hub`, `evaluating-llms-harness`, `serving-llms-vllm` |
| `productivity` | `google-workspace`, `notion`, `powerpoint`, `airtable` |
| `research` | `arxiv`, `blogwatcher`, `llm-wiki`, `polymarket` |
| `data-science` | `jupyter-live-kernel` |
| `smart-home` | `openhue` |

## 🔒 Security & Auth

### GitHub Authentication

```bash
# Set your GitHub token
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Test auth
gh auth status
```

### Best Practices

- Use **fine-granced tokens** for limited permissions
- **Rotate tokens** periodically
- **Never share** tokens in public contexts
- **Use secrets** for API keys in workflows

## 📦 Installation

### Python Package

```bash
pip install hermes-agent
```

### Desktop App

Download from: https://github.com/nousresearch/hermes-agent/releases

### Docker

```bash
docker run nousresearch/hermes-agent
```

## 🔧 Configuration

Create/Edit `~/.hermes/config.yaml`:

```yaml
model:
  provider: omlx
  model: qwen3.5-9b-mlx-4bit

memory:
  mode: hybrid
  compression:
    - session_prune
    - threshold: 0.6

tools:
  enable:
    - browser
    - terminal
    - file
    - web
  disable: []

skills: []

gateway:
  url: "https://api.nousresearch.com"
  timeout: 30

logging:
  level: info
  file: ~/.hermes/logs/hermes.log
```

## 🌐 API

```bash
# List tools
hermes tools list

# Get model info
hermes models list --provider omlx

# List cron jobs
hermes cron job list
```

## 📚 Learn More

- [Documentation](https://hermes-agent.nousresearch.com/docs)
- [GitHub](https://github.com/nousresearch/hermes-agent)
- [Docker Hub](https://hub.docker.com/r/nousresearch/hermes-agent)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details.

## 👥 Credits

- Powered by [Nous Research](https://nousresearch.com)
- Models by [Qwen](https://huggingface.co/Qwen)
- Icons by [Heroicons](https://heroicons.com)

---

**Made with ❤️ by Nous Research**
