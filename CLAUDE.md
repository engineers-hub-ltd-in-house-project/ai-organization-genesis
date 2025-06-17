# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Organization Genesis is a multi-agent AI orchestration system that simulates a software development team using Claude Code and tmux. The system manages 6 specialized AI agents (CEO, CTO, Frontend, Backend, DevOps, QA) that collaborate on software projects.

## Common Commands

### Initial Setup
```bash
# Generate AI organization structure (run once)
./ai-org-genesis.sh

# Install Python dependencies
pip install -r requirements.txt
```

### Daily Operations
```bash
# Start AI organization with all agents
./ai-org-master.sh start

# Stop AI organization
./ai-org-master.sh stop

# Attach to running tmux session
./ai-org-master.sh attach
```

### Project Management
```bash
# Create new project workflow (run in Control Center window)
cd ai-org
python3 ai-collaboration-system.py create-workflow --project "project-name" --type "web-app"
# Project types: web-app, api, cli-tool

# Generate daily standup report
python3 ai-collaboration-system.py standup
```

### tmux Navigation
- Switch windows: `Ctrl+B` → `0-7`
- Detach from session: `Ctrl+B` → `d`
- Scroll mode: `Ctrl+B` → `[` (exit with `q`)

### Window Layout
- 0: Control Center (project management)
- 1: AI-CEO (strategy/requirements)
- 2: AI-CTO (architecture/review)
- 3: AI-Frontend (UI/UX)
- 4: AI-Backend (API/server)
- 5: AI-DevOps (infrastructure)
- 6: AI-QA (testing/quality)
- 7: Monitor (real-time dashboard)

## Architecture

### Core Components

1. **ai-collaboration-system.py**: Main workflow engine that creates tasks and manages project workflows. Key methods:
   - `create_project_workflow()`: Generates task distribution for different project types
   - `create_task()`: Creates individual tasks for agents
   - `assign_tasks_to_agents()`: Distributes tasks based on agent specialization

2. **claude-code-agent.py**: Individual AI agent implementation with command loop for task execution

3. **message-bus.py**: Inter-agent communication system for collaboration

4. **monitor-dashboard.py**: Real-time monitoring using Python curses library

### Directory Structure

- `ai-org/config/`: Organization configuration (organization.json)
- `ai-org/personas/`: AI personality definitions (YAML files)
- `ai-org/agents/`: Individual agent workspaces
- `ai-org/communication/`: Message passing and task management
  - `messages/`: Inter-agent messages
  - `tasks/`: JSON task files for each agent
  - `reports/`: Progress reports
- `ai-org/workspace/`: Project files and shared resources
- `ai-org/knowledge/templates/`: Project scaffolding templates

### Task System

Tasks are JSON files stored in `ai-org/communication/tasks/{agent_name}_tasks.json` with structure:
```json
{
  "id": "unique-id",
  "title": "Task Title",
  "description": "Detailed description",
  "assigned_to": "agent-name",
  "status": "pending|in_progress|completed",
  "priority": "high|medium|low"
}
```

### Agent Communication

Agents communicate through:
1. Task files in `communication/tasks/`
2. Message files in `communication/messages/`
3. Shared workspace in `workspace/projects/`

## Development Notes

- Python 3.8+ required, minimal dependencies (mainly standard library)
- No formal test framework - testing is manual or through AI agents
- Windows users need `windows-curses` for the monitoring dashboard
- The system uses tmux for session management - ensure tmux is installed
- Each agent runs in its own tmux window with independent Python process