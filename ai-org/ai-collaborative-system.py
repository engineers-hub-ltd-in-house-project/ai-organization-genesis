#!/usr/bin/env python3
"""
AI Collaborative Development System
Claude Code内で動作し、複数のAIエージェントの役割を演じながら協調的に開発を進めるシステム
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
import logging
from pathlib import Path

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class AgentRole(Enum):
    CEO = "ai-ceo"
    CTO = "ai-cto"
    FRONTEND = "ai-frontend"
    BACKEND = "ai-backend"
    DEVOPS = "ai-devops"
    QA = "ai-qa"

@dataclass
class Task:
    id: str
    title: str
    description: str
    assigned_to: AgentRole
    project: str
    status: TaskStatus
    priority: int
    dependencies: List[str] = None
    created_at: datetime = None
    updated_at: datetime = None
    result: Optional[Dict] = None

class AICollaborativeSystem:
    """
    Claude Code内で動作する協調型開発システム
    単一のClaude Codeインスタンスが複数のエージェントの役割を演じる
    """
    def __init__(self, workspace_dir: str = "."):
        self.workspace_dir = Path(workspace_dir)
        self.tasks: List[Task] = []
        self.projects: Dict[str, Dict] = {}
        self.current_role: Optional[AgentRole] = None
        
        # エージェントの能力定義
        self.agent_capabilities = {
            AgentRole.CEO: ["strategic_planning", "requirements_analysis", "project_coordination"],
            AgentRole.CTO: ["technical_architecture", "technology_selection", "code_review"],
            AgentRole.FRONTEND: ["react_development", "ui_design", "responsive_design"],
            AgentRole.BACKEND: ["api_development", "database_design", "microservices"],
            AgentRole.DEVOPS: ["docker", "kubernetes", "ci_cd", "monitoring"],
            AgentRole.QA: ["test_automation", "quality_assurance", "bug_detection"]
        }
        
        # ロギング設定
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - [%(levelname)s] %(message)s'
        )
        
        self._ensure_directories()
    
    def _ensure_directories(self):
        """必要なディレクトリを作成"""
        dirs = [
            self.workspace_dir / "workspace" / "projects",
            self.workspace_dir / "communication" / "tasks",
            self.workspace_dir / "communication" / "reports",
            self.workspace_dir / "logs"
        ]
        for dir_path in dirs:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def create_project(self, project_name: str, project_type: str = "web-app") -> List[Task]:
        """プロジェクトを作成してタスクを生成"""
        logging.info(f"🚀 Creating project: {project_name} (type: {project_type})")
        
        workflow_tasks = []
        
        if project_type == "web-app":
            # Web アプリケーションのワークフロー
            tasks_config = [
                (AgentRole.CEO, "Product Vision & Requirements", "Define product vision, user stories, and functional requirements", 1),
                (AgentRole.CTO, "Technical Architecture", "Design system architecture, select tech stack, and create technical specifications", 2),
                (AgentRole.FRONTEND, "Frontend Development", "Implement React components, UI/UX, and responsive design", 3),
                (AgentRole.BACKEND, "Backend Development", "Implement REST API, database models, and business logic", 3),
                (AgentRole.DEVOPS, "Infrastructure Setup", "Setup Docker containers, CI/CD pipeline, and deployment configuration", 4),
                (AgentRole.QA, "Testing & Quality", "Implement unit tests, integration tests, and E2E test automation", 5)
            ]
        else:
            tasks_config = []
        
        # タスクを作成
        for role, title, description, priority in tasks_config:
            task = Task(
                id=f"task_{int(datetime.now().timestamp())}_{role.value}",
                title=title,
                description=description,
                assigned_to=role,
                project=project_name,
                status=TaskStatus.PENDING,
                priority=priority,
                dependencies=[],
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            workflow_tasks.append(task)
            self.tasks.append(task)
            self._save_task(task)
        
        # プロジェクト情報を保存
        self.projects[project_name] = {
            'type': project_type,
            'created_at': datetime.now().isoformat(),
            'tasks': [t.id for t in workflow_tasks]
        }
        
        return workflow_tasks
    
    def _save_task(self, task: Task):
        """タスクをファイルに保存"""
        task_file = self.workspace_dir / "communication" / "tasks" / f"{task.id}.json"
        with open(task_file, 'w') as f:
            json.dump({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'assigned_to': task.assigned_to.value,
                'project': task.project,
                'status': task.status.value,
                'priority': task.priority,
                'dependencies': task.dependencies or [],
                'created_at': task.created_at.isoformat(),
                'updated_at': task.updated_at.isoformat(),
                'result': task.result
            }, f, indent=2)
    
    def switch_role(self, role: AgentRole):
        """エージェントの役割を切り替え"""
        self.current_role = role
        logging.info(f"🎭 Switching to role: {role.value}")
    
    def get_pending_tasks(self, role: AgentRole) -> List[Task]:
        """特定の役割の保留中タスクを取得"""
        return [t for t in self.tasks 
                if t.assigned_to == role and t.status == TaskStatus.PENDING]
    
    def execute_task(self, task: Task):
        """タスクを実行（実際のコード生成と実装）"""
        self.switch_role(task.assigned_to)
        
        logging.info(f"📋 {self.current_role.value} starting task: {task.title}")
        task.status = TaskStatus.IN_PROGRESS
        task.updated_at = datetime.now()
        self._save_task(task)
        
        # プロジェクトディレクトリを作成
        project_dir = self.workspace_dir / "workspace" / "projects" / task.project
        project_dir.mkdir(parents=True, exist_ok=True)
        
        # 役割に応じたアクションを実行
        try:
            if task.assigned_to == AgentRole.CEO:
                self._execute_ceo_task(task, project_dir)
            elif task.assigned_to == AgentRole.CTO:
                self._execute_cto_task(task, project_dir)
            elif task.assigned_to == AgentRole.FRONTEND:
                self._execute_frontend_task(task, project_dir)
            elif task.assigned_to == AgentRole.BACKEND:
                self._execute_backend_task(task, project_dir)
            elif task.assigned_to == AgentRole.DEVOPS:
                self._execute_devops_task(task, project_dir)
            elif task.assigned_to == AgentRole.QA:
                self._execute_qa_task(task, project_dir)
            
            task.status = TaskStatus.COMPLETED
            logging.info(f"✅ {self.current_role.value} completed task: {task.title}")
        except Exception as e:
            task.status = TaskStatus.FAILED
            task.result = {'error': str(e)}
            logging.error(f"❌ {self.current_role.value} failed task: {task.title} - {str(e)}")
        
        task.updated_at = datetime.now()
        self._save_task(task)
    
    def _show_progress_header(self, project_name: str, total_tasks: int):
        """プロジェクト進捗ヘッダーを表示"""
        print("\n" + "="*60)
        print(f"🚀 PROJECT: {project_name}")
        print(f"📊 Total Tasks: {total_tasks}")
        print("="*60 + "\n")
    
    def _show_task_progress(self, current: int, total: int, task: Task):
        """タスク進捗を表示"""
        progress = (current - 1) / total * 100
        bar_length = 30
        filled_length = int(bar_length * (current - 1) // total)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        
        print(f"\n[{bar}] {progress:.0f}% Complete")
        print(f"⚡ Task {current}/{total}: {task.title}")
        print(f"👤 Assigned to: {task.assigned_to.value}")
        print(f"🔄 Status: Starting...")
    
    def _show_task_completion(self, task: Task):
        """タスク完了状態を表示"""
        status_icon = "✅" if task.status == TaskStatus.COMPLETED else "❌"
        print(f"{status_icon} Status: {task.status.value}")
        if task.result and 'created_files' in task.result:
            print(f"📁 Created {len(task.result['created_files'])} files")
    
    def _show_project_completion(self, project_name: str):
        """プロジェクト完了状態を表示"""
        project_tasks = [t for t in self.tasks if t.project == project_name]
        completed = len([t for t in project_tasks if t.status == TaskStatus.COMPLETED])
        success_rate = (completed / len(project_tasks) * 100) if project_tasks else 0
        
        print("\n" + "="*60)
        print(f"🎉 PROJECT COMPLETED: {project_name}")
        print(f"📈 Success Rate: {success_rate:.0f}%")
        print(f"✅ Completed Tasks: {completed}/{len(project_tasks)}")
        print("="*60 + "\n")
    
    def get_project_status(self, project_name: str) -> Dict[str, Any]:
        """プロジェクトのステータスを取得"""
        project_tasks = [t for t in self.tasks if t.project == project_name]
        
        status_count = {status: 0 for status in TaskStatus}
        for task in project_tasks:
            status_count[task.status] += 1
        
        completed_tasks = [t for t in project_tasks if t.status == TaskStatus.COMPLETED]
        
        return {
            'project': project_name,
            'total_tasks': len(project_tasks),
            'completed_tasks': len(completed_tasks),
            'success_rate': (len(completed_tasks) / len(project_tasks) * 100) if project_tasks else 0,
            'status_breakdown': {s.value: c for s, c in status_count.items()},
            'tasks': [
                {
                    'id': t.id,
                    'title': t.title,
                    'assigned_to': t.assigned_to.value,
                    'status': t.status.value,
                    'priority': t.priority,
                    'created_files': t.result.get('created_files', []) if t.result else []
                }
                for t in project_tasks
            ]
        }
    
    def monitor_project(self, project_name: str):
        """プロジェクトの現在状態をモニタリング表示"""
        status = self.get_project_status(project_name)
        
        print("\n" + "="*60)
        print(f"📊 PROJECT MONITOR: {project_name}")
        print("="*60)
        print(f"Progress: {status['success_rate']:.0f}% ({status['completed_tasks']}/{status['total_tasks']} tasks)")
        print(f"\nStatus Breakdown:")
        for status_type, count in status['status_breakdown'].items():
            if count > 0:
                icon = {"completed": "✅", "in_progress": "🔄", "pending": "⏳", "failed": "❌"}.get(status_type, "❓")
                print(f"  {icon} {status_type}: {count}")
        
        print(f"\nTask Details:")
        for task in status['tasks']:
            status_icon = {"completed": "✅", "in_progress": "🔄", "pending": "⏳", "failed": "❌"}.get(task['status'], "❓")
            print(f"  {status_icon} [{task['assigned_to']}] {task['title']}")
            if task['created_files']:
                print(f"     📁 Files: {', '.join(task['created_files'])}")
        print("="*60 + "\n")
    
    def _execute_ceo_task(self, task: Task, project_dir: Path):
        """CEOタスクを実行"""
        # 要件定義書を作成
        docs_dir = project_dir / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        requirements_content = """# ToDo Application Requirements

## Vision
A modern, user-friendly task management application that helps users organize their daily activities efficiently.

## User Stories
1. As a user, I want to create new tasks with title and description
2. As a user, I want to mark tasks as complete/incomplete
3. As a user, I want to edit existing tasks
4. As a user, I want to delete tasks
5. As a user, I want to filter tasks by status (all/active/completed)
6. As a user, I want to see the count of remaining tasks

## Functional Requirements
- Create, Read, Update, Delete (CRUD) operations for tasks
- Task persistence using local storage or backend API
- Responsive design for mobile and desktop
- Clean and intuitive user interface
- Real-time updates without page refresh

## Non-Functional Requirements
- Performance: Page load time < 2 seconds
- Accessibility: WCAG 2.1 AA compliant
- Browser Support: Chrome, Firefox, Safari, Edge (latest versions)
- Security: Input validation and XSS protection
"""
        
        with open(docs_dir / "requirements.md", 'w') as f:
            f.write(requirements_content)
        
        task.result = {'created_files': ['docs/requirements.md']}
    
    def _execute_cto_task(self, task: Task, project_dir: Path):
        """CTOタスクを実行"""
        docs_dir = project_dir / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        architecture_content = """# Technical Architecture

## Technology Stack
- **Frontend**: React 18 with TypeScript
- **State Management**: React Context API
- **Styling**: Tailwind CSS
- **Build Tool**: Vite
- **Backend**: Node.js with Express (optional)
- **Database**: PostgreSQL / MongoDB (optional)
- **Testing**: Jest + React Testing Library
- **Deployment**: Docker + Vercel/Netlify

## Project Structure
```
todo-app/
├── src/
│   ├── components/
│   │   ├── TodoList.tsx
│   │   ├── TodoItem.tsx
│   │   ├── AddTodo.tsx
│   │   └── FilterBar.tsx
│   ├── contexts/
│   │   └── TodoContext.tsx
│   ├── hooks/
│   │   └── useTodos.ts
│   ├── types/
│   │   └── todo.ts
│   ├── App.tsx
│   └── main.tsx
├── tests/
├── public/
└── package.json
```

## API Design (if backend is implemented)
- GET /api/todos - Get all todos
- POST /api/todos - Create new todo
- PUT /api/todos/:id - Update todo
- DELETE /api/todos/:id - Delete todo
"""
        
        with open(docs_dir / "architecture.md", 'w') as f:
            f.write(architecture_content)
        
        task.result = {'created_files': ['docs/architecture.md']}
    
    def _execute_frontend_task(self, task: Task, project_dir: Path):
        """Frontendタスクを実行"""
        # Reactプロジェクト構造を作成
        src_dir = project_dir / "src"
        src_dir.mkdir(exist_ok=True)
        
        # TypeScript型定義
        types_dir = src_dir / "types"
        types_dir.mkdir(exist_ok=True)
        
        todo_type_content = """export interface Todo {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  createdAt: Date;
  updatedAt?: Date;
}

export type FilterType = 'all' | 'active' | 'completed';
"""
        
        with open(types_dir / "todo.ts", 'w') as f:
            f.write(todo_type_content)
        
        # メインAppコンポーネント
        app_content = """import React, { useState, useEffect } from 'react';
import { Todo, FilterType } from './types/todo';
import TodoList from './components/TodoList';
import AddTodo from './components/AddTodo';
import FilterBar from './components/FilterBar';
import './App.css';

function App() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [filter, setFilter] = useState<FilterType>('all');

  // Load todos from localStorage on mount
  useEffect(() => {
    const savedTodos = localStorage.getItem('todos');
    if (savedTodos) {
      setTodos(JSON.parse(savedTodos));
    }
  }, []);

  // Save todos to localStorage whenever they change
  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos));
  }, [todos]);

  const addTodo = (title: string, description?: string) => {
    const newTodo: Todo = {
      id: Date.now().toString(),
      title,
      description,
      completed: false,
      createdAt: new Date()
    };
    setTodos([...todos, newTodo]);
  };

  const toggleTodo = (id: string) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed, updatedAt: new Date() } : todo
    ));
  };

  const deleteTodo = (id: string) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  const editTodo = (id: string, title: string, description?: string) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, title, description, updatedAt: new Date() } : todo
    ));
  };

  const filteredTodos = todos.filter(todo => {
    if (filter === 'active') return !todo.completed;
    if (filter === 'completed') return todo.completed;
    return true;
  });

  const activeTodoCount = todos.filter(todo => !todo.completed).length;

  return (
    <div className="app">
      <header className="app-header">
        <h1>Todo App</h1>
        <p className="todo-count">{activeTodoCount} active tasks</p>
      </header>
      
      <main className="app-main">
        <AddTodo onAdd={addTodo} />
        <FilterBar currentFilter={filter} onFilterChange={setFilter} />
        <TodoList
          todos={filteredTodos}
          onToggle={toggleTodo}
          onDelete={deleteTodo}
          onEdit={editTodo}
        />
      </main>
    </div>
  );
}

export default App;
"""
        
        with open(src_dir / "App.tsx", 'w') as f:
            f.write(app_content)
        
        # コンポーネントディレクトリ
        components_dir = src_dir / "components"
        components_dir.mkdir(exist_ok=True)
        
        # AddTodoコンポーネント
        add_todo_content = """import React, { useState } from 'react';

interface AddTodoProps {
  onAdd: (title: string, description?: string) => void;
}

const AddTodo: React.FC<AddTodoProps> = ({ onAdd }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (title.trim()) {
      onAdd(title.trim(), description.trim() || undefined);
      setTitle('');
      setDescription('');
    }
  };

  return (
    <form className="add-todo-form" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="What needs to be done?"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="todo-input"
      />
      <input
        type="text"
        placeholder="Description (optional)"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        className="todo-input"
      />
      <button type="submit" className="add-button">Add Task</button>
    </form>
  );
};

export default AddTodo;
"""
        
        with open(components_dir / "AddTodo.tsx", 'w') as f:
            f.write(add_todo_content)
        
        task.result = {
            'created_files': [
                'src/types/todo.ts',
                'src/App.tsx',
                'src/components/AddTodo.tsx'
            ]
        }
    
    def _execute_backend_task(self, task: Task, project_dir: Path):
        """Backendタスクを実行"""
        # APIサーバーのセットアップ
        backend_dir = project_dir / "backend"
        backend_dir.mkdir(exist_ok=True)
        
        server_content = """const express = require('express');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// In-memory storage (replace with database in production)
let todos = [];

// Routes
app.get('/api/todos', (req, res) => {
  res.json(todos);
});

app.post('/api/todos', (req, res) => {
  const { title, description } = req.body;
  
  if (!title) {
    return res.status(400).json({ error: 'Title is required' });
  }
  
  const newTodo = {
    id: uuidv4(),
    title,
    description,
    completed: false,
    createdAt: new Date(),
    updatedAt: new Date()
  };
  
  todos.push(newTodo);
  res.status(201).json(newTodo);
});

app.put('/api/todos/:id', (req, res) => {
  const { id } = req.params;
  const { title, description, completed } = req.body;
  
  const todoIndex = todos.findIndex(todo => todo.id === id);
  
  if (todoIndex === -1) {
    return res.status(404).json({ error: 'Todo not found' });
  }
  
  todos[todoIndex] = {
    ...todos[todoIndex],
    title: title || todos[todoIndex].title,
    description: description !== undefined ? description : todos[todoIndex].description,
    completed: completed !== undefined ? completed : todos[todoIndex].completed,
    updatedAt: new Date()
  };
  
  res.json(todos[todoIndex]);
});

app.delete('/api/todos/:id', (req, res) => {
  const { id } = req.params;
  const initialLength = todos.length;
  
  todos = todos.filter(todo => todo.id !== id);
  
  if (todos.length === initialLength) {
    return res.status(404).json({ error: 'Todo not found' });
  }
  
  res.status(204).send();
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
"""
        
        with open(backend_dir / "server.js", 'w') as f:
            f.write(server_content)
        
        # package.json
        package_json = {
            "name": "todo-app-backend",
            "version": "1.0.0",
            "description": "Backend API for Todo App",
            "main": "server.js",
            "scripts": {
                "start": "node server.js",
                "dev": "nodemon server.js"
            },
            "dependencies": {
                "express": "^4.18.2",
                "cors": "^2.8.5",
                "uuid": "^9.0.0"
            },
            "devDependencies": {
                "nodemon": "^3.0.1"
            }
        }
        
        with open(backend_dir / "package.json", 'w') as f:
            json.dump(package_json, f, indent=2)
        
        task.result = {
            'created_files': [
                'backend/server.js',
                'backend/package.json'
            ]
        }
    
    def _execute_devops_task(self, task: Task, project_dir: Path):
        """DevOpsタスクを実行"""
        # Dockerファイルを作成
        dockerfile_content = """# Frontend Dockerfile
FROM node:18-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
"""
        
        with open(project_dir / "Dockerfile", 'w') as f:
            f.write(dockerfile_content)
        
        # docker-compose.yml
        docker_compose_content = """version: '3.8'

services:
  frontend:
    build: .
    ports:
      - "3000:80"
    environment:
      - NODE_ENV=production
    depends_on:
      - backend

  backend:
    build: ./backend
    ports:
      - "3001:3001"
    environment:
      - NODE_ENV=production
      - PORT=3001
    volumes:
      - ./backend:/app
      - /app/node_modules

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: todoapp
      POSTGRES_PASSWORD: todoapp123
      POSTGRES_DB: tododb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
"""
        
        with open(project_dir / "docker-compose.yml", 'w') as f:
            f.write(docker_compose_content)
        
        # GitHub Actions CI/CD
        github_dir = project_dir / ".github" / "workflows"
        github_dir.mkdir(parents=True, exist_ok=True)
        
        ci_content = """name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        
    - name: Install dependencies
      run: npm ci
      
    - name: Run tests
      run: npm test
      
    - name: Build
      run: npm run build

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to Vercel
      uses: amondnet/vercel-action@v20
      with:
        vercel-token: ${{ secrets.VERCEL_TOKEN }}
        vercel-org-id: ${{ secrets.ORG_ID}}
        vercel-project-id: ${{ secrets.PROJECT_ID}}
"""
        
        with open(github_dir / "ci-cd.yml", 'w') as f:
            f.write(ci_content)
        
        task.result = {
            'created_files': [
                'Dockerfile',
                'docker-compose.yml',
                '.github/workflows/ci-cd.yml'
            ]
        }
    
    def _execute_qa_task(self, task: Task, project_dir: Path):
        """QAタスクを実行"""
        # テストディレクトリを作成
        tests_dir = project_dir / "tests"
        tests_dir.mkdir(exist_ok=True)
        
        # Jestの設定
        jest_config = {
            "preset": "ts-jest",
            "testEnvironment": "jsdom",
            "setupFilesAfterEnv": ["<rootDir>/tests/setup.ts"],
            "moduleNameMapper": {
                "\\.(css|less|scss|sass)$": "identity-obj-proxy"
            }
        }
        
        with open(project_dir / "jest.config.json", 'w') as f:
            json.dump(jest_config, f, indent=2)
        
        # テストセットアップ
        setup_content = """import '@testing-library/jest-dom';

// Mock localStorage
const localStorageMock = {
  getItem: jest.fn(),
  setItem: jest.fn(),
  removeItem: jest.fn(),
  clear: jest.fn(),
};
global.localStorage = localStorageMock as any;
"""
        
        with open(tests_dir / "setup.ts", 'w') as f:
            f.write(setup_content)
        
        # Appコンポーネントのテスト
        app_test_content = """import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from '../src/App';

describe('Todo App', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  test('renders todo app header', () => {
    render(<App />);
    expect(screen.getByText('Todo App')).toBeInTheDocument();
  });

  test('adds a new todo', async () => {
    render(<App />);
    
    const titleInput = screen.getByPlaceholderText('What needs to be done?');
    const addButton = screen.getByText('Add Task');
    
    fireEvent.change(titleInput, { target: { value: 'Test Todo' } });
    fireEvent.click(addButton);
    
    await waitFor(() => {
      expect(screen.getByText('Test Todo')).toBeInTheDocument();
    });
  });

  test('toggles todo completion', async () => {
    render(<App />);
    
    // Add a todo first
    const titleInput = screen.getByPlaceholderText('What needs to be done?');
    const addButton = screen.getByText('Add Task');
    
    fireEvent.change(titleInput, { target: { value: 'Test Todo' } });
    fireEvent.click(addButton);
    
    // Toggle completion
    const checkbox = screen.getByRole('checkbox');
    fireEvent.click(checkbox);
    
    await waitFor(() => {
      expect(checkbox).toBeChecked();
    });
  });

  test('filters todos', async () => {
    render(<App />);
    
    // Add todos
    const titleInput = screen.getByPlaceholderText('What needs to be done?');
    const addButton = screen.getByText('Add Task');
    
    fireEvent.change(titleInput, { target: { value: 'Todo 1' } });
    fireEvent.click(addButton);
    
    fireEvent.change(titleInput, { target: { value: 'Todo 2' } });
    fireEvent.click(addButton);
    
    // Mark one as completed
    const checkboxes = screen.getAllByRole('checkbox');
    fireEvent.click(checkboxes[0]);
    
    // Test filters
    const activeFilter = screen.getByText('Active');
    fireEvent.click(activeFilter);
    
    await waitFor(() => {
      expect(screen.queryByText('Todo 1')).not.toBeInTheDocument();
      expect(screen.getByText('Todo 2')).toBeInTheDocument();
    });
  });
});
"""
        
        with open(tests_dir / "App.test.tsx", 'w') as f:
            f.write(app_test_content)
        
        # E2Eテスト (Cypress)
        e2e_dir = project_dir / "cypress" / "e2e"
        e2e_dir.mkdir(parents=True, exist_ok=True)
        
        e2e_test_content = """describe('Todo App E2E', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000');
  });

  it('completes a full todo workflow', () => {
    // Add a new todo
    cy.get('input[placeholder="What needs to be done?"]').type('Buy groceries');
    cy.get('input[placeholder="Description (optional)"]').type('Milk, eggs, bread');
    cy.contains('Add Task').click();

    // Verify todo appears
    cy.contains('Buy groceries').should('be.visible');
    cy.contains('Milk, eggs, bread').should('be.visible');

    // Add another todo
    cy.get('input[placeholder="What needs to be done?"]').type('Walk the dog');
    cy.contains('Add Task').click();

    // Mark first todo as complete
    cy.get('input[type="checkbox"]').first().click();

    // Filter by active
    cy.contains('Active').click();
    cy.contains('Buy groceries').should('not.exist');
    cy.contains('Walk the dog').should('be.visible');

    // Filter by completed
    cy.contains('Completed').click();
    cy.contains('Buy groceries').should('be.visible');
    cy.contains('Walk the dog').should('not.exist');

    // Show all
    cy.contains('All').click();
    cy.contains('Buy groceries').should('be.visible');
    cy.contains('Walk the dog').should('be.visible');

    // Delete a todo
    cy.contains('Walk the dog').parent().find('button[aria-label="Delete"]').click();
    cy.contains('Walk the dog').should('not.exist');
  });
});
"""
        
        with open(e2e_dir / "todo-app.cy.ts", 'w') as f:
            f.write(e2e_test_content)
        
        task.result = {
            'created_files': [
                'jest.config.json',
                'tests/setup.ts',
                'tests/App.test.tsx',
                'cypress/e2e/todo-app.cy.ts'
            ]
        }
    
    def execute_project(self, project_name: str, show_progress: bool = True):
        """プロジェクトの全タスクを順次実行"""
        project_tasks = [t for t in self.tasks if t.project == project_name]
        
        # 優先度順にソート
        project_tasks.sort(key=lambda t: t.priority)
        
        logging.info(f"🚀 Starting project execution: {project_name}")
        logging.info(f"📋 Total tasks: {len(project_tasks)}")
        
        if show_progress:
            self._show_progress_header(project_name, len(project_tasks))
        
        for i, task in enumerate(project_tasks):
            if task.status == TaskStatus.PENDING:
                if show_progress:
                    self._show_task_progress(i + 1, len(project_tasks), task)
                self.execute_task(task)
                if show_progress:
                    self._show_task_completion(task)
        
        # プロジェクトサマリーを生成
        self._generate_project_summary(project_name)
        
        if show_progress:
            self._show_project_completion(project_name)
    
    def _generate_project_summary(self, project_name: str):
        """プロジェクトのサマリーレポートを生成"""
        project_tasks = [t for t in self.tasks if t.project == project_name]
        completed_tasks = [t for t in project_tasks if t.status == TaskStatus.COMPLETED]
        
        summary = f"""# Project Summary: {project_name}

## Status Overview
- Total Tasks: {len(project_tasks)}
- Completed: {len(completed_tasks)}
- Success Rate: {(len(completed_tasks) / len(project_tasks) * 100):.1f}%

## Completed Tasks
"""
        
        for task in completed_tasks:
            summary += f"\n### {task.assigned_to.value}: {task.title}\n"
            if task.result and 'created_files' in task.result:
                summary += "Created files:\n"
                for file in task.result['created_files']:
                    summary += f"- {file}\n"
        
        summary += f"\n## Project Location\n`workspace/projects/{project_name}/`\n"
        
        report_file = self.workspace_dir / "communication" / "reports" / f"{project_name}_summary.md"
        with open(report_file, 'w') as f:
            f.write(summary)
        
        logging.info(f"📊 Project summary saved to: {report_file}")

def main():
    """デモ実行"""
    system = AICollaborativeSystem()
    
    # ToDoアプリプロジェクトを作成
    project_name = "todo-app"
    tasks = system.create_project(project_name, "web-app")
    
    print(f"\n✅ Created project '{project_name}' with {len(tasks)} tasks")
    print("\n📋 Task breakdown:")
    for task in tasks:
        print(f"  - {task.assigned_to.value}: {task.title}")
    
    # プロジェクトを実行
    print("\n🤖 Starting collaborative development...")
    system.execute_project(project_name)
    
    print("\n✨ Project completed! Check workspace/projects/todo-app/ for the generated code.")

if __name__ == "__main__":
    main()