#!/usr/bin/env python3
"""
world-os CLI - Worldbuilding Framework Command Line Interface
"""
import sys
from pathlib import Path
import typer

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from cli.commands import projects, characters, prompts
from cli.commands.serve import serve as serve_cmd

app = typer.Typer(
    name="world-os",
    help="Worldbuilding Framework CLI"
)

# Add subcommands
app.add_typer(projects.app, name="projects")
app.add_typer(characters.app, name="characters")
app.add_typer(prompts.app, name="prompts")


@app.command()
def serve(port: int = typer.Option(8000, help="Port number")):
    """Start API server"""
    serve_cmd(port)


def main():
    app()


if __name__ == '__main__':
    main()
