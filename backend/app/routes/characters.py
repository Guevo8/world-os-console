from fastapi import APIRouter, HTTPException
from typing import List, Optional
from ..models import CharacterCard
from ..storage import load_characters, save_character, delete_character

router = APIRouter(tags=["characters"])


@router.get("/characters")
async def list_characters(project_id: Optional[str] = None):
    """List all characters, optionally filtered by project"""
    characters = load_characters()
    
    if project_id:
        characters = [c for c in characters if c.project_id == project_id]
    
    return characters


@router.get("/characters/{character_id}")
async def get_character(character_id: str):
    """Get single character by ID"""
    characters = load_characters()
    character = next((c for c in characters if c.id == character_id), None)
    
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    return character


@router.post("/characters")
async def create_character(character: CharacterCard):
    """Create new character"""
    return save_character(character)


@router.put("/characters/{character_id}")
async def update_character(character_id: str, character: CharacterCard):
    """Update existing character"""
    character.id = character_id
    return save_character(character)


@router.delete("/characters/{character_id}")
async def delete_character_route(character_id: str):
    """Delete character"""
    success = delete_character(character_id)
    if not success:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"deleted": True, "id": character_id}
