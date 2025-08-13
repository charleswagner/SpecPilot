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
        self.backup_dir = self.specpilot_dir / "backups"
        
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
    
    def create_backup(self) -> Optional[str]:
        """Create a backup of the current engine files."""
        if not self.engine_dir.exists():
            self.print_error("No existing SpecPilot installation found to backup.")
            return None
            
        # Create backup directory if it doesn't exist
        self.backup_dir.mkdir(exist_ok=True)
        
        # Generate timestamp for backup
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"engine_backup_{timestamp}"
        backup_path = self.backup_dir / backup_name
        
        try:
            # Copy engine directory to backup
            shutil.copytree(self.engine_dir, backup_path, dirs_exist_ok=True)
            self.print_step("Backup", f"Created: {backup_name}")
            return str(backup_path)
        except Exception as e:
            self.print_error(f"Backup creation failed: {str(e)}")
            return None
    
    def cleanup_old_backups(self, keep_count: int = 3):
        """Remove old backups, keeping only the specified number."""
        if not self.backup_dir.exists():
            return
            
        try:
            # Get all backup directories sorted by creation time (oldest first)
            backups = []
            for item in self.backup_dir.iterdir():
                if item.is_dir() and item.name.startswith("engine_backup_"):
                    backups.append((item.stat().st_ctime, item))
            
            backups.sort()  # Sort by creation time
            
            # Remove old backups
            if len(backups) > keep_count:
                for _, backup_path in backups[:-keep_count]:
                    shutil.rmtree(backup_path)
                    if hasattr(self, 'verbose') and self.verbose:
                        self.print_info(f"Removed old backup: {backup_path.name}")
        except Exception as e:
            self.print_warning(f"Backup cleanup failed: {str(e)}")
    
    def check_version_compatibility(self) -> bool:
        """Check if the update is compatible with the current installation."""
        # For now, assume compatibility (can be enhanced later)
        # This could check version files, configuration compatibility, etc.
        return True
    
    def update_engine_files(self, dry_run: bool = False) -> bool:
        """Update the engine files from the current framework."""
        try:
            if dry_run:
                self.print_info("🔍 DRY RUN MODE - No files will be modified")
            
            # Get source engine files from current framework
            source_engine = self.framework_root / ".specpilot" / "engine"
            if not source_engine.exists():
                self.print_error("Source engine files not found in current framework.")
                return False
            
            # List files that would be updated
            files_to_update = []
            for item in source_engine.rglob("*"):
                if item.is_file():
                    relative_path = item.relative_to(source_engine)
                    target_path = self.engine_dir / relative_path
                    files_to_update.append((str(item), str(target_path)))
            
            if dry_run:
                self.print_info(f"Would update {len(files_to_update)} engine files:")
                for source, target in files_to_update[:5]:  # Show first 5
                    self.print_info(f"  {target}")
                if len(files_to_update) > 5:
                    self.print_info(f"  ... and {len(files_to_update) - 5} more files")
                return True
            
            # Actually perform the update
            updated_count = 0
            for source, target in files_to_update:
                target_path = Path(target)
                target_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
                updated_count += 1
                
                if hasattr(self, 'verbose') and self.verbose:
                    self.print_info(f"Updated: {target}")
            
            self.print_step("Update", f"Successfully updated {updated_count} engine files")
            return True
            
        except Exception as e:
            self.print_error(f"Engine update failed: {str(e)}")
            return False
    
    def rollback_update(self, backup_path: str) -> bool:
        """Rollback to a previous backup."""
        try:
            backup_dir = Path(backup_path)
            if not backup_dir.exists():
                self.print_error(f"Backup not found: {backup_path}")
                return False
            
            # Remove current engine
            if self.engine_dir.exists():
                shutil.rmtree(self.engine_dir)
            
            # Restore from backup
            shutil.copytree(backup_dir, self.engine_dir)
            self.print_step("Rollback", f"Successfully restored from backup: {backup_dir.name}")
            return True
            
        except Exception as e:
            self.print_error(f"Rollback failed: {str(e)}")
            return False
    
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
    
    def run_update_mode(self, args) -> bool:
        """Run the bootstrap update mode."""
        print(f"{self.colors['bold']}🔄 Bootstrap Update Mode{self.colors['reset']}")
        
        # Check if SpecPilot is already installed
        if not self.specpilot_dir.exists():
            self.print_error("No SpecPilot installation found in this project.")
            self.print_info("Use 'init' command to install SpecPilot first.")
            return False
        
        if not self.engine_dir.exists():
            self.print_error("SpecPilot engine directory not found.")
            return False
        
        # Set verbose mode if requested
        self.verbose = args.verbose
        
        # Check version compatibility
        if not self.check_version_compatibility():
            self.print_error("Version compatibility check failed.")
            return False
        
        # Show update plan
        print(f"\n{self.colors['bold']}📋 Update Plan{self.colors['reset']}")
        print(f"Project: {self.project_root.name}")
        print(f"Current Engine: {self.engine_dir}")
        print(f"Source Engine: {self.framework_root / '.specpilot' / 'engine'}")
        print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE UPDATE'}")
        print(f"Backup Retention: Keep last {args.keep_backups} backups")
        
        if not args.force:
            response = input("\nProceed with update? (Y/n): ").strip().lower()
            if response == 'n':
                self.print_info("Update cancelled.")
                return False
        
        # Create backup before update
        backup_path = self.create_backup()
        if not backup_path:
            self.print_error("Failed to create backup. Update cancelled.")
            return False
        
        # Perform the update
        if not self.update_engine_files(args.dry_run):
            self.print_error("Update failed. Rolling back...")
            if self.rollback_update(backup_path):
                self.print_info("Successfully rolled back to previous version.")
            else:
                self.print_error("Rollback failed. Manual intervention required.")
            return False
        
        # Cleanup old backups
        self.cleanup_old_backups(args.keep_backups)
        
        if args.dry_run:
            self.print_info("🔍 DRY RUN COMPLETE - No changes were made")
        else:
            self.print_step("Update", "SpecPilot framework updated successfully!")
            self.print_info(f"Backup saved at: {backup_path}")
            self.print_info("Your project workspace and configuration are preserved.")
        
        return True
    
    def run_rollback_mode(self, args) -> bool:
        """Run the rollback mode to restore from a backup."""
        print(f"{self.colors['bold']}⏪ Rollback Mode{self.colors['reset']}")
        
        if not self.backup_dir.exists():
            self.print_error("No backups found.")
            return False
        
        # List available backups
        backups = []
        for item in self.backup_dir.iterdir():
            if item.is_dir() and item.name.startswith("engine_backup_"):
                backups.append(item)
        
        if not backups:
            self.print_error("No engine backups found.")
            return False
        
        # Sort backups by creation time (newest first)
        backups.sort(key=lambda x: x.stat().st_ctime, reverse=True)
        
        print(f"\n{self.colors['bold']}📋 Available Backups{self.colors['reset']}")
        for i, backup in enumerate(backups):
            ctime = backup.stat().st_ctime
            from datetime import datetime
            date_str = datetime.fromtimestamp(ctime).strftime("%Y-%m-%d %H:%M:%S")
            print(f"{i+1}. {backup.name} ({date_str})")
        
        if not args.force:
            choice = input(f"\nSelect backup to restore (1-{len(backups)}): ").strip()
            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(backups):
                    selected_backup = backups[choice_idx]
                else:
                    self.print_error("Invalid selection.")
                    return False
            except ValueError:
                self.print_error("Invalid input. Please enter a number.")
                return False
        else:
            # Use most recent backup
            selected_backup = backups[0]
            self.print_info(f"Auto-selected most recent backup: {selected_backup.name}")
        
        # Confirm rollback
        if not args.force:
            response = input(f"\nRestore from {selected_backup.name}? This will overwrite current engine. (y/N): ").strip().lower()
            if response != 'y':
                self.print_info("Rollback cancelled.")
                return False
        
        # Perform rollback
        if self.rollback_update(str(selected_backup)):
            self.print_step("Rollback", "Successfully restored from backup!")
            return True
        else:
            self.print_error("Rollback failed.")
            return False
    
    def run_cleanup_backups_mode(self, args) -> bool:
        """Run the backup cleanup mode."""
        print(f"{self.colors['bold']}🧹 Backup Cleanup Mode{self.colors['reset']}")
        
        if not self.backup_dir.exists():
            self.print_info("No backup directory found.")
            return True
        
        # Count current backups
        backups = []
        for item in self.backup_dir.iterdir():
            if item.is_dir() and item.name.startswith("engine_backup_"):
                backups.append(item)
        
        if not backups:
            self.print_info("No backups to clean up.")
            return True
        
        print(f"Found {len(backups)} backups.")
        print(f"Will keep {args.keep_backups} most recent backups.")
        
        if not args.force:
            response = input(f"Remove {len(backups) - args.keep_backups} old backups? (y/N): ").strip().lower()
            if response != 'y':
                self.print_info("Cleanup cancelled.")
                return True
        
        # Perform cleanup
        self.cleanup_old_backups(args.keep_backups)
        
        # Count remaining backups
        remaining = []
        for item in self.backup_dir.iterdir():
            if item.is_dir() and item.name.startswith("engine_backup_"):
                remaining.append(item)
        
        self.print_step("Cleanup", f"Successfully cleaned up backups. {len(remaining)} backups remaining.")
        return True
    
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
  python3 bootstrap.py /path/to/project update             # Update framework
  python3 bootstrap.py /path/to/project update --dry-run   # Simulate update
  python3 bootstrap.py /path/to/project update --verbose   # Verbose update
  python3 bootstrap.py /path/to/project rollback           # Rollback to backup
  python3 bootstrap.py /path/to/project cleanup-backups    # Clean old backups

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
            choices=['init', 'update', 'rollback', 'cleanup-backups'],
            help='Bootstrap command (init, update, rollback, cleanup-backups, optional, defaults to init)'
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
        
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Enable verbose output for update operations'
        )
        
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Simulate update without making changes (update mode only)'
        )
        
        parser.add_argument(
            '--force',
            action='store_true',
            help='Skip confirmation prompts (use with caution)'
        )
        
        parser.add_argument(
            '--keep-backups',
            type=int,
            default=3,
            help='Number of backups to keep (default: 3)'
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
        
        # Route to appropriate mode based on command
        if args.command == 'update':
            success = bootstrap.run_update_mode(args)
        elif args.command == 'rollback':
            success = bootstrap.run_rollback_mode(args)
        elif args.command == 'cleanup-backups':
            success = bootstrap.run_cleanup_backups_mode(args)
        elif args.command == 'init' or args.command is None:
            if args.fast:
                if not args.title:
                    print("❌ --title is required for fast mode")
                    sys.exit(1)
                success = bootstrap.run_fast_mode(args.title)
            else:
                success = bootstrap.run_interactive_mode()
        else:
            print(f"❌ Unknown command: {args.command}")
            sys.exit(1)
        
        if not success:
            sys.exit(1)


if __name__ == "__main__":
    SpecPilotBootstrap.run() 