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
    def __init__(self, workspace_dir: str = "."):
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
