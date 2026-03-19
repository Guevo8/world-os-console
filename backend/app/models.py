from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
from datetime import datetime

# === PROJECT MODEL (EXISTIERT BEREITS) ===

class Project(BaseModel):
    """Core Project Model - 6-Tier Worldbuilding Framework"""
    id: str
    name: str
    type: str  # game, novel, ttrpg
    description: str = ""
    
    # T0: Foundation
    t0: Dict[str, Any] = {
        "canon": "",
        "physics": "",
        "themes": ""
    }
    
    # T1: Core
    t1: Dict[str, Any] = {
        "logline": "",
        "conflict": "",
        "factions": []
    }
    
    created_at: datetime
    updated_at: datetime


# === CHARACTER MODEL (NEU) ===

class CharacterCard(BaseModel):
    """TavernAI V2 + U-CPS compatible character card"""
    id: str = Field(default_factory=lambda: f"char-{int(datetime.now().timestamp())}")
    project_id: str  # Zu welchem Projekt gehört der Charakter
    
    # TavernAI V2 Core Fields
    name: str
    description: str = ""
    personality: str = ""
    tags: List[str] = []
    
    # U-CPS Extensions (optional)
    extensions: Dict[str, Any] = {
        "ucps": {
            "subject": "",
            "identity_anchors": [],
            "outfit": "",
            "emotion": "",
            "pose": "",
            "camera": {},
            "lighting": {},
            "environment": "",
            "style_tags": [],
            "aspect_ratio": "1:1",
            "exclusions": []
        }
    }
    
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


# === PROMPT TEMPLATE MODEL (NEU) ===

class PromptTemplate(BaseModel):
    """SD Prompt Template for project-specific image generation"""
    id: str = Field(default_factory=lambda: f"prompt-{int(datetime.now().timestamp())}")
    project_id: Optional[str] = None  # Kann zu Projekt gehören oder global sein
    
    name: str
    description: str = ""
    
    # SD Module Configuration
    modules: Dict[str, str] = {
        "shotType": "",
        "cameraAngle": "",
        "lensAperture": "",
        "lighting": "",
        "styleGenre": "",
        "textureAtmosphere": "",
        "colorGrade": "",
        "composition": "",
        "focusDepth": "",
        "aspectRatio": "",
        "cameraFilm": ""
    }
    
    # Generated Prompts
    prompt: str = ""
    negative_prompt: str = ""
    
    # Metadata
    conflicts: List[str] = []
    
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
