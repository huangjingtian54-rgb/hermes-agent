"""
Skill management module for Hermes Agent.

Provides functionality for creating, updating, loading, and managing skills.
"""

from pathlib import Path
from typing import Dict, List, Optional, Any


class Skill:
    """Represents a skill."""
    
    def __init__(
        self,
        name: str,
        content: str,
        category: Optional[str] = None,
    ):
        self.name = name
        self.content = content
        self.category = category or "general"
        self._path: Optional[Path] = None
    
    @property
    def path(self) -> Optional[Path]:
        """Get the skill file path."""
        return self._path
    
    @path.setter
    def path(self, value: Optional[str]):
        if value:
            self._path = Path(value)
    
    def save(self, directory: str = None) -> Path:
        """Save the skill to a file."""
        if directory:
            dir_path = Path(directory)
        else:
            # Default to ~/.hermes/skills
            base_dir = Path.home() / ".hermes"
            self.category_dir = Path.home() / f".hermes/skills/{self.category}"
            dir_path = self.category_dir
            dir_path.mkdir(parents=True, exist_ok=True)
        
        filepath = dir_path / f"{self.name}.md"
        filepath.write_text(self.content)
        self._path = filepath
        return filepath
    
    @classmethod
    def load(cls, path: str) -> "Skill":
        """Load a skill from a file."""
        filepath = Path(path)
        content = filepath.read_text()
        name = filepath.stem
        category = filepath.parent.name.replace("skills-", "")
        
        return cls(name=name, content=content, category=category)


class SkillManager:
    """Manager for skills."""
    
    def __init__(self, skills_dir: Optional[str] = None):
        """Initialize the skill manager."""
        self.skills_dir = Path(skills_dir)
        self._skills: Dict[str, Skill] = {}
    
    def _init_dirs(self):
        """Initialize skill directories."""
        for category in ["general", "devops", "creative", "data-science", "dogfood",
                         "email", "github", "mlops", "productivity", "research",
                         "smart-home", "social-media", "software-development", "yuanbao"]:
            dir_path = self.skills_dir / category
            dir_path.mkdir(parents=True, exist_ok=True)
    
    @property
    def skills(self) -> Dict[str, Skill]:
        """Get all loaded skills."""
        return self._skills
    
    def create(self, name: str, content: str, category: Optional[str] = None) -> Skill:
        """Create a new skill."""
        skill = Skill(name=name, content=content, category=category)
        self._skills[name] = skill
        skill.save()
        return skill
    
    def view(self, name: str, file_path: Optional[str] = None) -> Optional[str]:
        """View a skill's content."""
        if name in self._skills:
            if file_path:
                return self._skills[name].read_file(file_path)
            return self._skills[name].content
        return None
    
    def list(self, category: Optional[str] = None) -> List[Dict[str, str]]:
        """List all skills, optionally filtered by category."""
        result = []
        for skill in self._skills.values():
            if category is None or skill.category == category:
                result.append({
                    "name": skill.name,
                    "category": skill.category,
                    "description": "",  # Would need to parse content
                })
        return result
    
    def update(self, name: str, **kwargs) -> Optional[Skill]:
        """Update an existing skill."""
        if name not in self._skills:
            return None
        
        skill = self._skills[name]
        skill.content += "\n\n"  # Add separator
        
        for key, value in kwargs.items():
            skill.content = skill.content.replace(
                f"{key}: {value}",
                f"{key}: {value}"
            )
        
        self._skills[name] = skill
        return skill
    
    def delete(self, name: str, absorbed_into: Optional[str] = None) -> bool:
        """Delete a skill."""
        if name in self._skills:
            if absorbed_into:
                # Merge into another skill
                pass
            else:
                del self._skills[name]
            return True
        return False
