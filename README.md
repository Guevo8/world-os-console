# 🌍 world-os-console

**6-Tier Worldbuilding Framework** with FastAPI Backend + CLI

A structured system for building consistent fictional universes for novels, games, TTRPGs, and screenplays.

## 🏗️ The 6-Tier System
T0 Foundation  → Canon, Physics, Themes
T1 Core        → Logline, Conflict, Factions
T2 Modules     → Magic, Technology, Culture
T3 Characters  → NPCs, Goals, Relationships
T4 Zones       → Locations, Atmosphere
T5 Narrative   → Plots, Story Arcs
## 🚀 Quickstart

### Installation
```bash
pip install -e .
Start Server
world-os serve
# Server runs on http://localhost:8000
# API Docs: http://localhost:8000/docs
CLI Commands
# List all projects
world-os list

# Create new project
world-os create "My World" --type novel --description "Epic fantasy saga"

# Show project details
world-os show my-world

# Get help
world-os --help
📂 Project Structure
world-os-console/
├── backend/          # FastAPI server
│   ├── app/
│   │   ├── main.py      # API routes
│   │   ├── models.py    # Pydantic models
│   │   └── storage.py   # JSON persistence
│   └── data/
│       └── projects.json
├── cli/              # CLI tool
│   ├── main.py       # Entry point
│   ├── client.py     # API client
│   └── commands/     # Command implementations
└── setup.py
🎯 Use Cases
Authors: Organize novel series worldbuilding
Game Designers: Create consistent game worlds
TTRPG Masters: Build campaign settings
Worldbuilding Coaches: Structure client projects
🔧 Tech Stack
Backend: FastAPI, Pydantic, Uvicorn
CLI: Python argparse, requests
Storage: JSON file-based (portable)
📖 API Endpoints
GET /health - Health check
GET /projects - List all projects
GET /projects/{id} - Get project details
POST /projects - Create project
PUT /projects/{id} - Update project
DELETE /projects/{id} - Delete project
🌟 Example Projects
The system comes with example projects:
Heartroot City - Biotech tree city (game)
Hydraulic Dreams - Steampunk-cyberpunk fusion
Resonanz-Chroniken - Cyberpunk-fantasy with resonance physics
Die Echoverbundene Sphäre - Dark fantasy resonance world
🛠️ Development
# Run server in development mode
cd backend
uvicorn app.main:app --reload

# Run CLI from source
python cli/main.py list
📝 License
MIT
👤 Author
Tobi Peters (Guevo8)
Built with Python 🐍 for structured creative worldbuilding
