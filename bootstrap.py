#!/usr/bin/env python3
"""
SpecPilot Bootstrap Script

This script installs the SpecPilot framework into a new or existing project.
It provides both interactive and fast modes for project setup.

Usage:
    python3 bootstrap.py init                    # Interactive mode
    python3 bootstrap.py init --fast --title "Project Name"  # Fast mode
"""

import os
import sys
import shutil
import json
import subprocess
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class SpecPilotBootstrap:
    """Main bootstrap class for installing SpecPilot framework."""
    
    def __init__(self, target_directory: str = None):
        if target_directory:
            self.project_root = Path(target_directory).resolve()
        else:
            self.project_root = Path.cwd()
        
        self.framework_root = Path(__file__).parent
        self.specpilot_dir = self.project_root / ".specpilot"
        self.engine_dir = self.specpilot_dir / "engine"
        self.workspace_dir = self.specpilot_dir / "workspace"
        
        # Colors for terminal output
        self.colors = {
            'reset': '\033[0m',
            'bold': '\033[1m',
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m'
        }
    
    def print_banner(self):
        """Display the SpecPilot welcome banner."""
        banner = f"""
{self.colors['bold']}{self.colors['blue']}
╔══════════════════════════════════════════════════════════════╗
║                    🚀 SpecPilot Framework                   ║
║                                                              ║
║              AI Speed. Engineered Discipline.               ║
║                                                              ║
║        Transforming AI coding from chaos to clarity         ║
╚══════════════════════════════════════════════════════════════╝
{self.colors['reset']}
"""
        print(banner)
    
    def print_step(self, step: str, message: str):
        """Print a formatted step message."""
        print(f"{self.colors['bold']}{self.colors['green']}✅ {step}{self.colors['reset']} {message}")
    
    def print_warning(self, message: str):
        """Print a formatted warning message."""
        print(f"{self.colors['bold']}{self.colors['yellow']}⚠️  {message}{self.colors['reset']}")
    
    def print_error(self, message: str):
        """Print a formatted error message."""
        print(f"{self.colors['bold']}{self.colors['red']}❌ {message}{self.colors['reset']}")
    
    def print_info(self, message: str):
        """Print a formatted info message."""
        print(f"{self.colors['cyan']}ℹ️  {message}{self.colors['reset']}")
    
    def validate_environment(self) -> bool:
        """Validate the current environment for installation."""
        print(f"{self.colors['bold']}🚦 Validating environment...{self.colors['reset']}")
        
        # Check Python version
        if sys.version_info < (3, 7):
            self.print_error("Python 3.7 or higher is required.")
            return False
        
        # Check if .specpilot already exists
        if self.specpilot_dir.exists():
            self.print_warning(".specpilot directory already exists.")
            response = input("Overwrite existing installation? (y/N): ").strip().lower()
            if response != 'y':
                self.print_info("Installation cancelled.")
                return False
        
        # Check if directory is writable
        if not os.access(self.project_root, os.W_OK):
            self.print_error("Target directory is not writable.")
            return False
        
        self.print_step("Environment", "Validation passed")
        return True
    
    def get_user_info(self) -> Dict[str, str]:
        """Get user information interactively."""
        print(f"\n{self.colors['bold']}👤 User Configuration{self.colors['reset']}")
        
        # Get username
        git_user = self.get_git_user()
        username = input(f"Username [{git_user}]: ").strip() or git_user
        
        # Get project title
        project_title = input("Project title: ").strip()
        if not project_title:
            project_title = self.project_root.name
        
        # Get project description
        project_desc = input("Project description (optional): ").strip()
        
        return {
            'username': username,
            'project_title': project_title,
            'project_desc': project_desc
        }
    
    def get_git_user(self) -> str:
        """Get Git username from configuration."""
        try:
            result = subprocess.run(
                ['git', 'config', 'user.name'],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip() or 'developer'
        except (subprocess.CalledProcessError, FileNotFoundError):
            return 'developer'
    
    def get_development_philosophy(self) -> str:
        """Get user's development philosophy preference."""
        print(f"\n{self.colors['bold']}🏗️  Development Philosophy{self.colors['reset']}")
        print("Choose your development approach:")
        print("1. 🥇 Enterprise Scale - Strict rules, security focus, TDD")
        print("2. 🦄 Scalable MVP - Solid foundations, growth-oriented")
        print("3. 🍄 Vibe Time - Minimal conventions, flexible approach")
        
        while True:
            choice = input("Select (1-3) [2]: ").strip() or "2"
            if choice in ['1', '2', '3']:
                philosophies = {
                    '1': 'enterprise',
                    '2': 'scalable',
                    '3': 'vibe'
                }
                return philosophies[choice]
            print("Please select 1, 2, or 3.")
    
    def get_architecture_goal(self) -> str:
        """Get user's architectural goal preference."""
        print(f"\n{self.colors['bold']}🏛️  Architecture Goals{self.colors['reset']}")
        print("Choose your primary architectural goal:")
        print("1. 🥇 Enterprise Scale - High security and reliability from day one")
        print("2. 🦄 Scalable MVP - Build a solid foundation that can grow")
        print("3. 🍄 Vibe Time - No formal architecture, just get it working")
        
        while True:
            choice = input("Select (1-3) [2]: ").strip() or "2"
            if choice in ['1', '2', '3']:
                goals = {
                    '1': 'enterprise',
                    '2': 'scalable',
                    '3': 'vibe'
                }
                return goals[choice]
            print("Please select 1, 2, or 3.")
    
    def get_notepad_preference(self) -> str:
        """Get user's notepad summary preference."""
        print(f"\n{self.colors['bold']}📝 Notepad Configuration{self.colors['reset']}")
        print("How would you like your notepad summarized?")
        print("1. one-line - Brief summary after each command")
        print("2. verbose - Detailed summary after each command")
        print("3. none - No automatic summary")
        
        while True:
            choice = input("Select (1-3) [1]: ").strip() or "1"
            if choice in ['1', '2', '3']:
                preferences = {
                    '1': 'one-line',
                    '2': 'verbose',
                    '3': 'none'
                }
                return preferences[choice]
            print("Please select 1, 2, or 3.")
    
    def get_commit_intelligence(self) -> bool:
        """Get user's commit intelligence preference."""
        print(f"\n{self.colors['bold']}🎁 Commit Intelligence{self.colors['reset']}")
        print("Enable SpecPilot's intelligent commit analysis?")
        print("This provides development intelligence scores and session analytics.")
        
        response = input("Enable commit intelligence? (Y/n): ").strip().lower()
        return response != 'n'
    
    def create_directory_structure(self):
        """Create the complete directory structure."""
        print(f"\n{self.colors['bold']}📁 Creating directory structure...{self.colors['reset']}")
        
        directories = [
            self.specpilot_dir,
            self.engine_dir,
            self.workspace_dir,
            self.project_root / "docs" / "plans",
            self.project_root / "docs" / "specs",
            self.project_root / "src",
            self.project_root / "tests",
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            self.print_step("Directory", f"Created {directory}")
    
    def copy_framework_files(self):
        """Copy the SpecPilot framework files."""
        print(f"\n{self.colors['bold']}🔧 Installing SpecPilot framework...{self.colors['reset']}")
        
        # Copy engine directory
        if (self.framework_root / ".specpilot" / "engine").exists():
            source_engine = self.framework_root / ".specpilot" / "engine"
            shutil.copytree(source_engine, self.engine_dir, dirs_exist_ok=True)
            self.print_step("Framework", "Engine files copied")
        else:
            self.print_error("SpecPilot engine not found in framework directory")
            return False
        
        return True
    
    def create_user_workspace(self, username: str):
        """Create user-specific workspace."""
        print(f"\n{self.colors['bold']}👤 Setting up user workspace...{self.colors['reset']}")
        
        user_workspace = self.workspace_dir / username
        user_workspace.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories
        (user_workspace / "config").mkdir(exist_ok=True)
        (user_workspace / "logs").mkdir(exist_ok=True)
        (user_workspace / "notepad").mkdir(exist_ok=True)
        
        self.print_step("Workspace", f"Created for user '{username}'")
        return user_workspace
    
    def create_config_files(self, user_workspace: Path, username: str, preferences: Dict):
        """Create configuration files."""
        print(f"\n{self.colors['bold']}⚙️  Creating configuration files...{self.colors['reset']}")
        
        # Create .specpilot.local
        local_config = {
            "username": username,
            "workspace_path": f".specpilot/workspace/{username}"
        }
        
        with open(self.project_root / ".specpilot.local", "w") as f:
            json.dump(local_config, f, indent=2)
        
        # Create user config
        user_config = {
            "_description": f"Project-specific configuration for {username}",
            "logging": {
                "verbose_mode": True,
                "notepad_summary": preferences.get('notepad_summary', 'one-line'),
                "track_model": True
            },
            "commitconfiguration": {
                "commit_intelligence": preferences.get('commit_intelligence', True),
                "session_analytics": True,
                "frustration_scoring": True,
                "productivity_metrics": True
            }
        }
        
        with open(user_workspace / "config" / "config.json", "w") as f:
            json.dump(user_config, f, indent=2)
        
        self.print_step("Configuration", "Files created")
    
    def create_documentation_templates(self, project_title: str, project_desc: str, philosophy: str, architecture: str):
        """Create documentation template files."""
        print(f"\n{self.colors['bold']}📚 Creating documentation templates...{self.colors['reset']}")
        
        # Create README.md
        readme_content = f"""# {project_title}

{project_desc or "A project built with SpecPilot framework."}

## Getting Started

This project uses the SpecPilot framework for AI-powered, spec-driven development.

### Development Modes

- **🚦 Initialization Mode**: Project startup and validation
- **🤖 Pilot Mode**: Systematic development guidance
- **🏛️ Architecture Mode**: Collaborative architectural design
- **🎨 Design Mode**: Specification creation
- **📐 Spec Mode**: Implementation and testing
- **🍄 Vibe Mode**: Debugging and troubleshooting
- **🕵️ Deep Check Mode**: Quality assurance
- **🎁 Commit Mode**: Intelligent commit analysis

### Quick Start

1. Open Cursor IDE in this project
2. Create a new mode with SpecPilot instructions
3. Say "Enter Pilot Mode" to begin guided development

## Project Structure

- `docs/plans/` - Product, architecture, and technical roadmaps
- `docs/specs/` - Feature specifications
- `src/` - Source code
- `tests/` - Test files
- `.specpilot/` - Framework configuration and workspace

## Development Philosophy

**{philosophy.title()}** approach with **{architecture.title()}** architecture goals.

For more information, see the [SpecPilot documentation](https://github.com/specpilot/framework).
"""
        
        with open(self.project_root / "README.md", "w") as f:
            f.write(readme_content)
        
        # Create other template files
        self.create_template_file("docs/plans/product_roadmap.md", "product_roadmap")
        self.create_template_file("docs/plans/architecture.md", "architecture")
        self.create_template_file("docs/plans/technical_roadmap.md", "technical_roadmap")
        self.create_template_file("docs/project_conventions.md", "project_conventions")
        
        self.print_step("Documentation", "Templates created")
    
    def create_template_file(self, filepath: str, template_type: str):
        """Create a template file from the engine templates."""
        template_source = self.engine_dir / "templates" / f"{template_type}.md"
        if template_source.exists():
            shutil.copy2(template_source, self.project_root / filepath)
    
    def create_notepad(self, user_workspace: Path):
        """Create the user's notepad file."""
        notepad_file = user_workspace / "notepad" / "note.md"
        
        notepad_content = """# Development Notes

---

## Ideas
*Add your ideas here*

## To Do List
*Add your tasks here*

## Decisions to Make
*Add decisions that need to be made here*

## Other Notes
*Add other notes here*

---
_Use "Add to notepad:" to capture content | Use "Organize Notepad" to clean up_
"""
        
        with open(notepad_file, "w") as f:
            f.write(notepad_content)
        
        self.print_step("Notepad", "Initialized")
    
    def create_gitignore(self):
        """Create .gitignore file."""
        gitignore_content = """# SpecPilot
.specpilot.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
"""
        
        with open(self.project_root / ".gitignore", "w") as f:
            f.write(gitignore_content)
        
        self.print_step("Files", ".gitignore created (useful even without Git)")
    
    def create_requirements_txt(self):
        """Create requirements.txt file."""
        requirements_content = """# Project dependencies
# Add your Python package requirements here
"""
        
        with open(self.project_root / "requirements.txt", "w") as f:
            f.write(requirements_content)
        
        self.print_step("Dependencies", "requirements.txt created")
    
    def run_interactive_mode(self):
        """Run the interactive bootstrap mode."""
        print(f"{self.colors['bold']}🌱 Interactive Bootstrap Mode{self.colors['reset']}")
        
        # Validate environment
        if not self.validate_environment():
            return False
        
        # Get user information
        user_info = self.get_user_info()
        philosophy = self.get_development_philosophy()
        architecture = self.get_architecture_goal()
        notepad_pref = self.get_notepad_preference()
        commit_intel = self.get_commit_intelligence()
        
        preferences = {
            'notepad_summary': notepad_pref,
            'commit_intelligence': commit_intel
        }
        
        # Show installation plan
        print(f"\n{self.colors['bold']}📋 Installation Plan{self.colors['reset']}")
        print(f"Project: {user_info['project_title']}")
        print(f"Username: {user_info['username']}")
        print(f"Philosophy: {philosophy.title()}")
        print(f"Architecture: {architecture.title()}")
        print(f"Notepad: {notepad_pref}")
        print(f"Commit Intelligence: {'Yes' if commit_intel else 'No'}")
        
        response = input("\nProceed with installation? (Y/n): ").strip().lower()
        if response == 'n':
            self.print_info("Installation cancelled.")
            return False
        
        # Execute installation
        return self.execute_installation(user_info, preferences)
    
    def run_fast_mode(self, project_title: str):
        """Run the fast bootstrap mode."""
        print(f"{self.colors['bold']}⚡ Fast Bootstrap Mode{self.colors['reset']}")
        
        # Validate environment
        if not self.validate_environment():
            return False
        
        # Use defaults
        username = self.get_git_user()
        user_info = {
            'username': username,
            'project_title': project_title,
            'project_desc': f"A {project_title} project built with SpecPilot framework."
        }
        
        preferences = {
            'notepad_summary': 'one-line',
            'commit_intelligence': True
        }
        
        print(f"Using defaults:")
        print(f"  Project: {project_title}")
        print(f"  Username: {username}")
        print(f"  Philosophy: Scalable")
        print(f"  Architecture: Scalable")
        
        # Execute installation
        return self.execute_installation(user_info, preferences)
    
    def execute_installation(self, user_info: Dict[str, str], preferences: Dict) -> bool:
        """Execute the complete installation process."""
        try:
            # Create directory structure
            self.create_directory_structure()
            
            # Copy framework files
            if not self.copy_framework_files():
                return False
            
            # Create user workspace
            user_workspace = self.create_user_workspace(user_info['username'])
            
            # Create configuration files
            self.create_config_files(user_workspace, user_info['username'], preferences)
            
            # Create documentation templates
            self.create_documentation_templates(
                user_info['project_title'],
                user_info['project_desc'],
                'scalable',  # Default for fast mode
                'scalable'   # Default for fast mode
            )
            
            # Create notepad
            self.create_notepad(user_workspace)
            
            # Create project files
            self.create_gitignore()
            self.create_requirements_txt()
            
            # Success message
            print(f"\n{self.colors['bold']}{self.colors['green']}🎉 SpecPilot installation complete!{self.colors['reset']}")
            print(f"\nNext steps:")
            print(f"1. Open Cursor IDE in this project")
            print(f"2. Create a new mode with SpecPilot instructions")
            print(f"3. Say 'Enter Pilot Mode' to begin guided development")
            print(f"\nYour workspace is ready at: .specpilot/workspace/{user_info['username']}/")
            print(f"\nOptional: Run 'git init' if you want version control for this project")
            
            return True
            
        except Exception as e:
            self.print_error(f"Installation failed: {str(e)}")
            return False
    
    @staticmethod
    def run():
        """Main entry point for the bootstrap script."""
        parser = argparse.ArgumentParser(
            description="SpecPilot Framework Bootstrap Script",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  python3 bootstrap.py /path/to/project                    # Interactive mode
  python3 bootstrap.py /path/to/project --fast --title "My Project"  # Fast mode
  python3 bootstrap.py /path/to/project init               # Interactive mode (explicit)

Note: The target directory does not need to be a Git repository.
SpecPilot will work in any writable directory.
            """
        )
        
        parser.add_argument(
            'target_directory',
            type=str,
            help='Target directory where SpecPilot should be installed'
        )
        
        parser.add_argument(
            'command',
            nargs='?',
            default='init',
            choices=['init'],
            help='Bootstrap command (init, optional, defaults to init)'
        )
        
        parser.add_argument(
            '--fast',
            action='store_true',
            help='Run in fast mode (non-interactive)'
        )
        
        parser.add_argument(
            '--title',
            type=str,
            help='Project title for fast mode'
        )
        
        args = parser.parse_args()
        
        # Validate target directory
        target_path = Path(args.target_directory).resolve()
        if not target_path.exists():
            print(f"❌ Target directory does not exist: {target_path}")
            sys.exit(1)
        
        if not target_path.is_dir():
            print(f"❌ Target must be a directory: {target_path}")
            sys.exit(1)
        
        # Initialize bootstrap with target directory
        bootstrap = SpecPilotBootstrap(str(target_path))
        bootstrap.print_banner()
        
        if args.fast:
            if not args.title:
                print("❌ --title is required for fast mode")
                sys.exit(1)
            success = bootstrap.run_fast_mode(args.title)
        else:
            success = bootstrap.run_interactive_mode()
        
        if not success:
            sys.exit(1)


if __name__ == "__main__":
    SpecPilotBootstrap.run() 