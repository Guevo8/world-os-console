import typer
import requests
from rich.console import Console
from rich.table import Table
from typing import Optional

app = typer.Typer(help="Manage characters")
console = Console()

API_BASE = "http://localhost:8000"


@app.command("list")
def list_characters(
    project: Optional[str] = typer.Option(None, "--project", "-p", help="Filter by project ID")
):
    """List all characters"""
    url = f"{API_BASE}/characters"
    params = {"project_id": project} if project else {}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        characters = response.json()
        
        if not characters:
            console.print("[yellow]No characters found[/yellow]")
            return
        
        table = Table(title="Characters")
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Project", style="blue")
        table.add_column("Tags", style="magenta")
        
        for char in characters:
            tags = ", ".join(char.get("tags", []))
            table.add_row(
                char["id"][:16] + "...",
                char["name"],
                char["project_id"],
                tags or "-"
            )
        
        console.print(table)
        console.print(f"\n[green]Total: {len(characters)} characters[/green]")
        
    except requests.exceptions.ConnectionError:
        console.print("[red]Error: Server not running. Start with 'world-os serve'[/red]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")


@app.command("show")
def show_character(character_id: str):
    """Show character details"""
    url = f"{API_BASE}/characters/{character_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        char = response.json()
        
        console.print(f"\n[bold cyan]Character: {char['name']}[/bold cyan]")
        console.print(f"[dim]ID: {char['id']}[/dim]")
        console.print(f"Project: {char['project_id']}")
        console.print(f"Tags: {', '.join(char.get('tags', []))}")
        
        if char.get("description"):
            console.print(f"\n[bold]Description:[/bold]\n{char['description']}")
        
        if char.get("personality"):
            console.print(f"\n[bold]Personality:[/bold]\n{char['personality']}")
        
        # U-CPS Info
        ucps = char.get("extensions", {}).get("ucps", {})
        if ucps.get("outfit") or ucps.get("emotion"):
            console.print("\n[bold]U-CPS Profile:[/bold]")
            if ucps.get("outfit"):
                console.print(f"  Outfit: {ucps['outfit']}")
            if ucps.get("emotion"):
                console.print(f"  Emotion: {ucps['emotion']}")
        
        console.print(f"\n[dim]Created: {char['created_at'][:10]}[/dim]")
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            console.print(f"[red]Character '{character_id}' not found[/red]")
        else:
            console.print(f"[red]Error: {e}[/red]")
    except requests.exceptions.ConnectionError:
        console.print("[red]Error: Server not running[/red]")


@app.command("add")
def add_character(
    name: str = typer.Argument(..., help="Character name"),
    project: str = typer.Option(..., "--project", "-p", help="Project ID"),
    tags: str = typer.Option("", "--tags", "-t", help="Comma-separated tags"),
    description: str = typer.Option("", "--description", "-d", help="Character description"),
    personality: str = typer.Option("", "--personality", help="Character personality"),
):
    """Create a new character"""
    url = f"{API_BASE}/characters"
    
    data = {
        "project_id": project,
        "name": name,
        "description": description,
        "personality": personality,
        "tags": [t.strip() for t in tags.split(",") if t.strip()]
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        char = response.json()
        
        console.print(f"\n[green]✓ Character created:[/green]")
        console.print(f"  ID: {char['id']}")
        console.print(f"  Name: {char['name']}")
        console.print(f"  Project: {char['project_id']}")
        
    except requests.exceptions.ConnectionError:
        console.print("[red]Error: Server not running[/red]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")


@app.command("delete")
def delete_character(
    character_id: str,
    yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation")
):
    """Delete a character"""
    
    if not yes:
        confirm = typer.confirm(f"Delete character '{character_id}'?")
        if not confirm:
            console.print("[yellow]Cancelled[/yellow]")
            return
    
    url = f"{API_BASE}/characters/{character_id}"
    
    try:
        response = requests.delete(url)
        response.raise_for_status()
        
        console.print(f"[green]✓ Character '{character_id}' deleted[/green]")
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            console.print(f"[red]Character '{character_id}' not found[/red]")
        else:
            console.print(f"[red]Error: {e}[/red]")
    except requests.exceptions.ConnectionError:
        console.print("[red]Error: Server not running[/red]")


if __name__ == "__main__":
    app()
