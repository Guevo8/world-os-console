import re
from cli.client import WorldOSClient

def slugify(text: str) -> str:
    """Convert text to slug-friendly ID"""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text

def create_project(name: str, project_type: str, description: str = None):
    """Create new project"""
    client = WorldOSClient()
    
    # Generate ID from name
    project_id = slugify(name)
    
    data = {
        "id": project_id,
        "name": name,
        "type": project_type,
        "description": description,
        "tags": [],
        "tiers": {
            "T0_foundation": {},
            "T1_core": {}
        }
    }
    
    try:
        project = client.create_project(data)
        print(f"✅ Created project: {project['name']}")
        print(f"   ID: {project['id']}")
        print(f"   Type: {project['type']}")
        print()
        print(f"Next steps:")
        print(f"  world-os show {project['id']}")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
