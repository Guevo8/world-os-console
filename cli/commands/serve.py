import os
import sys

def serve(port: int):
    """Start FastAPI server"""
    print(f"🚀 Starting world-os server on port {port}...")
    print(f"📚 API Docs: http://localhost:{port}/docs")
    print(f"🔍 Health: http://localhost:{port}/health")
    print()
    print("Press CTRL+C to stop")
    print()
    
    os.chdir("backend")
    os.execvp("uvicorn", ["uvicorn", "app.main:app", "--reload", "--port", str(port)])
