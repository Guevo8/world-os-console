from cli.client import WorldOSClient

def list_projects():
    """List all projects"""
    client = WorldOSClient()
    
    try:
        projects = client.list_projects()
        
        if not projects:
            print("📭 No projects yet. Create one with: world-os create \"My Project\"")
            return 0
        
        print(f"📚 {len(projects)} project(s):\n")
        for p in projects:
            print(f"  🔹 {p['id']}")
            print(f"     Name: {p['name']}")
            print(f"     Type: {p['type']}")
            if p.get('description'):
                print(f"     Desc: {p['description']}")
            print()
        
        return 0
    except requests.exceptions.ConnectionError:
        print("❌ Server not running. Start it with: world-os serve")
        return 1
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
