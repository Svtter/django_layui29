# django_layui29

[![中文](https://img.shields.io/badge/中文-文档-blue)](./README_zh.md)
[![Run Tests](https://github.com/Svtter/django_layui29/actions/workflows/test.yml/badge.svg)](https://github.com/Svtter/django_layui29/actions/workflows/test.yml)

> **WARNING:** This project is unstable. Please do not use it in a production environment.

`django_layui29` is a Django app that integrates the [Layui](https://layui.dev/) front-end framework (v2.9.25). It simplifies the use of Layui's UI components within a Django project.

This package also includes:
- `htmx 1.9.4`
- `js.cookie.js 3.0.5`

## Installation

Install the package using pip:
```bash
pip install django_layui29
```

## Features

- **Multiple Layouts**: Provides `center`, `admin`, and `normal` base layouts.
- **Table Components**: Simplifies the creation of data tables.
- **Flexible Asset Loading**: Supports loading Layui assets from a local source or a CDN.

## Usage

1.  Add `django_layui29` to your `INSTALLED_APPS` in `settings.py`:

    ```python
    INSTALLED_APPS = [
        # ... other apps
        'django_layui29',
    ]
    ```

2.  In your template, extend the base template:

    ```html
    {% extends 'layui29/base.html' %}
    ```

### Context Processors

Add the following to your `TEMPLATES` setting in `settings.py`:

```python
TEMPLATES = [
    {
        # ... other settings
        'OPTIONS': {
            'context_processors': [
                # ... other context processors
                'django_layui29.utils.get_layui_from_local',
            ],
        },
    },
]
```

### Asset Loading Configuration

You can control how Layui assets are loaded by setting `LAYUI_FROM_LOCAL` in your `settings.py`:

```python
# Set to True to load from local assets (recommended for production)
LAYUI_FROM_LOCAL = True

# Set to False to load from the unpkg CDN
# LAYUI_FROM_LOCAL = False
```

When `LAYUI_FROM_LOCAL` is `True`, the app will use the `layui.js` and `layui.css` files included with the package.

### Customizing Components

You can override the default templates to customize components. For example, to replace the header, place your app before `django_layui29` in `INSTALLED_APPS` and create your own `layui29/component/base/header.html` file.

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'your_app',       # Your app with custom templates
    'django_layui29',
]
```

## Example Project

You can run the `testapp` included in the [repository](https://github.com/Svtter/django_layui29.git) to see the features in action.

## Funding

If you find this project helpful, consider supporting me on [Ko-fi](https://ko-fi.com/svtter).
