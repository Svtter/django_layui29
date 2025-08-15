# 项目文档指南

本项目使用 MkDocs 构建文档系统，以下是文档结构说明：

## 文档目录结构
```
docs/
├── index.md          # 主文档（项目介绍/安装/使用）
├── quickstart.md     # 快速入门指南
├── components.md     # 组件使用文档
├── layouts.md        # 布局系统详解
└── advanced.md       # 高级配置和扩展
```

## 本地开发
```bash
# 安装 mkdocs
pip install mkdocs

# 启动实时预览（访问 http://localhost:8000）
mkdocs serve

# 构建静态站点
mkdocs build
```

## 部署到 GitHub Pages
1. 配置 `.github/workflows/gh-pages.yml`
2. 推送代码后将自动部署到 gh-pages 分支

## 文档编写规范
1. 使用 Markdown 语法
2. 代码示例需包含语言标识（如 ```python）
3. 保持目录结构清晰
4. 重要变更需更新 CHANGELOG.md
