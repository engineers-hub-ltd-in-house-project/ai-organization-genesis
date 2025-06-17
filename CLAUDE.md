# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Organization Genesis is an AI collaborative development system that runs within Claude Code. A single AI instance role-plays as 6 specialized agents (CEO, CTO, Frontend, Backend, DevOps, QA) to automatically develop complete software projects with real code generation.

## Common Commands

### Running Projects

```bash
# Navigate to the ai-org directory
cd ai-org

# Run a demo project with progress monitoring
python3 ai-collaborative-system.py

# Create and execute a custom project
python3 -c "
from ai_collaborative_system import AICollaborativeSystem
system = AICollaborativeSystem()
system.create_project('my-app', 'web-app')
system.execute_project('my-app', show_progress=True)
"

# Monitor project status
python3 -c "
from ai_collaborative_system import AICollaborativeSystem
system = AICollaborativeSystem()
system.monitor_project('my-app')
"
```

### Project Types
- `web-app`: Full-stack web application (React + Node.js + Docker)
- `api`: REST API service (planned)
- `cli-tool`: Command-line tool (planned)

## Architecture

### Core System

**ai-collaborative-system.py** - Single-file system containing:
- `AICollaborativeSystem`: Main orchestrator class
- `Task`, `TaskStatus`, `AgentRole`: Data models
- Agent role implementations (`_execute_ceo_task`, `_execute_cto_task`, etc.)
- Progress monitoring and reporting functions

### Key Methods

- `create_project(project_name, project_type)`: Creates project and generates tasks
- `execute_project(project_name, show_progress=True)`: Executes all project tasks
- `monitor_project(project_name)`: Displays project status and progress
- `get_project_status(project_name)`: Returns project status as dict

### Agent Roles and Outputs

Each agent produces specific artifacts:

- **CEO**: `docs/requirements.md`
- **CTO**: `docs/architecture.md`
- **Frontend**: React components in `src/`
- **Backend**: Express server in `backend/`
- **DevOps**: `Dockerfile`, `docker-compose.yml`, CI/CD configs
- **QA**: Test files in `tests/` and `cypress/`

### Directory Structure

```
ai-org/
├── ai-collaborative-system.py  # Main system (only required file)
├── workspace/                  # Generated projects (gitignored)
│   └── projects/
│       └── [project-name]/
├── communication/              # System state (gitignored)
│   ├── tasks/                 # Task JSON files
│   └── reports/               # Project summaries
└── logs/                      # System logs (gitignored)
```

## Development Notes

- No external dependencies - uses Python standard library only
- Runs entirely within Claude Code environment
- Cannot recursively call Claude Code SDK
- All generated projects are in `workspace/projects/` (gitignored)
- Task files use timestamp-based IDs: `task_{timestamp}_{role}.json`

## Extending the System

To add new project types or agent capabilities:

1. Add project type in `create_project()` method
2. Implement corresponding `_execute_[role]_task()` methods
3. Update `agent_capabilities` dictionary for new skills

Example:
```python
def _execute_mobile_task(self, task: Task, project_dir: Path):
    """Mobile development task implementation"""
    # Generate React Native or Flutter code
    pass
```