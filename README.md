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
- Claude Code (オプション)

### Installation

```bash
# リポジトリをクローン
git clone https://github.com/engineers-hub-ltd-in-house-project/ai-organization-genesis.git
cd ai-organization-genesis

# 依存関係をインストール
pip install -r requirements.txt

# AI組織を生成
./ai-org-genesis.sh

# AI組織を起動
./ai-org-master.sh start
```

### Usage

1. **AI組織に接続**
   ```bash
   tmux attach -t ai-org
   ```

2. **ウィンドウ間の移動**
   - `Ctrl+B` → 数字キー (0-7)

3. **ウィンドウ構成**
   - Window 0: Control Center - コマンド実行
   - Window 1: AI-CEO - 戦略立案
   - Window 2: AI-CTO - 技術統括
   - Window 3: AI-Frontend - UI開発
   - Window 4: AI-Backend - API開発
   - Window 5: AI-DevOps - インフラ管理
   - Window 6: AI-QA - 品質保証
   - Window 7: Monitor - 監視ダッシュボード

## 🤖 AI Agents

### Management Layer

- **AI-CEO**: プロダクトビジョン、要件定義、プロジェクト調整
- **AI-CTO**: 技術アーキテクチャ、技術選定、コードレビュー

### Development Layer

- **AI-Frontend**: React/Vue開発、UI/UX、レスポンシブデザイン
- **AI-Backend**: API開発、データベース設計、認証システム
- **AI-DevOps**: Docker、Kubernetes、CI/CD、監視
- **AI-QA**: テスト自動化、品質保証、バグ検出

## 📋 Commands

### Master Control

```bash
# AI組織を起動
./ai-org-master.sh start

# AI組織を停止
./ai-org-master.sh stop

# 既存セッションに接続
./ai-org-master.sh attach

# ヘルプを表示
./ai-org-master.sh help
```

### Project Management

```bash
# 新規プロジェクト作成
cd ai-org
python3 knowledge/templates/project-generator.py

# ワークフロー生成
python3 ai-collaboration-system.py create-workflow --project "project-name" --type "web-app"

# デイリースタンドアップ
python3 ai-collaboration-system.py standup
```

### Agent Control

各エージェントウィンドウで使用可能なコマンド:

- `tasks` - 割り当てられたタスクを表示
- `start` - エージェントループを開始
- `quit` - エージェントを終了

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

### Adding New Agents

1. `personas/`に新しいAI人格定義を追加
2. `ai-collaboration-system.py`のエージェント定義を更新
3. `tmux-orchestrator.sh`に新しいウィンドウを追加

### Custom Workflows

`workflows/`ディレクトリにカスタムワークフローを定義可能

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