"""
Memory module for Hermes Agent.

Provides persistent memory storage and retrieval across sessions.
"""

from pathlib import Path
from typing import List, Dict, Any, Optional
import json


class MemorySystem:
    """Persistent memory storage for Hermes Agent."""
    
    def __init__(self, memory_dir: Optional[str] = None):
        """Initialize memory system."""
        self.memory_dir = Path(memory_dir or Path.home()) / ".hermes" / "memory"
        self._user_memory: List[Dict[str, Any]] = []
        self._project_memory: List[Dict[str, Any]] = []
        self._max_chars = 2500
        self._user_max_chars = 800
        
        self.memory_dir.mkdir(parents=True, exist_ok=True)
    
    @property
    def user_memory(self) -> List[Dict[str, Any]]:
        """Get user memory entries."""
        return self._user_memory
    
    @property
    def project_memory(self) -> List[Dict[str, Any]]:
        """Get project-specific memory entries."""
        return self._project_memory
    
    @property
    def char_limit(self) -> int:
        """Get total character limit."""
        total = sum(len(entry.get("content", "")) for entry in self._user_memory)
        total += sum(len(entry.get("content", "")) for entry in self._project_memory)
        return total
    
    def add(self, target: str, content: str) -> None:
        """Add a new memory entry."""
        if target == "user":
            target_store = self._user_memory
        elif target == "memory":
            target_store = self._project_memory
        else:
            raise ValueError(f"Invalid target: {target}")
        
        # Calculate new total chars
        new_content_len = len(content)
        projected_total = self.char_limit + new_content_len
        
        if projected_total > self._max_chars:
            # Remove old entries if needed
            entries_to_remove = []
            for i, entry in enumerate(target_store):
                if self.char_limit + len(entry.get("content", "")) + new_content_len > self._max_chars:
                    entries_to_remove.append(i)
            
            for idx in sorted(entries_to_remove, reverse=True):
                target_store.pop(idx)
        
        target_store.append({
            "target": target,
            "content": content,
        })
    
    def add_batch(self, operations: List[Dict[str, str]]) -> None:
        """Add multiple memory entries in a single batch."""
        for op in operations:
            action = op.get("action")
            content = op.get("content")
            old_text = op.get("old_text")
            
            if action == "add":
                self.add("memory", content)
            elif action == "replace":
                self._replace(old_text, content)
            elif action == "remove":
                self._remove(old_text)
    
    def _replace(self, old_text: str, new_content: str) -> None:
        """Replace an existing memory entry."""
        target = "memory"  # default
        # Find the entry
        for entry in self._user_memory:
            if entry.get("old_text") == old_text:
                entry["content"] = new_content
                entry["target"] = "user"
                break
        
        for entry in self._project_memory:
            if entry.get("old_text") == old_text:
                entry["content"] = new_content
                entry["target"] = "memory"
                break
    
    def _remove(self, old_text: str) -> None:
        """Remove a memory entry."""
        target = "memory"  # default
        
        for i, entry in enumerate(self._user_memory):
            if entry.get("old_text") == old_text:
                self._user_memory.pop(i)
                return
        
        for entry in self._project_memory:
            if entry.get("old_text") == old_text:
                self._project_memory.remove(entry)
                return
    
    def save(self) -> None:
        """Save all memory to files."""
        self._save_user_memory()
        self._save_project_memory()
    
    def _save_user_memory(self) -> None:
        """Save user memory to file."""
        filepath = self.memory_dir / "USER.md"
        with open(filepath, 'w') as f:
            f.write("# User Memory\n\n")
            for entry in self._user_memory:
                f.write(f"## {entry['content']}\n")
    
    def _save_project_memory(self) -> None:
        """Save project memory to file."""
        filepath = self.memory_dir / "PROJECT.md"
        with open(filepath, 'w') as f:
            f.write("# Project Memory\n\n")
            for entry in self._project_memory:
                f.write(f"## {entry['content']}\n")
