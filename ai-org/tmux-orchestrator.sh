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
