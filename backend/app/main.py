from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import characters, prompts

app = FastAPI(
    title="world-os API",
    description="Worldbuilding Framework + Tools",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(characters.router)
app.include_router(prompts.router)

@app.get("/")
async def root():
    return {
        "message": "world-os API v2.0",
        "features": ["projects", "characters", "prompts"]
    }

@app.get("/health")
async def health():
    return {"status": "ok"}
