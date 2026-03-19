#!/usr/bin/env python3
"""
world-os CLI - Worldbuilding Framework Command Line Interface
"""
import sys
import os
import argparse
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def main():
    parser = argparse.ArgumentParser(
        prog='world-os',
        description='Worldbuilding Framework CLI'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # list command
    list_parser = subparsers.add_parser('list', help='List all projects')
    
    # show command
    show_parser = subparsers.add_parser('show', help='Show project details')
    show_parser.add_argument('project_id', help='Project ID')
    
    # create command
    create_parser = subparsers.add_parser('create', help='Create new project')
    create_parser.add_argument('name', help='Project name')
    create_parser.add_argument('--type', choices=['novel', 'game', 'ttrpg', 'screenplay', 'other'], default='other')
    create_parser.add_argument('--description', help='Project description')
    
    # serve command
    serve_parser = subparsers.add_parser('serve', help='Start API server')
    serve_parser.add_argument('--port', type=int, default=8000)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    # Import commands only when needed
    if args.command == 'list':
        from cli.commands.list import list_projects
        return list_projects()
    elif args.command == 'show':
        from cli.commands.show import show_project
        return show_project(args.project_id)
    elif args.command == 'create':
        from cli.commands.create import create_project
        return create_project(args.name, args.type, args.description)
    elif args.command == 'serve':
        from cli.commands.serve import serve
        return serve(args.port)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
