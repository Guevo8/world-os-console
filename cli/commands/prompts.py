import typer
import requests
from rich.console import Console
from rich.table import Table
from typing import Optional

app = typer.Typer(help="Manage prompt templates")
console = Console()

API_BASE = "http://localhost:8000"


@app.command("list")
def list_prompts(
    project: Optional[str] = typer.Option(None, "--project", "-p", help="Filter by project ID")
):
    """List all prompt templates"""
    url = f"{API_BASE}/prompts"
    params = {"project_id": project} if project else {}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        prompts = response.json()
        
        if not prompts:
            console.print("[yellow]No prompts found[/yellow]")
            return
        
        table = Table(title="Prompt Templates")
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Project", style="blue")
        table.add_column("Modules", style="magenta")
        
        for p in prompts:
            modules = [k for k, v in p.get("modules", {}).items() if v]
            modules_str = ", ".join(modules[:3])
            if len(modules) > 3:
                modules_str += f" +{len(modules)-3}"
            
            table.add_row(
                p["id"][:16] + "...",
                p["name"],
                p.get("project_id", "global") or "global",
                modules_str or "-"
            )
        
        console.print(table)
        console.print(f"\n[green]Total: {len(prompts)} prompts[/green]")
        
    except requests.exceptions.ConnectionError:
        console.print("[red]Error: Server not running[/red]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")


@app.command("show")
def show_prompt(prompt_id: str):
    """Show prompt template details"""
    url = f"{API_BASE}/prompts/{prompt_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        p = response.json()
        
        console.print(f"\n[bold cyan]Prompt: {p['name']}[/bold cyan]")
        console.print(f"[dim]ID: {p['id']}[/dim]")
        console.print(f"Project: {p.get('project_id', 'global') or 'global'}")
        
        if p.get("description"):
            console.print(f"\n[bold]Description:[/bold]\n{p['description']}")
        
        # Modules
        modules = {k: v for k, v in p.get("modules", {}).items() if v}
        if modules:
            console.print("\n[bold]SD Modules:[/bold]")
            for key, value in modules.items():
                console.print(f"  {key}: {value}")
        
        # Prompts
        if p.get("prompt"):
            console.print(f"\n[bold]Prompt:[/bold]\n{p['prompt']}")
        
        if p.get("negative_prompt"):
            console.print(f"\n[bold]Negative:[/bold]\n{p['negative_prompt']}")
        
        console.print(f"\n[dim]Created: {p['created_at'][:10]}[/dim]")
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            console.print(f"[red]Prompt '{prompt_id}' not found[/red]")
        else:
            console.print(f"[red]Error: {e}[/red]")
    except requests.exceptions.ConnectionError:
        console.print("[red]Error: Server not running[/red]")


@app.command("add")
def add_prompt(
    name: str = typer.Argument(..., help="Prompt name"),
    project: Optional[str] = typer.Option(None, "--project", "-p", help="Project ID"),
    description: str = typer.Option("", "--description", "-d", help="Description"),
    prompt: str = typer.Option("", "--prompt", help="Positive prompt text"),
):
    """Create a new prompt template"""
    url = f"{API_BASE}/prompts"
    
    data = {
        "name": name,
        "project_id": project,
        "description": description,
        "prompt": prompt
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        p = response.json()
        
        console.print(f"\n[green]✓ Prompt created:[/green]")
        console.print(f"  ID: {p['id']}")
        console.print(f"  Name: {p['name']}")
        
    except requests.exceptions.ConnectionError:
        console.print("[red]Error: Server not running[/red]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")


@app.command("delete")
def delete_prompt(
    prompt_id: str,
    yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation")
):
    """Delete a prompt template"""
    
    if not yes:
        confirm = typer.confirm(f"Delete prompt '{prompt_id}'?")
        if not confirm:
            console.print("[yellow]Cancelled[/yellow]")
            return
    
    url = f"{API_BASE}/prompts/{prompt_id}"
    
    try:
        response = requests.delete(url)
        response.raise_for_status()
        
        console.print(f"[green]✓ Prompt '{prompt_id}' deleted[/green]")
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            console.print(f"[red]Prompt '{prompt_id}' not found[/red]")
        else:
            console.print(f"[red]Error: {e}[/red]")
    except requests.exceptions.ConnectionError:
        console.print("[red]Error: Server not running[/red]")


if __name__ == "__main__":
    app()
