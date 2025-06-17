# 🌟 AI Organization Genesis

> **"In the beginning was the Code, and the Code was AI"**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success)](https://github.com/engineers-hub-ltd-in-house-project/ai-organization-genesis)

## 🎯 Overview

AI Organization Genesisは、複数のAIエージェントが協調してソフトウェア開発を行う革新的なシステムです。Claude Codeとtmuxを活用し、CEO、CTO、エンジニアなど6つの専門AIが自動的にプロジェクトを遂行します。

### ✨ Features

- 🤖 **6つの専門AIエージェント**: CEO, CTO, Frontend, Backend, DevOps, QA
- 🤝 **自動協調システム**: AIエージェント間の自動タスク分配と連携
- 📊 **リアルタイム監視**: 進捗とエージェント状態をダッシュボードで可視化
- 🚀 **完全自動化**: プロジェクト作成から実装まで全自動
- 💬 **AI間通信**: メッセージバスによるエージェント間コミュニケーション

## 🏗️ System Architecture

```
ai-org/
├── config/                    # 組織設定
│   └── organization.json     # AI組織の構造定義
├── personas/                  # AI人格定義
│   ├── manager/              # 管理職AI (CEO, CTO)
│   └── developers/           # 開発者AI
├── agents/                    # エージェント作業環境
├── communication/             # 通信システム
│   ├── messages/             # AI間メッセージ
│   ├── tasks/                # タスク管理
│   └── reports/              # レポート
├── workspace/                 # プロジェクト作業場
│   ├── shared/               # 共有リソース
│   └── projects/             # 各プロジェクト
├── workflows/                 # ワークフロー定義
├── knowledge/                 # 知識ベース
│   └── templates/            # プロジェクトテンプレート
└── logs/                     # システムログ
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- tmux
- Git
- Node.js (Claude Codeを使用する場合)
- Claude Code CLI (オプション、実際のAI実行用)

### Installation

```bash
# リポジトリをクローン
git clone https://github.com/engineers-hub-ltd-in-house-project/ai-organization-genesis.git
cd ai-organization-genesis

# 依存関係をインストール
pip install -r requirements.txt
# 注: claude-code-sdkとanyioが含まれています（実AIモード用）

# AI組織を生成
./ai-org-genesis.sh

# AI組織を起動
./ai-org-master.sh start
```

### 🎮 動作モード

#### シミュレーションモード（デフォルト）
Claude Codeがインストールされていない環境でも動作確認が可能。タスクの実行をシミュレートします。

#### 実AIモード
実際のClaude Codeを使用してAIがコードを生成します。

```bash
# 実AIモードを有効にする
export USE_REAL_CLAUDE=true

# Claude Code CLIのインストール（必要な場合）
npm install -g @anthropic-ai/claude-code
```

### Usage

#### 1. 基本的な起動と接続

```bash
# AI組織を起動
./ai-org-master.sh start

# tmuxセッションに接続
tmux attach -t ai-org
```

#### 2. tmux操作ガイド

**ウィンドウ切り替え**: `Ctrl+B` → 数字キー

| キー | ウィンドウ | 役割 |
|------|------------|------|
| 0 | Control Center | コマンド実行・プロジェクト管理 |
| 1 | AI-CEO | 戦略立案・要件定義 |
| 2 | AI-CTO | 技術アーキテクチャ設計 |
| 3 | AI-Frontend | UI/UX開発 |
| 4 | AI-Backend | API・サーバーサイド開発 |
| 5 | AI-DevOps | インフラ・CI/CD構築 |
| 6 | AI-QA | テスト自動化・品質保証 |
| 7 | Monitor | リアルタイム監視ダッシュボード |

**その他のtmuxコマンド**:
- `Ctrl+B` → `D`: セッションから離脱（バックグラウンドで継続）
- `Ctrl+B` → `[`: スクロールモード（`q`で終了）
- `Ctrl+B` → `c`: 新しいウィンドウ作成
- `Ctrl+B` → `x`: 現在のペインを閉じる

#### 3. プロジェクトの作成と開発

**新規プロジェクトの開始**（Control Centerで実行）:

```bash
# Webアプリケーション開発
cd ai-org
python3 ai-collaboration-system.py create-workflow --project "my-ecommerce-site" --type "web-app"

# REST API開発
python3 ai-collaboration-system.py create-workflow --project "user-api" --type "api"

# CLIツール開発
python3 ai-collaboration-system.py create-workflow --project "deploy-tool" --type "cli-tool"
```

#### 4. AIエージェントの操作

各エージェントウィンドウで利用可能なコマンド:

```bash
# 割り当てられたタスクを確認
tasks

# 自動実行モードを開始（AIがタスクを自動処理）
start

# エージェントを終了
quit
```

**実行例**（AI-CEOウィンドウ）:
```bash
ai-ceo> tasks
📋 Product Vision & Requirements (Status: pending)
📋 Market Analysis Report (Status: pending)

ai-ceo> start
🚀 Starting ai-ceo agent loop...
🤖 ai-ceo executing task: Product Vision & Requirements
✅ ai-ceo completed task: Product Vision & Requirements
```

#### 5. プロジェクト進捗の確認

**監視ダッシュボード**（Window 7）:
- タスクの進捗状況をリアルタイム表示
- 各エージェントの作業負荷を可視化
- プロジェクトの完了率を確認

**デイリースタンドアップレポート**:
```bash
cd ai-org
python3 ai-collaboration-system.py standup
```

#### 6. 実践的なワークフロー例

**ECサイト構築プロジェクト**:

```bash
# 1. プロジェクト作成
python3 ai-collaboration-system.py create-workflow --project "fashion-store" --type "web-app"

# 2. 各エージェントでタスク実行
# CEO: ビジネス要件定義
# CTO: 技術スタック決定（React + Node.js + PostgreSQL）
# Frontend: Reactコンポーネント開発
# Backend: REST API実装
# DevOps: Docker化とKubernetes設定
# QA: E2Eテスト自動化

# 3. 進捗確認（Monitor windowで監視）
```

#### 7. システムの停止と再開

```bash
# セッションから離脱（バックグラウンドで継続）
# tmux内で: Ctrl+B → D

# AI組織を完全に停止
./ai-org-master.sh stop

# 既存セッションに再接続
./ai-org-master.sh attach
```

## 🤖 AI Agents

### Management Layer

- **AI-CEO**: プロダクトビジョン、要件定義、プロジェクト調整
- **AI-CTO**: 技術アーキテクチャ、技術選定、コードレビュー

### Development Layer

- **AI-Frontend**: React/Vue開発、UI/UX、レスポンシブデザイン
- **AI-Backend**: API開発、データベース設計、認証システム
- **AI-DevOps**: Docker、Kubernetes、CI/CD、監視
- **AI-QA**: テスト自動化、品質保証、バグ検出

## 📋 Commands Reference

### Master Control

```bash
./ai-org-master.sh start    # AI組織を起動
./ai-org-master.sh stop     # AI組織を停止
./ai-org-master.sh attach   # 既存セッションに接続
./ai-org-master.sh help     # ヘルプを表示
```

### Project Management

```bash
# 新規プロジェクト作成（プロジェクトタイプ: web-app, api, cli-tool）
python3 ai-collaboration-system.py create-workflow --project "project-name" --type "web-app"

# デイリースタンドアップレポート生成
python3 ai-collaboration-system.py standup

# プロジェクトテンプレート生成
python3 knowledge/templates/project-generator.py
```

### Agent Commands

```bash
tasks  # 割り当てられたタスクを表示
start  # 自動実行モードを開始
quit   # エージェントを終了
```

### tmux Commands

| コマンド | 説明 |
|---------|------|
| `Ctrl+B` → `0-7` | ウィンドウ切り替え |
| `Ctrl+B` → `D` | セッションから離脱 |
| `Ctrl+B` → `[` | スクロールモード |
| `Ctrl+B` → `%` | 画面を縦に分割 |
| `Ctrl+B` → `"` | 画面を横に分割 |
| `Ctrl+B` → `arrow` | ペイン間を移動 |

## 🔄 Workflow

1. **プロジェクト開始**
   - AI-CEOが要件を定義
   - AI-CTOが技術アーキテクチャを設計

2. **開発フェーズ**
   - Frontend/Backend AIが並行開発
   - AI-DevOpsがインフラを構築

3. **品質保証**
   - AI-QAが自動テストを実装
   - 継続的な品質チェック

4. **デプロイメント**
   - AI-DevOpsが自動デプロイ
   - 監視とアラート設定

## 📊 Monitoring

監視ダッシュボードで以下の情報をリアルタイム確認:

- 組織全体のタスク状況
- エージェント別の作業負荷
- プロジェクトの進捗状況
- タスクの完了率

## 🛠️ Development

### トラブルシューティング

**tmuxセッションが見つからない場合**:
```bash
# セッション一覧を確認
tmux ls

# 古いセッションを削除
tmux kill-session -t ai-org

# 再起動
./ai-org-master.sh start
```

**エージェントが応答しない場合**:
```bash
# 特定のウィンドウでエージェントを再起動
# 例: CEOエージェントの再起動
tmux send-keys -t ai-org:CEO C-c Enter
tmux send-keys -t ai-org:CEO "python3 claude-code-agent.py ai-ceo" Enter
```

**タスクが正しく読み込まれない場合**:
```bash
# タスクファイルの確認
ls -la ai-org/communication/tasks/

# タスクの手動作成
cd ai-org
python3 ai-collaboration-system.py create-workflow --project "test-project" --type "web-app"
```

**Claude Code SDKエラーの場合**:
```bash
# 依存関係を再インストール
pip install -r requirements.txt

# シミュレーションモードで実行
unset USE_REAL_CLAUDE
```

**ディレクトリ構造の問題**:
```bash
# 入れ子のai-orgディレクトリが作成された場合
rm -rf ai-org/ai-org

# 正しいディレクトリから実行
cd ai-org
pwd  # /path/to/ai-organization-genesis/ai-org であることを確認
```

### Adding New Agents

1. `personas/`に新しいAI人格定義を追加
2. `ai-collaboration-system.py`のエージェント定義を更新
3. `tmux-orchestrator.sh`に新しいウィンドウを追加

### Custom Workflows

`workflows/`ディレクトリにカスタムワークフローを定義可能

### プロジェクトタイプの拡張

新しいプロジェクトタイプを追加する場合は、`ai-collaboration-system.py`の`create_project_workflow`メソッドを拡張:

```python
if project_type == "mobile-app":
    # モバイルアプリ用のタスクを定義
    tasks.append(self.create_task(...))
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Claude Code by Anthropic
- tmux for terminal multiplexing
- Python community for excellent libraries

## 🌟 Future Roadmap

- [ ] Web UI for monitoring
- [ ] More AI agent specializations
- [ ] Cloud deployment support
- [ ] Multi-language support
- [ ] AI learning and improvement system
- [ ] Integration with popular development tools

---

**Built with ❤️ by the AI Organization Genesis Project**

*"Where Silicon Dreams Become Digital Reality"*