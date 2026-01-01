# django_layui29

[English](./README.md)

> **警告：** 此项目尚不稳定，请勿在生产环境中使用。

`django_layui29` 是一个集成了 [Layui](https://layui.dev/) 前端框架 (v2.9.25) 的 Django 应用。它简化了在 Django 项目中使用 Layui UI 组件的过程。

该包还包含：
- `htmx 1.9.4`
- `js.cookie.js 3.0.5`

## 安装

使用 pip 安装：
```bash
pip install django_layui29
```

## 功能特性

- **多种布局**: 提供 `center`、`admin` 和 `normal` 三种基础布局。
- **表格组件**: 简化数据表格的创建。
- **灵活的静态资源加载**: 支持从本地或 CDN 加载 Layui 静态资源。

## 使用方法

1.  在 `settings.py` 的 `INSTALLED_APPS` 中添加 `django_layui29`：

    ```python
    INSTALLED_APPS = [
        # ... 其他应用
        'django_layui29',
    ]
    ```

2.  在你的模板中，继承基础模板：

    ```html
    {% extends 'layui29/base.html' %}
    ```

### 上下文处理器 (Context Processors)

在 `settings.py` 的 `TEMPLATES` 设置中添加以下内容：

```python
TEMPLATES = [
    {
        # ... 其他设置
        'OPTIONS': {
            'context_processors': [
                # ... 其他上下文处理器
                'django_layui29.utils.get_layui_from_local',
            ],
        },
    },
]
```

### 静态资源加载配置

你可以通过在 `settings.py` 中设置 `LAYUI_FROM_LOCAL` 来控制 Layui 静态资源的加载方式：

```python
# 设置为 True 以从本地加载资源（生产环境推荐）
LAYUI_FROM_LOCAL = True

# 设置为 False 以从 unpkg CDN 加载
# LAYUI_FROM_LOCAL = False
```

当 `LAYUI_FROM_LOCAL` 为 `True` 时，应用将使用包内自带的 `layui.js` 和 `layui.css` 文件。

### 自定义组件

你可以通过覆盖默认模板来自定义组件。例如，要替换头部（header），请将你自己的应用放在 `INSTALLED_APPS` 中 `django_layui29` 的前面，并创建你自己的 `layui29/component/base/header.html` 文件。

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'your_app',       # 包含自定义模板的应用
    'django_layui29',
]
```

## 示例项目

你可以运行[仓库](https://github.com/Svtter/django_layui29.git)中包含的 `testapp` 来查看各项功能的实际效果。

## 赞助

如果你觉得这个项目对你有帮助，欢迎在 [Ko-fi](https://ko-fi.com/svtter) 上支持我。
