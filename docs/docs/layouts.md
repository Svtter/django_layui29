# 布局系统详解

## 布局类型

### 1. 居中布局 (center.html)
适用于内容居中展示的页面，如登录页、展示页等。

```html
{% extends "layui29/layout/center.html" %}

{% block content %}
<!-- 主要内容区域 -->
<div class="layui-card">
  <div class="layui-card-header">标题</div>
  <div class="layui-card-body">
    内容区域
  </div>
</div>
{% endblock %}
```

### 2. 管理后台布局 (admin.html)
包含左侧导航和顶部导航栏，适合后台管理系统。

```html
{% extends "layui29/layout/admin.html" %}

{% block left_nav %}
<!-- 自定义左侧导航 -->
<ul class="layui-nav layui-nav-tree">
  <li class="layui-nav-item layui-nav-itemed">
    <a href="javascript:;">控制台</a>
  </li>
</ul>
{% endblock %}

{% block content %}
<!-- 主要内容区域 -->
{% endblock %}
```

### 3. 主页布局 (home.html)
适合门户网站首页，包含顶部通栏导航。

```html
{% extends "layui29/layout/home.html" %}

{% block header %}
<!-- 自定义顶部导航 -->
<ul class="layui-nav">
  <li class="layui-nav-item"><a href="">首页</a></li>
</ul>
{% endblock %}

{% block content %}
<!-- 主要内容区域 -->
{% endblock %}
```

## 布局结构

### 通用区块
| 区块名称              | 说明                |
| --------------------- | ------------------- |
| `{% block content %}` | 主要内容区域 (必需) |
| `{% block css %}`     | 额外CSS样式         |
| `{% block js %}`      | 额外JavaScript      |

### Admin布局特有区块
| 区块名称               | 说明         |
| ---------------------- | ------------ |
| `{% block left_nav %}` | 左侧导航菜单 |
| `{% block top_nav %}`  | 顶部导航栏   |

## 布局配置 (PLANNING)

在 `settings.py` 中可配置默认布局选项：

```python
LAYUI29_LAYOUT_SETTINGS = {
    'DEFAULT_LAYOUT': 'center',  # 默认布局
    'ADMIN_TITLE': '管理系统',   # Admin布局标题
    'LOGO_URL': '/static/logo.png' # Logo地址
}
```