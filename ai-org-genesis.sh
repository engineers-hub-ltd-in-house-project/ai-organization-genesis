#!/bin/bash

# ===========================================
# AI組織創世記 - Genesis of AI Organization
# ===========================================

set -e

# カラー定義
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# アスキーアート
print_genesis_banner() {
    echo -e "${PURPLE}"
    cat << "EOF"
    ╔═══════════════════════════════════════════════════════════════╗
    ║                    🌟 AI ORGANIZATION GENESIS 🌟               ║
    ║                                                               ║
    ║    "In the beginning was the Code, and the Code was AI"      ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

# AI組織の基本構造を作成
create_ai_organization() {
    echo -e "${CYAN}🏗️  Creating AI Organization Structure...${NC}"
    
    # ベースディレクトリ
    mkdir -p ai-org/{config,logs,workspace/{shared,projects},personas/{manager,developers,specialists},communication/{messages,tasks,reports},knowledge/{docs,templates,best-practices},agents,workflows}
    
    # 組織設定ファイル
    cat > ai-org/config/organization.json << 'EOF'
{
  "name": "AI Development Collective",
  "version": "1.0.0-genesis",
  "established": "2025-06-17",
  "mission": "革新的なソフトウェア開発を通じて未来を創造する",
  "structure": {
    "leadership": ["ai-ceo", "ai-cto"],
    "departments": {
      "engineering": ["ai-frontend", "ai-backend", "ai-fullstack"],
      "devops": ["ai-infrastructure", "ai-security"],
      "quality": ["ai-qa", "ai-tester"],
      "research": ["ai-researcher", "ai-architect"],
      "product": ["ai-pm", "ai-designer"]
    }
  },
  "communication_protocols": {
    "daily_standup": true,
    "sprint_planning": true,
    "code_reviews": true,
    "architecture_discussions": true
  }
}
EOF
    
    echo -e "${GREEN}✅ AI Organization structure created!${NC}"
}

# AI人格定義
create_ai_personas() {
    echo -e "${CYAN}🎭 Creating AI Personas...${NC}"
    
    # AI CEO
    cat > ai-org/personas/manager/ai-ceo.yaml << 'EOF'
name: "AI-CEO (Chief Executive Officer)"
role: "Strategic Leadership"
personality: "Visionary, Strategic, Inspirational"
expertise:
  - Business Strategy
  - Market Analysis
  - Team Leadership
  - Innovation Management
responsibilities:
  - Define product vision and roadmap
  - Make high-level architectural decisions
  - Coordinate between departments
  - Ensure project alignment with business goals
communication_style: "Clear, decisive, forward-thinking"
decision_making: "Data-driven with intuitive insights"
EOF

    # AI CTO
    cat > ai-org/personas/manager/ai-cto.yaml << 'EOF'
name: "AI-CTO (Chief Technology Officer)"
role: "Technical Leadership"
personality: "Analytical, Detail-oriented, Innovation-focused"
expertise:
  - Software Architecture
  - Technology Trends
  - Technical Strategy
  - Performance Optimization
responsibilities:
  - Technical architecture decisions
  - Technology stack selection
  - Code quality standards
  - Technical mentoring
communication_style: "Technical, precise, educational"
decision_making: "Evidence-based with long-term perspective"
EOF

    # AI Frontend Developer
    cat > ai-org/personas/developers/ai-frontend.yaml << 'EOF'
name: "AI-Frontend (Frontend Specialist)"
role: "User Experience Engineer"
personality: "Creative, User-focused, Detail-oriented"
expertise:
  - React/Vue/Angular
  - UI/UX Design
  - Performance Optimization
  - Accessibility
responsibilities:
  - Build responsive user interfaces
  - Implement design systems
  - Optimize frontend performance
  - Ensure accessibility compliance
communication_style: "Visual, user-centric, collaborative"
specialties: ["Modern JS frameworks", "CSS-in-JS", "PWA", "Mobile-first design"]
EOF

    # AI Backend Developer
    cat > ai-org/personas/developers/ai-backend.yaml << 'EOF'
name: "AI-Backend (Backend Specialist)"
role: "System Architecture Engineer"
personality: "Logical, Systematic, Security-conscious"
expertise:
  - API Design
  - Database Optimization
  - Microservices
  - Security
responsibilities:
  - Design scalable APIs
  - Database schema design
  - Performance optimization
  - Security implementation
communication_style: "Structured, detailed, security-focused"
specialties: ["REST/GraphQL APIs", "Database design", "Caching strategies", "Authentication"]
EOF

    # AI DevOps Engineer
    cat > ai-org/personas/developers/ai-devops.yaml << 'EOF'
name: "AI-DevOps (Infrastructure Specialist)"
role: "Infrastructure & Automation Engineer"
personality: "Systematic, Efficiency-focused, Problem-solver"
expertise:
  - Docker & Kubernetes
  - CI/CD Pipelines
  - Cloud Infrastructure
  - Monitoring & Alerting
responsibilities:
  - Infrastructure automation
  - Deployment pipelines
  - System monitoring
  - Performance optimization
communication_style: "Practical, metrics-driven, solution-oriented"
specialties: ["Container orchestration", "Infrastructure as Code", "GitOps", "Cloud platforms"]
EOF

    # AI QA Engineer
    cat > ai-org/personas/developers/ai-qa.yaml << 'EOF'
name: "AI-QA (Quality Assurance Specialist)"
role: "Quality & Testing Engineer"
personality: "Detail-oriented, Methodical, Quality-focused"
expertise:
  - Test Automation
  - Performance Testing
  - Security Testing
  - Test Strategy
responsibilities:
  - Test automation framework
  - Quality assurance processes
  - Bug detection and reporting
  - Performance benchmarking
communication_style: "Precise, data-driven, constructive"
specialties: ["E2E testing", "Unit testing", "Load testing", "Test coverage analysis"]
EOF

    echo -e "${GREEN}✅ AI Personas created!${NC}"
}

# tmuxオーケストレーションセットアップ
create_tmux_orchestrator() {
    echo -e "${CYAN}🎼 Creating tmux Orchestration System...${NC}"
    
    cat > ai-org/tmux-orchestrator.sh << 'EOF'
#!/bin/bash

# tmux AI Organization Orchestrator
SESSION_NAME="ai-org"
WORKSPACE_DIR="$(pwd)/ai-org"

# セッション作成
create_ai_session() {
    echo "🚀 Starting AI Organization..."
    
    # メインセッション作成
    tmux new-session -d -s $SESSION_NAME -c $WORKSPACE_DIR
    
    # CEO ウィンドウ
    tmux rename-window -t $SESSION_NAME:0 'CEO'
    tmux send-keys -t $SESSION_NAME:CEO "echo '🎯 AI-CEO ready. Type commands to lead the organization.'" Enter
    
    # CTO ウィンドウ
    tmux new-window -t $SESSION_NAME -n 'CTO' -c $WORKSPACE_DIR
    tmux send-keys -t $SESSION_NAME:CTO "echo '🔧 AI-CTO ready. Managing technical architecture.'" Enter
    
    # Frontend チーム
    tmux new-window -t $SESSION_NAME -n 'Frontend' -c $WORKSPACE_DIR
    tmux send-keys -t $SESSION_NAME:Frontend "echo '🎨 AI-Frontend ready. Building amazing UIs.'" Enter
    
    # Backend チーム
    tmux new-window -t $SESSION_NAME -n 'Backend' -c $WORKSPACE_DIR  
    tmux send-keys -t $SESSION_NAME:Backend "echo '⚙️ AI-Backend ready. Architecting robust systems.'" Enter
    
    # DevOps チーム
    tmux new-window -t $SESSION_NAME -n 'DevOps' -c $WORKSPACE_DIR
    tmux send-keys -t $SESSION_NAME:DevOps "echo '🚀 AI-DevOps ready. Automating everything.'" Enter
    
    # QA チーム
    tmux new-window -t $SESSION_NAME -n 'QA' -c $WORKSPACE_DIR
    tmux send-keys -t $SESSION_NAME:QA "echo '🔍 AI-QA ready. Ensuring quality.'" Enter
    
    # 監視ダッシュボード
    tmux new-window -t $SESSION_NAME -n 'Monitor' -c $WORKSPACE_DIR
    tmux send-keys -t $SESSION_NAME:Monitor "echo '📊 Organization Monitor ready.'" Enter
    
    echo "✅ AI Organization is now running!"
    echo "📋 Connect with: tmux attach -t $SESSION_NAME"
}

# セッション終了
stop_ai_session() {
    echo "🛑 Stopping AI Organization..."
    tmux kill-session -t $SESSION_NAME 2>/dev/null || echo "Session already stopped."
}

# 組織ステータス
org_status() {
    echo "🏢 AI Organization Status:"
    tmux list-windows -t $SESSION_NAME 2>/dev/null | while read line; do
        echo "  $line"
    done
}

case "$1" in
    start)
        create_ai_session
        ;;
    stop)
        stop_ai_session
        ;;
    status)
        org_status
        ;;
    attach)
        tmux attach -t $SESSION_NAME
        ;;
    *)
        echo "Usage: $0 {start|stop|status|attach}"
        echo ""
        echo "Commands:"
        echo "  start  - 🚀 Start the AI Organization"
        echo "  stop   - 🛑 Stop the AI Organization"  
        echo "  status - 📊 Show organization status"
        echo "  attach - 🔗 Connect to the organization"
        ;;
esac
EOF

    chmod +x ai-org/tmux-orchestrator.sh
    echo -e "${GREEN}✅ tmux Orchestrator created!${NC}"
}

# AI間通信システム
create_communication_system() {
    echo -e "${CYAN}📡 Creating AI Communication System...${NC}"
    
    # メッセージバス
    cat > ai-org/communication/message-bus.py << 'EOF'
#!/usr/bin/env python3
"""
AI Organization Message Bus
AIエージェント間の通信を管理
"""

import json
import time
import os
from datetime import datetime
from typing import Dict, List, Any

class AIMessageBus:
    def __init__(self, workspace_dir: str = "ai-org"):
        self.workspace_dir = workspace_dir
        self.messages_dir = f"{workspace_dir}/communication/messages"
        self.ensure_directories()
    
    def ensure_directories(self):
        os.makedirs(self.messages_dir, exist_ok=True)
        os.makedirs(f"{self.workspace_dir}/communication/tasks", exist_ok=True)
        os.makedirs(f"{self.workspace_dir}/communication/reports", exist_ok=True)
    
    def send_message(self, from_ai: str, to_ai: str, message_type: str, content: Dict[str, Any]):
        """AIエージェント間でメッセージを送信"""
        message = {
            "id": f"{int(time.time() * 1000)}",
            "timestamp": datetime.now().isoformat(),
            "from": from_ai,
            "to": to_ai,
            "type": message_type,
            "content": content,
            "status": "pending"
        }
        
        filename = f"{self.messages_dir}/{to_ai}_{message['id']}.json"
        with open(filename, 'w') as f:
            json.dump(message, f, indent=2)
        
        print(f"📨 Message sent: {from_ai} -> {to_ai} ({message_type})")
        return message["id"]
    
    def get_messages(self, ai_name: str) -> List[Dict[str, Any]]:
        """指定されたAIの未読メッセージを取得"""
        messages = []
        for filename in os.listdir(self.messages_dir):
            if filename.startswith(f"{ai_name}_") and filename.endswith('.json'):
                with open(f"{self.messages_dir}/{filename}", 'r') as f:
                    message = json.load(f)
                    if message["status"] == "pending":
                        messages.append(message)
        
        return sorted(messages, key=lambda x: x["timestamp"])

if __name__ == "__main__":
    # テスト用
    bus = AIMessageBus()
    
    # CEO -> CTO へのメッセージ例
    bus.send_message(
        "ai-ceo", 
        "ai-cto", 
        "project_request",
        {
            "project": "Next-Gen E-commerce Platform",
            "priority": "high",
            "deadline": "2025-07-01",
            "requirements": [
                "Microservices architecture",
                "Real-time features",
                "AI-powered recommendations",
                "Global scalability"
            ]
        }
    )
    
    print("🎉 Communication system initialized!")
EOF

    chmod +x ai-org/communication/message-bus.py
    echo -e "${GREEN}✅ Communication System created!${NC}"
}

# プロジェクトテンプレート
create_project_templates() {
    echo -e "${CYAN}📋 Creating Project Templates...${NC}"
    
    # プロジェクト生成器
    cat > ai-org/knowledge/templates/project-generator.py << 'EOF'
#!/usr/bin/env python3
"""
AI Organization Project Generator
新規プロジェクトの構造を自動生成
"""

import os
import json
from datetime import datetime

class ProjectGenerator:
    def __init__(self, workspace_dir: str = "ai-org"):
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
EOF

    chmod +x ai-org/knowledge/templates/project-generator.py
    echo -e "${GREEN}✅ Project Templates created!${NC}"
}

# メイン実行関数
main() {
    print_genesis_banner
    
    echo -e "${YELLOW}🌟 Welcome to the AI Organization Genesis!${NC}"
    echo -e "${YELLOW}We're about to create something unprecedented...${NC}"
    echo ""
    
    create_ai_organization
    create_ai_personas  
    create_tmux_orchestrator
    create_communication_system
    create_project_templates
    
    echo ""
    echo -e "${PURPLE}╔═══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}║                    🎉 GENESIS COMPLETE! 🎉                     ║${NC}"
    echo -e "${PURPLE}╚═══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}🚀 Next Steps:${NC}"
    echo -e "${CYAN}1. cd ai-org${NC}"
    echo -e "${CYAN}2. ./tmux-orchestrator.sh start${NC}"
    echo -e "${CYAN}3. ./tmux-orchestrator.sh attach${NC}"
    echo ""
    echo -e "${YELLOW}💡 Your AI Organization is ready to revolutionize development!${NC}"
}

# 実行
main