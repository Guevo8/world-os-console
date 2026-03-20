import json
from pathlib import Path
from typing import List
from datetime import datetime, timezone

from .models import Project, CharacterCard, PromptTemplate

# Paths
DATA_PATH = Path(__file__).resolve().parent.parent / "data"
DATA_FILE = DATA_PATH / "projects.json"
CHARACTERS_FILE = DATA_PATH / "characters.json"
PROMPTS_FILE = DATA_PATH / "prompts.json"


def _ensure_storage() -> None:
    DATA_PATH.mkdir(parents=True, exist_ok=True)
    
    # Stelle sicher, dass alle JSON-Dateien existieren
    for file_path in (DATA_FILE, CHARACTERS_FILE, PROMPTS_FILE):
        if not file_path.exists():
            file_path.write_text("[]", encoding="utf-8")


# =====================================================
# PROJECT STORAGE (EXISTIERT BEREITS)
# =====================================================

def load_projects() -> List[Project]:
    _ensure_storage()
    raw_text = DATA_FILE.read_text(encoding="utf-8").strip()
    if not raw_text:
        return []
    data = json.loads(raw_text)
    return [Project(**item) for item in data]


def save_projects(projects: List[Project]) -> None:
    _ensure_storage()
    data = [p.dict() for p in projects]
    DATA_FILE.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")


# =====================================================
# CHARACTER STORAGE (NEU)
# =====================================================

def load_characters() -> List[CharacterCard]:
    """Load all characters from JSON"""
    _ensure_storage()
    
    try:
        with open(CHARACTERS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [CharacterCard(**char) for char in data]
    except Exception as e:
        print(f"Error loading characters: {e}")
        return []


def save_character(character: CharacterCard) -> CharacterCard:
    """Save or update character"""
    characters = load_characters()
    
    # Check if character exists
    existing_idx = None
    for i, c in enumerate(characters):
        if c.id == character.id:
            existing_idx = i
            break
    
    # Update or append
    if existing_idx is not None:
        character.updated_at = datetime.now()
        characters[existing_idx] = character
    else:
        characters.append(character)
    
    # Save to file
    with open(CHARACTERS_FILE, 'w', encoding='utf-8') as f:
        json.dump([c.dict() for c in characters], f, indent=2, default=str)
    
    return character


def delete_character(character_id: str) -> bool:
    """Delete character by ID"""
    characters = load_characters()
    before = len(characters)
    
    remaining = [c for c in characters if c.id != character_id]
    deleted = len(remaining) != before
    
    if deleted:
        with open(CHARACTERS_FILE, 'w', encoding='utf-8') as f:
            json.dump([c.dict() for c in remaining], f, indent=2, default=str)
    
    return deleted


# =====================================================
# PROMPT TEMPLATE STORAGE (NEU)
# =====================================================

def load_prompts() -> List[PromptTemplate]:
    """Load all prompt templates from JSON"""
    _ensure_storage()
    
    try:
        with open(PROMPTS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [PromptTemplate(**p) for p in data]
    except Exception as e:
        print(f"Error loading prompts: {e}")
        return []


def save_prompt(prompt: PromptTemplate) -> PromptTemplate:
    """Save or update prompt template"""
    prompts = load_prompts()
    
    # Check if prompt exists
    existing_idx = None
    for i, p in enumerate(prompts):
        if p.id == prompt.id:
            existing_idx = i
            break
    
    # Update or append
    if existing_idx is not None:
        prompt.updated_at = datetime.now()
        prompts[existing_idx] = prompt
    else:
        prompts.append(prompt)
    
    # Save to file
    with open(PROMPTS_FILE, 'w', encoding='utf-8') as f:
        json.dump([p.dict() for p in prompts], f, indent=2, default=str)
    
    return prompt


def delete_prompt(prompt_id: str) -> bool:
    """Delete prompt template by ID"""
    prompts = load_prompts()
    before = len(prompts)
    
    remaining = [p for p in prompts if p.id != prompt_id]
    deleted = len(remaining) != before
    
    if deleted:
        with open(PROMPTS_FILE, 'w', encoding='utf-8') as f:
            json.dump([p.dict() for p in remaining], f, indent=2, default=str)
    
    return deleted
