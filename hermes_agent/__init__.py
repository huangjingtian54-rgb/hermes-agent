"""
Hermes Agent - Intelligent AI Agent CLI

An AI-powered command-line agent that helps with development tasks,
code review, debugging, research, and automation.
"""

from hermes_agent.__version__ import __version__
from hermes_agent.config import Config
from hermes_agent.agents import Agent
from hermes_agent.memory import MemorySystem
from hermes_agent.tools import ToolRegistry
from hermes_agent.scripts import run, chat, setup, config, skills, cron

__all__ = [
    '__version__',
    'Config',
    'Agent',
    'MemorySystem',
    'ToolRegistry',
    'run',
    'chat',
    'setup',
    'config',
    'skills',
    'cron',
]
