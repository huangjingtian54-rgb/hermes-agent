"""
Tool registry for Hermes Agent.

Provides a centralized registry of all available tools.
"""

from typing import Dict, Callable, Any, Type


class Tool:
    """Base class for all tools."""
    
    def __init__(
        self,
        name: str,
        description: str,
        args: Dict[str, Any] = None,
    ):
        self.name = name
        self.description = description
        self.args = args or {}
    
    def __call__(self, **kwargs) -> Any:
        """Execute the tool with given arguments."""
        raise NotImplementedError


class BrowserTool(Tool):
    """Browser automation tools."""
    pass


class TerminalTool(Tool):
    """Terminal command execution tools."""
    pass


class FileTool(Tool):
    """File system operation tools."""
    pass


class WebTool(Tool):
    """Web API interaction tools."""
    pass


class CodeExecTool(Tool):
    """Code execution tool."""
    pass


class MemoryTool(Tool):
    """Memory management tools."""
    pass


class SkillTool(Tool):
    """Skill management tools."""
    pass


class AgentTool(Tool):
    """Agent spawning and management tools."""
    pass


class CronJobTool(Tool):
    """Cron job management tools."""
    pass


class ConsoleTool(Tool):
    """Browser console inspection tool."""
    pass


class VisionTool(Tool):
    """Image vision and analysis tool."""
    pass


class TypeTool(Tool):
    """Text input tool."""
    pass


class ClickTool(Tool):
    """Browser click tool."""
    pass


class PressTool(Tool):
    """Keyboard press tool."""
    pass


class ScrollTool(Tool):
    """Browser scroll tool."""
    pass


class NavigateTool(Tool):
    """Browser navigation tool."""
    pass


class SnapshotTool(Tool):
    """Browser snapshot tool."""
    pass


class ToolRegistry:
    """Registry of all available tools."""
    
    def __init__(self):
        """Initialize the tool registry."""
        self._tools: Dict[str, Callable] = {}
        self._tool_classes: Dict[str, type] = {
            "browser": BrowserTool,
            "terminal": TerminalTool,
            "file": FileTool,
            "web": WebTool,
            "code_exec": CodeExecTool,
            "memory": MemoryTool,
            "skill": SkillTool,
            "agent": AgentTool,
            "cron": CronJobTool,
            "console": ConsoleTool,
            "vision": VisionTool,
            "type": TypeTool,
            "click": ClickTool,
            "press": PressTool,
            "scroll": ScrollTool,
            "navigate": NavigateTool,
            "snapshot": SnapshotTool,
        }
    
    def register(self, tool: Tool) -> None:
        """Register a tool."""
        self._tools[tool.name] = tool
    
    def unregister(self, name: str) -> bool:
        """Unregister a tool by name."""
        if name in self._tools:
            del self._tools[name]
            return True
        return False
    
    def get(self, name: str) -> Any:
        """Get a tool by name."""
        return self._tools.get(name)
    
    def list(self, toolsets: list = None) -> list:
        """List all registered tools."""
        tools = []
        for name, tool in self._tools.items():
            if toolsets is None or any(ts in name for ts in toolsets):
                tools.append({
                    "name": name,
                    "description": tool.description,
                    "toolset": type(tool).__name__.replace("Tool", ""),
                })
        return sorted(tools, key=lambda x: x["name"])
