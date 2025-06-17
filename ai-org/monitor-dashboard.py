#!/usr/bin/env python3
"""
AI Organization Monitor Dashboard
AI組織の状態をリアルタイムで監視するダッシュボード
"""

import json
import os
import time
from datetime import datetime
from typing import Dict, List, Any
import curses

class OrganizationMonitor:
    def __init__(self, workspace_dir: str = "."):
        self.workspace_dir = workspace_dir
        self.tasks_dir = f"{workspace_dir}/communication/tasks"
        self.agents_dir = f"{workspace_dir}/agents"
        self.projects_dir = f"{workspace_dir}/workspace/projects"
        
    def get_all_tasks(self) -> List[Dict]:
        """すべてのタスクを取得"""
        tasks = []
        if os.path.exists(self.tasks_dir):
            for filename in os.listdir(self.tasks_dir):
                if filename.endswith('.json'):
                    with open(f"{self.tasks_dir}/{filename}", 'r') as f:
                        tasks.append(json.load(f))
        return tasks
    
    def get_organization_status(self) -> Dict[str, Any]:
        """組織全体のステータスを取得"""
        tasks = self.get_all_tasks()
        
        status = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_tasks": len(tasks),
            "tasks_by_status": {
                "pending": 0,
                "in_progress": 0,
                "completed": 0,
                "failed": 0
            },
            "tasks_by_agent": {},
            "projects": []
        }
        
        # タスクの集計
        for task in tasks:
            status["tasks_by_status"][task.get("status", "pending")] += 1
            
            agent = task.get("assigned_to", "unknown")
            if agent not in status["tasks_by_agent"]:
                status["tasks_by_agent"][agent] = {
                    "pending": 0,
                    "in_progress": 0,
                    "completed": 0,
                    "failed": 0
                }
            status["tasks_by_agent"][agent][task.get("status", "pending")] += 1
        
        # プロジェクト情報
        if os.path.exists(self.projects_dir):
            for project_name in os.listdir(self.projects_dir):
                project_path = f"{self.projects_dir}/{project_name}"
                if os.path.isdir(project_path):
                    project_tasks = [t for t in tasks if t.get("project") == project_name]
                    status["projects"].append({
                        "name": project_name,
                        "total_tasks": len(project_tasks),
                        "completed": len([t for t in project_tasks if t.get("status") == "completed"])
                    })
        
        return status
    
    def display_dashboard(self, stdscr):
        """Cursesを使用したダッシュボード表示"""
        curses.curs_set(0)  # カーソルを非表示
        stdscr.nodelay(1)   # 非ブロッキングモード
        
        # カラーペアの初期化
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
        
        while True:
            try:
                stdscr.clear()
                status = self.get_organization_status()
                
                # ヘッダー
                stdscr.addstr(0, 0, "╔═══════════════════════════════════════════════════════════════╗")
                stdscr.addstr(1, 0, "║        🌟 AI ORGANIZATION MONITOR DASHBOARD 🌟                ║")
                stdscr.addstr(2, 0, "╚═══════════════════════════════════════════════════════════════╝")
                
                # タイムスタンプ
                stdscr.addstr(4, 0, f"Last Update: {status['timestamp']}", curses.color_pair(4))
                
                # 全体統計
                stdscr.addstr(6, 0, "📊 ORGANIZATION OVERVIEW", curses.A_BOLD)
                stdscr.addstr(7, 0, f"Total Tasks: {status['total_tasks']}")
                
                # タスクステータス
                y = 9
                stdscr.addstr(y, 0, "📋 TASK STATUS", curses.A_BOLD)
                y += 1
                for status_type, count in status["tasks_by_status"].items():
                    color = 1 if status_type == "completed" else 2 if status_type == "in_progress" else 3 if status_type == "failed" else 0
                    stdscr.addstr(y, 2, f"{status_type.capitalize()}: {count}", curses.color_pair(color))
                    y += 1
                
                # エージェント別タスク
                y += 1
                stdscr.addstr(y, 0, "🤖 AGENT WORKLOAD", curses.A_BOLD)
                y += 1
                for agent, tasks in status["tasks_by_agent"].items():
                    stdscr.addstr(y, 2, f"{agent}:")
                    y += 1
                    for task_status, count in tasks.items():
                        if count > 0:
                            stdscr.addstr(y, 4, f"{task_status}: {count}")
                            y += 1
                
                # プロジェクト進捗
                if status["projects"]:
                    y += 1
                    stdscr.addstr(y, 0, "🏗️ PROJECT PROGRESS", curses.A_BOLD)
                    y += 1
                    for project in status["projects"]:
                        progress = (project["completed"] / project["total_tasks"] * 100) if project["total_tasks"] > 0 else 0
                        stdscr.addstr(y, 2, f"{project['name']}: {progress:.0f}% ({project['completed']}/{project['total_tasks']})")
                        y += 1
                
                # 操作説明
                max_y, max_x = stdscr.getmaxyx()
                stdscr.addstr(max_y - 2, 0, "Press 'q' to quit, 'r' to refresh")
                
                stdscr.refresh()
                
                # キー入力チェック
                key = stdscr.getch()
                if key == ord('q'):
                    break
                elif key == ord('r'):
                    continue
                
                time.sleep(5)  # 5秒ごとに自動更新
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                stdscr.addstr(0, 0, f"Error: {str(e)}")
                stdscr.refresh()
                time.sleep(2)

def main():
    monitor = OrganizationMonitor()
    
    # コマンドライン版
    print("🌟 AI Organization Monitor 🌟")
    print("=" * 50)
    
    try:
        # Cursesダッシュボードを起動
        curses.wrapper(monitor.display_dashboard)
    except:
        # Cursesが使えない場合は簡易表示
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            status = monitor.get_organization_status()
            
            print(f"Last Update: {status['timestamp']}")
            print(f"\nTotal Tasks: {status['total_tasks']}")
            print("\nTask Status:")
            for status_type, count in status["tasks_by_status"].items():
                print(f"  {status_type}: {count}")
            
            print("\nAgent Workload:")
            for agent, tasks in status["tasks_by_agent"].items():
                print(f"  {agent}:")
                for task_status, count in tasks.items():
                    if count > 0:
                        print(f"    {task_status}: {count}")
            
            print("\nPress Ctrl+C to quit")
            time.sleep(5)

if __name__ == "__main__":
    main()