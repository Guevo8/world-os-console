import json
from cli.client import WorldOSClient

def show_project(project_id: str):
    """Show project details"""
    client = WorldOSClient()
    
    try:
        project = client.get_project(project_id)
        
        print(f"📖 Project: {project['name']}")
        print(f"   ID: {project['id']}")
        print(f"   Type: {project['type']}")
        print(f"   Created: {project['created_at']}")
        print()
        
        # T0 Foundation
        t0 = project['tiers']['T0_foundation']
        if any(t0.values()):
            print("🏗️  T0 Foundation:")
            if t0.get('canon_statement'):
                print(f"   Canon: {t0['canon_statement']}")
            if t0.get('themes'):
                print(f"   Themes: {t0['themes']}")
            print()
        
        # T1 Core
        t1 = project['tiers']['T1_core']
        if any(t1.values()):
            print("🎯 T1 Core:")
            if t1.get('logline'):
                print(f"   Logline: {t1['logline']}")
            if t1.get('setting_summary'):
                print(f"   Setting: {t1['setting_summary']}")
            print()
        
        # Stats
        t2_count = len(project['tiers']['T2_modules'])
        t3_count = len(project['tiers']['T3_characters'])
        t4_count = len(project['tiers']['T4_zones'])
        t5_count = len(project['tiers']['T5_narrative'])
        
        print(f"📊 Content:")
        print(f"   Modules: {t2_count}")
        print(f"   Characters: {t3_count}")
        print(f"   Zones: {t4_count}")
        print(f"   Narratives: {t5_count}")
        
        return 0
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"❌ Project '{project_id}' not found")
        else:
            print(f"❌ Error: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
