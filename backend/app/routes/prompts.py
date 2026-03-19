from fastapi import APIRouter, HTTPException
from typing import List, Optional
from ..models import PromptTemplate
from ..storage import load_prompts, save_prompt, delete_prompt

router = APIRouter(tags=["prompts"])


@router.get("/prompts")
async def list_prompts(project_id: Optional[str] = None):
    """List all prompt templates, optionally filtered by project"""
    prompts = load_prompts()
    
    if project_id:
        prompts = [p for p in prompts if p.project_id == project_id]
    
    return prompts


@router.get("/prompts/{prompt_id}")
async def get_prompt(prompt_id: str):
    """Get single prompt template by ID"""
    prompts = load_prompts()
    prompt = next((p for p in prompts if p.id == prompt_id), None)
    
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    
    return prompt


@router.post("/prompts")
async def create_prompt(prompt: PromptTemplate):
    """Create new prompt template"""
    return save_prompt(prompt)


@router.put("/prompts/{prompt_id}")
async def update_prompt(prompt_id: str, prompt: PromptTemplate):
    """Update existing prompt template"""
    prompt.id = prompt_id
    return save_prompt(prompt)


@router.delete("/prompts/{prompt_id}")
async def delete_prompt_route(prompt_id: str):
    """Delete prompt template"""
    success = delete_prompt(prompt_id)
    if not success:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return {"deleted": True, "id": prompt_id}
