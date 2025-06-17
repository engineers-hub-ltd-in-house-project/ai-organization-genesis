#!/usr/bin/env python3
"""
AI Organization Project Generator
新規プロジェクトの構造を自動生成
"""

import os
import json
from datetime import datetime

class ProjectGenerator:
    def __init__(self, workspace_dir: str = "."):
        self.workspace_dir = workspace_dir
        self.projects_dir = f"{workspace_dir}/workspace/projects"
    
    def create_project(self, project_name: str, project_type: str = "web-app"):
        """新規プロジェクトを作成"""
        project_dir = f"{self.projects_dir}/{project_name}"
        os.makedirs(project_dir, exist_ok=True)
        
        # プロジェクト設定
        project_config = {
            "name": project_name,
            "type": project_type,
            "created": datetime.now().isoformat(),
            "status": "planning",
            "team_assignments": {
                "ai-ceo": "Product Vision",
                "ai-cto": "Technical Architecture", 
                "ai-frontend": "UI/UX Development",
                "ai-backend": "API Development",
                "ai-devops": "Infrastructure",
                "ai-qa": "Testing & Quality"
            }
        }
        
        with open(f"{project_dir}/project.json", 'w') as f:
            json.dump(project_config, f, indent=2)
        
        print(f"🎉 Project '{project_name}' created successfully!")
        return project_dir

if __name__ == "__main__":
    generator = ProjectGenerator()
    generator.create_project("ai-powered-ecommerce", "web-app")
    generator.create_project("real-time-chat-platform", "web-app") 
    generator.create_project("ai-code-reviewer", "cli-tool")
    print("🌟 Sample projects generated!")
