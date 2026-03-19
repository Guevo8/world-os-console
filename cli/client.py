"""
API Client für world-os CLI
"""
import requests
from typing import Optional, Dict, Any

class WorldOSClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
    
    def list_projects(self):
        """Get all projects"""
        response = requests.get(f"{self.base_url}/projects")
        response.raise_for_status()
        return response.json()
    
    def get_project(self, project_id: str):
        """Get single project"""
        response = requests.get(f"{self.base_url}/projects/{project_id}")
        response.raise_for_status()
        return response.json()
    
    def create_project(self, data: Dict[str, Any]):
        """Create new project"""
        response = requests.post(f"{self.base_url}/projects", json=data)
        response.raise_for_status()
        return response.json()
    
    def update_project(self, project_id: str, data: Dict[str, Any]):
        """Update project"""
        response = requests.put(f"{self.base_url}/projects/{project_id}", json=data)
        response.raise_for_status()
        return response.json()
    
    def delete_project(self, project_id: str):
        """Delete project"""
        response = requests.delete(f"{self.base_url}/projects/{project_id}")
        response.raise_for_status()
        return response.json()
