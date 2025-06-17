# 🌟 AI Organization Genesis

> **"Where AI Agents Collaborate to Build Software"**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success)](https://github.com/engineers-hub-ltd-in-house-project/ai-organization-genesis)

## 🎯 Overview

AI Organization Genesisは、Claude Code内で動作する革新的なAI協調開発システムです。単一のAIインスタンスが6つの専門的な役割（CEO、CTO、Frontend、Backend、DevOps、QA）を演じ分け、実際のソフトウェアプロジェクトを自動的に開発します。

### ✨ Key Features

- 🤖 **6つの専門AIエージェント**: 各分野のエキスパートとして振る舞う
- 📊 **リアルタイム進捗モニタリング**: プログレスバーとステータス表示
- 🚀 **完全自動コード生成**: 要件定義から実装、テストまで全自動
- 🎯 **タスクベース開発**: 優先度に基づく効率的なタスク実行
- 📁 **実ファイル生成**: 本物のコード、ドキュメント、設定ファイルを生成

## 🏗️ Architecture

```
ai-org/
├── ai-collaborative-system.py  # メインシステム（これだけあれば動作します）
├── workspace/                  # プロジェクト作業ディレクトリ（自動生成）
│   └── projects/              # 生成されたプロジェクト
├── communication/              # システム内部通信（自動生成）
│   ├── tasks/                 # タスク管理
│   └── reports/               # プロジェクトレポート
└── logs/                      # システムログ（自動生成）
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Claude Code環境（このシステムはClaude Code内で動作します）

### Installation

```bash
# リポジトリをクローン
git clone https://github.com/engineers-hub-ltd-in-house-project/ai-organization-genesis.git
cd ai-organization-genesis/ai-org

# 依存関係をインストール（標準ライブラリのみ使用）
# pip install は不要です
```

### Basic Usage

```bash
# シンプルに実行（デフォルトでToDoアプリを作成）
python3 ai-collaborative-system.py

# カスタムプロジェクトを作成する場合
python3 -c "
from ai_collaborative_system import AICollaborativeSystem
system = AICollaborativeSystem()
system.create_project('my-app', 'web-app')
system.execute_project('my-app', show_progress=True)
"
```

## 🤖 AI Agents

### Management Layer

- **AI-CEO** 👔
  - プロダクトビジョンと要件定義
  - ユーザーストーリーの作成
  - プロジェクト全体の調整

- **AI-CTO** 🔧
  - 技術アーキテクチャ設計
  - 技術スタックの選定
  - システム設計書の作成

### Development Layer

- **AI-Frontend** 🎨
  - React/TypeScriptでのUI開発
  - レスポンシブデザイン実装
  - コンポーネント設計

- **AI-Backend** ⚙️
  - REST API開発
  - データベース設計
  - ビジネスロジック実装

- **AI-DevOps** 🚀
  - Docker/Kubernetes設定
  - CI/CDパイプライン構築
  - インフラストラクチャ管理

- **AI-QA** 🔍
  - 自動テスト実装
  - E2Eテスト作成
  - 品質保証プロセス

## 📋 Usage Examples

### 1. 最も簡単な実行方法

```bash
# ai-orgディレクトリに移動
cd ai-org

# デフォルトのToDoアプリプロジェクトを自動生成
python3 ai-collaborative-system.py
```

実行結果：
```
✅ Created project 'todo-app' with 6 tasks

📋 Task breakdown:
  - ai-ceo: Product Vision & Requirements
  - ai-cto: Technical Architecture
  - ai-frontend: Frontend Development
  - ai-backend: Backend Development
  - ai-devops: Infrastructure Setup
  - ai-qa: Testing & Quality

🤖 Starting collaborative development...

============================================================
🚀 PROJECT: todo-app
📊 Total Tasks: 6
============================================================

[███████████████░░░░░░░░░░░░░░░] 50% Complete
⚡ Task 4/6: Backend Development
👤 Assigned to: ai-backend
🔄 Status: Starting...
✅ Status: completed
📁 Created 2 files
```

### 2. カスタムプロジェクトの作成

```python
from ai_collaborative_system import AICollaborativeSystem

# システムを初期化
system = AICollaborativeSystem()

# カスタムプロジェクトを作成（例：タスク管理アプリ）
tasks = system.create_project("task-manager", "web-app")

# プロジェクトを実行（進捗表示付き）
system.execute_project("task-manager", show_progress=True)

# プロジェクトステータスを確認
system.monitor_project("task-manager")
```

### 3. ワンライナーでの実行

```bash
# Pythonワンライナーで直接実行
python3 -c "from ai_collaborative_system import AICollaborativeSystem; s = AICollaborativeSystem(); s.create_project('my-app', 'web-app'); s.execute_project('my-app', show_progress=True)"
```

### 4. プロジェクトタイプ

現在サポートされているプロジェクトタイプ：

- `web-app`: フルスタックWebアプリケーション
- `api`: RESTful APIサービス（予定）
- `cli-tool`: コマンドラインツール（予定）

### 5. 生成される成果物

各プロジェクトで生成される主なファイル：

```
workspace/projects/[project-name]/
├── docs/
│   ├── requirements.md        # AI-CEOが作成した要件定義書
│   └── architecture.md        # AI-CTOが作成した技術仕様書
├── src/
│   ├── App.tsx               # AI-Frontendが作成したメインコンポーネント
│   ├── components/           # Reactコンポーネント
│   └── types/               # TypeScript型定義
├── backend/
│   ├── server.js            # AI-Backendが作成したExpressサーバー
│   └── package.json         # Node.js依存関係
├── tests/
│   ├── App.test.tsx         # AI-QAが作成した単体テスト
│   └── setup.ts            # テスト設定
├── cypress/
│   └── e2e/                # E2Eテスト
├── .github/
│   └── workflows/          # AI-DevOpsが作成したCI/CD設定
├── Dockerfile              # コンテナ設定
├── docker-compose.yml      # マルチコンテナ設定
└── jest.config.json       # テスト設定
```

### 6. 実行後の確認方法

```bash
# 生成されたファイルを確認
ls -la workspace/projects/todo-app/

# プロジェクトサマリーを確認
cat communication/reports/todo-app_summary.md

# 生成されたコードを確認（例：React App）
cat workspace/projects/todo-app/src/App.tsx
```

## 📊 Progress Monitoring

システムは開発進捗をリアルタイムで表示します：

```
============================================================
🚀 PROJECT: todo-app
📊 Total Tasks: 6
============================================================

[███████████████░░░░░░░░░░░░░░░] 50% Complete
⚡ Task 4/6: Backend Development
👤 Assigned to: ai-backend
🔄 Status: Starting...
✅ Status: completed
📁 Created 2 files
```

プロジェクト完了後の詳細レポート：

```
============================================================
📊 PROJECT MONITOR: todo-app
============================================================
Progress: 100% (6/6 tasks)

Task Details:
  ✅ [ai-ceo] Product Vision & Requirements
     📁 Files: docs/requirements.md
  ✅ [ai-cto] Technical Architecture
     📁 Files: docs/architecture.md
  ...
```

## 🛠️ Development

### プロジェクト構造のカスタマイズ

新しいプロジェクトタイプを追加する場合：

```python
def _execute_custom_task(self, task: Task, project_dir: Path):
    """カスタムタスクの実装"""
    # タスク固有のロジックを実装
    pass
```

### エージェントの役割拡張

`agent_capabilities`辞書を編集して、各エージェントの能力を拡張できます。

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/NewAgent`)
3. Commit your changes (`git commit -m 'Add new AI agent'`)
4. Push to the branch (`git push origin feature/NewAgent`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Future Roadmap

- [ ] より多くのプロジェクトタイプのサポート
- [ ] エージェント間の非同期通信
- [ ] 機械学習モデルの統合
- [ ] Webダッシュボード
- [ ] プラグインシステム

---

**Built with ❤️ by AI Organization Genesis Project**

*"Where Silicon Dreams Become Digital Reality"*