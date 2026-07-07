"""
Browser tool implementations.
"""

import requests
from typing import Optional, Dict, Any


class BrowserTool:
    """Browser automation tool."""
    
    def __init__(self, base_url: str = "https://hermes-agent.api.nousresearch.com"):
        self.base_url = base_url
    
    def navigate(self, url: str) -> Dict[str, Any]:
        """Navigate to a URL and get page snapshot."""
        params = {"url": url, "full": False}
        response = requests.get(f"{self.base_url}/browser/navigate", params=params)
        return response.json()
    
    def snapshot(self, full: bool = False) -> Dict[str, Any]:
        """Get page snapshot."""
        params = {"full": full}
        response = requests.post(f"{self.base_url}/browser/snapshot", params=params)
        return response.json()
    
    def click(self, ref: str) -> Dict[str, Any]:
        """Click on an element."""
        data = {"ref": ref}
        response = requests.post(f"{self.base_url}/browser/click", json=data)
        return response.json()
    
    def type(self, ref: str, text: str) -> Dict[str, Any]:
        """Type text into an input field."""
        data = {"ref": ref, "text": text}
        response = requests.post(f"{self.base_url}/browser/type", json=data)
        return response.json()
    
    def press(self, key: str) -> Dict[str, Any]:
        """Press a keyboard key."""
        data = {"key": key}
        response = requests.post(f"{self.base_url}/browser/press", json=data)
        return response.json()
    
    def scroll(self, direction: str) -> Dict[str, Any]:
        """Scroll the page."""
        data = {"direction": direction}
        response = requests.post(f"{self.base_url}/browser/scroll", json=data)
        return response.json()
    
    def vision(self, question: str, annotate: bool = False) -> Dict[str, Any]:
        """Take a screenshot and answer question."""
        data = {"question": question, "annotate": annotate}
        response = requests.post(f"{self.base_url}/browser/vision", json=data)
        return response.json()
    
    def console(self, clear: bool = False, expression: Optional[str] = None) -> Dict[str, Any]:
        """Get browser console output."""
        data = {"clear": clear}
        if expression:
            data["expression"] = expression
        response = requests.post(f"{self.base_url}/browser/console", json=data)
        return response.json()
    
    def get_images(self) -> Dict[str, Any]:
        """Get images on the current page."""
        response = requests.post(f"{self.base_url}/browser/get_images")
        return response.json()
    
    def back(self) -> Dict[str, Any]:
        """Navigate back in browser history."""
        response = requests.post(f"{self.base_url}/browser/back")
        return response.json()


# Import script functions
from hermes_agent.scripts import *
