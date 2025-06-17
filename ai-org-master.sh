#!/bin/bash

# ===========================================
# AI Organization Master Control System
# ===========================================

set -e

# カラー定義
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

WORKSPACE_DIR="ai-org"
SESSION_NAME="ai-org"

# 壮大なバナー表示
show_master_banner() {
    clear
    echo -e "${PURPLE}"
    cat << "EOF"
    ╔═══════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                   ║
    ║     🌟 AI ORGANIZATION MASTER CONTROL SYSTEM 🌟                                   ║
    ║                                                                                   ║
    ║         "Where Silicon Dreams Become Digital Reality"                             ║
    ║                                                                                   ║
    ║    🤖 CEO  🔧 CTO  🎨 Frontend  ⚙️ Backend  🚀 DevOps  🔍 QA                      ║
    ║                                                                                   ║
    ╚═══════════════════════════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
    echo ""
}

# システム状態チェック
check_prerequisites() {
    echo -e "${CYAN}🔍 Checking system prerequisites...${NC}"
    
    # tmux チェック
    if ! command -v tmux &> /dev/null; then
        echo -e "${RED}❌ tmux is not installed${NC}"
        echo -e "${YELLOW}💡 Install with: brew install tmux (macOS) or apt install tmux (Ubuntu)${NC}"
        exit 1
    fi
    
    # Python チェック
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Python 3 is not installed${NC}"
        exit 1
    fi
    
    # ワークスペースチェック
    if [ ! -d "$WORKSPACE_DIR" ]; then
        echo -e "${RED}❌ Workspace directory not found${NC}"
        echo -e "${YELLOW}💡 Run the genesis script first: ./ai-org-genesis.sh${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✅ Prerequisites check passed${NC}"
}

# tmux セッション構築
setup_tmux_environment() {
    echo -e "${CYAN}🖥️  Setting up tmux environment...${NC}"
    
    # 既存セッションを終了
    tmux kill-session -t "$SESSION_NAME" 2>/dev/null || true
    
    # メインセッション作成
    tmux new-session -d -s "$SESSION_NAME" -c "$WORKSPACE_DIR"
    
    # AI エージェント用ウィンドウ作成
    agents=("CEO" "CTO" "Frontend" "Backend" "DevOps" "QA")
    agent_names=("ai-ceo" "ai-cto" "ai-frontend" "ai-backend" "ai-devops" "ai-qa")
    
    tmux rename-window -t "$SESSION_NAME:0" 'Control'
    
    for i in "${!agents[@]}"; do
        agent="${agents[$i]}"
        agent_name="${agent_names[$i]}"
        
        tmux new-window -t "$SESSION_NAME" -n "$agent" -c "$WORKSPACE_DIR"
        tmux send-keys -t "$SESSION_NAME:$agent" "echo '🤖 ${agent_name} Agent Terminal'" Enter
        tmux send-keys -t "$SESSION_NAME:$agent" "python3 claude-code-agent.py ${agent_name}" Enter
    done
    
    # 監視ウィンドウ
    tmux new-window -t "$SESSION_NAME" -n 'Monitor' -c "$WORKSPACE_DIR"
    tmux send-keys -t "$SESSION_NAME:Monitor" "echo '📊 AI Organization Monitor'" Enter
    
    echo -e "${GREEN}✅ tmux environment ready${NC}"
}

# サンプルプロジェクト作成
create_sample_projects() {
    echo -e "${CYAN}🎯 Creating sample projects...${NC}"
    
    cd "$WORKSPACE_DIR"
    
    # プロジェクト生成
    python3 knowledge/templates/project-generator.py
    
    # ワークフロー生成
    python3 ai-collaboration-system.py create-workflow --project "ai-powered-ecommerce" --type "web-app"
    
    echo -e "${GREEN}✅ Sample projects created${NC}"
}

# 完全起動シーケンス
full_startup() {
    show_master_banner
    
    echo -e "${WHITE}🚀 INITIATING AI ORGANIZATION STARTUP SEQUENCE...${NC}"
    echo ""
    
    check_prerequisites
    echo ""
    
    setup_tmux_environment
    echo ""
    
    create_sample_projects
    echo ""
    
    echo -e "${PURPLE}╔═══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}║                    🎉 STARTUP COMPLETE! 🎉                     ║${NC}"
    echo -e "${PURPLE}╚═══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}🎯 Your AI Organization is now fully operational!${NC}"
    echo ""
    echo -e "${CYAN}📋 Next Steps:${NC}"
    echo -e "${YELLOW}1. Connect to the organization: tmux attach -t ai-org${NC}"
    echo -e "${YELLOW}2. Navigate between agents with Ctrl+B then 1,2,3...${NC}"
    echo -e "${YELLOW}3. Use Control window for commands${NC}"
    echo ""
    
    # tmuxセッションに接続
    tmux attach -t "$SESSION_NAME"
}

# システム停止
shutdown_organization() {
    echo -e "${YELLOW}🛑 Shutting down AI Organization...${NC}"
    tmux kill-session -t "$SESSION_NAME" 2>/dev/null || true
    echo -e "${GREEN}✅ AI Organization shutdown complete${NC}"
}

# ヘルプ表示
show_help() {
    echo -e "${PURPLE}🤖 AI Organization Master Control${NC}"
    echo -e "${PURPLE}================================${NC}"
    echo ""
    echo -e "${CYAN}Usage: $0 <command>${NC}"
    echo ""
    echo -e "${YELLOW}Commands:${NC}"
    echo -e "${GREEN}  start     ${NC}- 🚀 Full startup sequence"
    echo -e "${GREEN}  stop      ${NC}- 🛑 Shutdown AI organization"
    echo -e "${GREEN}  attach    ${NC}- 🔗 Attach to existing session"
    echo -e "${GREEN}  help      ${NC}- 📖 Show this help"
    echo ""
}

# メイン処理
main() {
    case "${1:-help}" in
        "start"|"startup")
            full_startup
            ;;
        "stop"|"shutdown")
            shutdown_organization
            ;;
        "attach"|"connect")
            if tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
                tmux attach -t "$SESSION_NAME"
            else
                echo -e "${RED}❌ No active session found${NC}"
                echo -e "${YELLOW}💡 Start the organization first: $0 start${NC}"
            fi
            ;;
        "help"|"--help"|"-h"|"")
            show_help
            ;;
        *)
            echo -e "${RED}❌ Unknown command: $1${NC}"
            show_help
            exit 1
            ;;
    esac
}

# 実行
main "$@"