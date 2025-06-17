#!/usr/bin/env python3
"""
Claude Code AI Agent Wrapper
各AIエージェントがClaude Codeを通じて実際に作業を実行するためのラッパー
"""

import json
import os
import time
import anyio
from typing import Dict, List, Any
from datetime import datetime
try:
    from claude_code_sdk import query, ClaudeCodeOptions, Message
    CLAUDE_SDK_AVAILABLE = True
except ImportError:
    CLAUDE_SDK_AVAILABLE = False
    print("⚠️  Claude Code SDK not installed. Running in simulation mode.")

class ClaudeCodeAgent:
    def __init__(self, agent_name: str, workspace_dir: str = "."):
        self.agent_name = agent_name
        self.workspace_dir = workspace_dir
        self.agent_dir = f"{workspace_dir}/agents/{agent_name}"
        self.config_file = f"{self.agent_dir}/agent-config.json"
        
        self.ensure_agent_setup()
        self.load_agent_config()
    
    def ensure_agent_setup(self):
        """エージェントのセットアップを確認"""
        os.makedirs(self.agent_dir, exist_ok=True)
        
        if not os.path.exists(self.config_file):
            self.create_default_config()
    
    def create_default_config(self):
        """デフォルト設定を作成"""
        config = {
            "name": self.agent_name,
            "status": "ready",
            "current_task": None,
            "last_activity": datetime.now().isoformat(),
            "capabilities": self.get_agent_capabilities()
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
    
    def get_agent_capabilities(self) -> List[str]:
        """エージェントの能力を定義"""
        capabilities = {
            "ai-ceo": ["strategic_planning", "requirements_analysis", "project_coordination"],
            "ai-cto": ["technical_architecture", "technology_selection", "code_review"],
            "ai-frontend": ["react_development", "ui_design", "responsive_design"],
            "ai-backend": ["api_development", "database_design", "microservices"],
            "ai-devops": ["docker", "kubernetes", "ci_cd", "monitoring"],
            "ai-qa": ["test_automation", "quality_assurance", "bug_detection"]
        }
        
        return capabilities.get(self.agent_name, ["general_development"])
    
    def load_agent_config(self):
        """エージェント設定を読み込み"""
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)
    
    def check_tasks(self) -> List[Dict]:
        """自分に割り当てられたタスクをチェック"""
        tasks_dir = f"{self.workspace_dir}/communication/tasks"
        tasks = []
        
        if os.path.exists(tasks_dir):
            for filename in os.listdir(tasks_dir):
                if filename.endswith('.json'):
                    with open(f"{tasks_dir}/{filename}", 'r') as f:
                        task = json.load(f)
                        if (task["assigned_to"] == self.agent_name and 
                            task["status"] in ["pending", "in_progress"]):
                            # priorityを数値に変換
                            if isinstance(task.get("priority"), str):
                                try:
                                    task["priority"] = int(task["priority"])
                                except:
                                    task["priority"] = 2  # デフォルトはMEDIUM
                            tasks.append(task)
        
        return sorted(tasks, key=lambda x: x["priority"], reverse=True)
    
    def execute_task_with_claude_code(self, task: Dict) -> Dict[str, Any]:
        """Claude Codeを使ってタスクを実行"""
        print(f"🤖 {self.agent_name} executing task: {task['title']}")
        
        # Claude Code用のプロンプトを生成
        prompt = self.generate_claude_code_prompt(task)
        
        # 実際のClaude Codeコマンドを実行するか、シミュレーションを選択
        use_real_claude = os.environ.get('USE_REAL_CLAUDE', 'false').lower() == 'true'
        
        if use_real_claude and CLAUDE_SDK_AVAILABLE:
            # 非同期実行のためのラッパー
            result = anyio.run(self.execute_with_real_claude, task, prompt)
        else:
            # シミュレーションモード
            result = self.simulate_claude_code_execution(task)
        
        if result['success']:
            self.update_task_status(task['id'], 'completed')
            print(f"✅ {self.agent_name} completed task: {task['title']}")
        else:
            self.update_task_status(task['id'], 'failed')
            print(f"❌ {self.agent_name} failed task: {task['title']}")
        
        return result
    
    async def execute_with_real_claude(self, task: Dict, prompt: str) -> Dict[str, Any]:
        """実際のClaude Code SDKを使ってタスクを実行"""
        if not CLAUDE_SDK_AVAILABLE:
            print("⚠️  Claude Code SDK not available. Falling back to simulation.")
            return self.simulate_claude_code_execution(task)
        
        try:
            messages = []
            project_dir = f"{self.workspace_dir}/workspace/projects/{task['project']}"
            os.makedirs(project_dir, exist_ok=True)
            
            # Claude Codeオプションを設定
            options = ClaudeCodeOptions(
                max_turns=10,
                system_prompt=f"You are {self.agent_name}, an AI agent specialized in {', '.join(self.config['capabilities'])}. Work in the project directory: {project_dir}",
                cwd=project_dir,
                permission_mode="autoApprove"  # 自動承認モード
            )
            
            # Claude Codeクエリを実行
            async for message in query(prompt, options):
                messages.append(message)
            
            # 結果を解析
            success = len(messages) > 0
            output_files = []
            
            # 作成されたファイルをチェック
            if os.path.exists(project_dir):
                for root, dirs, files in os.walk(project_dir):
                    for file in files:
                        rel_path = os.path.relpath(os.path.join(root, file), project_dir)
                        output_files.append(rel_path)
            
            return {
                'success': success,
                'output_files': output_files,
                'summary': f"Task completed with {len(messages)} Claude interactions",
                'metrics': {
                    'files_created': len(output_files),
                    'claude_messages': len(messages)
                }
            }
            
        except Exception as e:
            print(f"❌ Error executing with Claude Code: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'summary': f"Failed to execute task: {str(e)}",
                'metrics': {}
            }
    
    def generate_claude_code_prompt(self, task: Dict) -> str:
        """Claude Code用のプロンプトを生成"""
        prompt = f"""
## AI Agent: {self.agent_name}

### Current Task
**Title**: {task['title']}
**Description**: {task['description']}
**Project**: {task['project']}
**Priority**: {task['priority']}

### Your Role
You are an expert {self.agent_name} with capabilities in: {', '.join(self.config['capabilities'])}

### Instructions
1. Analyze the task requirements carefully
2. Implement the solution using appropriate tools and frameworks
3. Write comprehensive code and documentation
4. Ensure high quality and best practices

Execute this task with your specialized expertise.
"""
        return prompt
    
    def simulate_claude_code_execution(self, task: Dict) -> Dict[str, Any]:
        """Claude Code実行のシミュレーション"""
        time.sleep(2)  # 実行時間をシミュレート
        
        # エージェントの役割に応じた出力ファイルを生成
        output_files = []
        if self.agent_name == "ai-frontend":
            output_files = ["src/components/App.tsx", "src/styles/main.css"]
        elif self.agent_name == "ai-backend":
            output_files = ["src/api/routes.py", "src/models/database.py"]
        elif self.agent_name == "ai-devops":
            output_files = ["docker-compose.yml", "k8s/deployment.yaml"]
        
        return {
            'success': True,
            'output_files': output_files,
            'summary': f"Successfully completed {task['title']}",
            'metrics': {'files_created': len(output_files)}
        }
    
    def update_task_status(self, task_id: str, status: str):
        """タスクステータスを更新"""
        task_file = f"{self.workspace_dir}/communication/tasks/{task_id}.json"
        if os.path.exists(task_file):
            with open(task_file, 'r') as f:
                task = json.load(f)
            
            task['status'] = status
            task['updated_at'] = datetime.now().isoformat()
            
            with open(task_file, 'w') as f:
                json.dump(task, f, indent=2)
    
    def start_agent_loop(self):
        """エージェントのメインループを開始"""
        print(f"🚀 Starting {self.agent_name} agent loop...")
        
        while True:
            try:
                # タスクをチェック
                tasks = self.check_tasks()
                if tasks:
                    # 最優先タスクを実行
                    current_task = tasks[0]
                    self.execute_task_with_claude_code(current_task)
                    time.sleep(5)
                else:
                    time.sleep(30)
                    
            except KeyboardInterrupt:
                print(f"🛑 Stopping {self.agent_name} agent...")
                break

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Claude Code AI Agent")
    parser.add_argument("agent_name", help="Agent name (ai-ceo, ai-cto, etc.)")
    parser.add_argument("--workspace", default=".", help="Workspace directory")
    parser.add_argument("--mode", choices=["interactive", "batch"], default="interactive", help="Run mode")
    parser.add_argument("--command", help="Command to run in batch mode")
    
    args = parser.parse_args()
    
    agent = ClaudeCodeAgent(args.agent_name, args.workspace)
    
    if args.mode == "batch":
        # バッチモード
        if args.command == "tasks":
            tasks = agent.check_tasks()
            for task in tasks:
                print(f"📋 {task['title']} (Status: {task['status']})")
        elif args.command == "start":
            agent.start_agent_loop()
        return
    
    # インタラクティブモード
    print(f"🤖 {args.agent_name} agent ready")
    print("Commands: 'tasks', 'start', 'quit'")
    
    while True:
        try:
            command = input(f"{args.agent_name}> ").strip()
            
            if command == 'tasks':
                tasks = agent.check_tasks()
                for task in tasks:
                    print(f"📋 {task['title']} (Status: {task['status']})")
            
            elif command == 'start':
                agent.start_agent_loop()
                break
            
            elif command == 'quit':
                break
            
            else:
                print("Unknown command")
                
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()