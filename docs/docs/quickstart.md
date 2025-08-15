# 快速入门指南

## 1. 安装
```bash
pip install django_layui29
```

## 2. 基本配置
在 `settings.py` 中添加：
```python
INSTALLED_APPS = [
    ...
    'django_layui29',
    ...
]
```

## 3. 创建第一个页面
1. 创建视图：
```python
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')
```

2. 创建模板文件 `myapp/templates/myapp/home.html`：
```html
{% extends "layui29/layout/center.html" %}

{% block content %}
<div class="layui-card">
  <div class="layui-card-header">欢迎</div>
  <div class="layui-card-body">
    这是使用 django_layui29 创建的第一个页面
  </div>
</div>
{% endblock %}
```

3. 配置 URL：
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

## 4. 运行项目
```bash
python manage.py runserver
```
访问 http://localhost:8000 查看效果
