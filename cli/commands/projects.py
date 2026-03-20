import typer
from .list import list_projects as list_cmd
from .show import show_project as show_cmd
from .create import create_project as create_cmd

app = typer.Typer(help="Manage projects")


@app.command("list")
def list_projects():
    """List all projects"""
    list_cmd()


@app.command("show")
def show_project(project_id: str):
    """Show project details"""
    show_cmd(project_id)


@app.command("create")
def create_project(
    name: str,
    type: str = typer.Option("other", help="Project type"),
    description: str = typer.Option("", help="Project description")
):
    """Create new project"""
    create_cmd(name, type, description)


if __name__ == "__main__":
    app()
