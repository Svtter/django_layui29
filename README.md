# django_layui29

> WARNING: This project is unstable. Please do not use in your production project.

集成 layui version 2.9.25 的 django 插件。

- `htmx 1.9.4`
- `js.cookie.js 3.0.5`

## Installation

`pip install django_layui29`

## Features

This section lists all features about `django-layui29`.

- `center/admin/nomral` layout.
- table components.

### Example project

You could run the `testapp` in this [repo](https://github.com/Svtter/django_layui29.git) to view the features.

The file `layui29/component/base/header.html` need to be replaced.

When doing the replacement, put your apps in front of `django_layui29`, like this:

```python
INSTALLED_APPS = [
    ...
    'your_app',
    'django_layui29',
]
```

## Usage

1. add `django_layui29` to your settings.
2. in your template, `{% extends 'layui29/base.html' %}`.
