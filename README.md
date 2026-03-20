# world-os-console
**Worldbuilding Framework + Character Management + Prompt Templates**

Version 2.0 - Production-Ready Backend with CLI

---

## 🎯 Features

### Core System (v1.0)
- **6-Tier Worldbuilding Framework**
  - T0: Foundation (Canon, Physics, Themes)
  - T1: Core (Logline, Conflict, Factions)
  - T2: Modules (Magic, Technology, Culture)
  - T3: Characters
  - T4: Zones
  - T5: Narrative

### NEW in v2.0
- ✅ **Character Management** (TavernAI V2 + U-CPS compatible)
- ✅ **Prompt Templates** (Stable Diffusion / AI Image Gen)
- ✅ **REST API** (FastAPI)
- ✅ **CLI Tool** (systemwide installation)

---

## 🚀 Quick Start

### Installation

```bash
# Clone
git clone https://github.com/Guevo8/world-os-console.git
cd world-os-console

# Install CLI (optional)
pip install -e .

# Install Backend Dependencies
cd backend
pip install -r requirements.txt
```

### Start Server

```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Server runs on: **http://localhost:8000**

### CLI Usage

```bash
# Manage projects
world-os list
world-os create "My World" --type novel
world-os show my-world-001

# Start server
world-os serve --port 8000
```

---

## 📚 API Endpoints

### Projects
- `GET /` - API Info
- `GET /health` - Health Check

### Characters (NEW)
- `GET /characters` - List all characters
- `GET /characters?project_id=xyz` - Filter by project
- `POST /characters` - Create character
- `PUT /characters/{id}` - Update character
- `DELETE /characters/{id}` - Delete character

### Prompts (NEW)
- `GET /prompts` - List all prompt templates
- `POST /prompts` - Create prompt template
- `PUT /prompts/{id}` - Update prompt
- `DELETE /prompts/{id}` - Delete prompt

---

## 📂 Project Structure

```
world-os-console/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app
│   │   ├── models.py        # Pydantic models
│   │   ├── storage.py       # JSON persistence
│   │   └── routes/          # API routes
│   │       ├── characters.py
│   │       └── prompts.py
│   ├── data/
│   │   ├── projects.json    # Your worlds
│   │   ├── characters.json  # Your characters
│   │   └── prompts.json     # Your prompt templates
│   └── requirements.txt
├── cli/
│   ├── main.py              # CLI entry point
│   └── commands/
├── setup.py
└── README.md
```

---

## 🔧 Tech Stack

- **Backend**: FastAPI + Pydantic + Uvicorn
- **CLI**: Typer + Rich
- **Storage**: JSON files (simple, portable)
- **Python**: 3.10+

---

## 💾 Data Models

### Character Card (TavernAI V2 Compatible)
```json
{
  "id": "char-123",
  "project_id": "my-world",
  "name": "Kai Voss",
  "description": "Protagonist",
  "tags": ["Mechaniker", "Zynisch"],
  "extensions": {
    "ucps": {
      "outfit": "oil-stained work clothes",
      "emotion": "distrustful"
    }
  }
}
```

### Prompt Template (SD/AI Image Gen)
```json
{
  "id": "prompt-456",
  "project_id": "hydraulic-dreams",
  "name": "Steampunk Invention",
  "modules": {
    "shotType": "Insert Shot",
    "lighting": "Rembrandt",
    "styleGenre": "Steampunk"
  },
  "prompt": "steampunk machinery, brass gears, smoky ambience",
  "negative_prompt": "no artifacts, no glitches"
}
```

---

## 🎨 Use Cases

### For Authors
- Manage characters across multiple novels
- Track character arcs and relationships
- Export character sheets as JSON/Markdown

### For Game Designers
- Worldbuilding with 6-tier framework
- Character database for NPCs
- Prompt templates for concept art generation

### For TTRPG Masters
- Campaign management
- NPC database
- Visual reference library via prompts

---

## 🔐 Security Notes

- `backend/data/*.json` files are gitignored
- Your characters and prompts stay local
- No telemetry, no cloud sync (unless you want it)

---

## 🚧 Roadmap

### v2.1 (Next)
- [ ] CLI commands for characters/prompts
- [ ] Markdown/PDF export
- [ ] Character → Prompt auto-generation

### v3.0 (Future)
- [ ] Web Frontend (React)
- [ ] Image upload support
- [ ] Cloud sync (optional)

---

## 📝 Development

```bash
# Run tests (TODO)
pytest

# Format code
black .

# Type checking
mypy backend/
```

---

## 🤝 Contributing

This is a personal project, but feedback welcome!

---

## 📄 License

MIT License - Do whatever you want with it!

---

## 👨‍💻 Author

**Tobi** (Guevo8)  
Self-taught developer from Mönchengladbach, Germany.

Building tools for worldbuilding, character management, and creative workflows.  
Codes mainly on Android via Termux, switches to VS Code for larger projects.

---

## 🙏 Credits

- Built with love on a Samsung phone via Termux
- Powered by FastAPI, Pydantic, and lots of coffee ☕

---

**Last Updated:** 2026-03-20  
**Version:** 2.0.0
