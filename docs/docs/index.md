# django_layui29

- stable version: `1.5.1`
- dev version: `1.6.*`


基于 Django 的 Layui 2.9.8 集成插件，提供现代化后台管理界面和 UI 组件。

## 特性
- 三种布局模板：`center`（居中布局）、`admin`（管理后台布局）、`home`（主页布局）
- 表格组件（支持分页、排序、筛选）
- 集成依赖：
  - htmx 1.9.4 (前端交互增强)
  - js.cookie.js 3.0.5 (Cookie 管理)
  - Layui 2.9.8 (核心 UI 框架)

## 安装
```bash
pip install django_layui29
```

## 配置

在 `settings.py` 中添加应用：

```python
INSTALLED_APPS = [
    ...
    'django_layui29',
    ...
]
```

引入静态文件（确保已配置 STATICFILES_DIRS）：

```html
{% load static %}
<link rel="stylesheet" href="{% static 'layui29/css/layui.css' %}">
<script src="{% static 'layui29/layui.js' %}"></script>
```

如果使用 django_layui29 自带的 template，则不需要引入 static 文件。模板会自动引入。

## 快速入门
### 使用布局模板
```html
{% extends "layui29/layout/admin.html" %}

{% block content %}
<!-- 您的页面内容 -->
<div class="layui-card">
  <div class="layui-card-header">控制面板</div>
  <div class="layui-card-body">
    欢迎使用 django_layui29
  </div>
</div>
{% endblock %}
```

### 使用表格组件
```html
{% include "layui29/component/tables.html" with table_id="userTable" %}

<script>
layui.use('table', function(){
  layui.table.render({
    elem: '#userTable',
    url: '/api/users/',
    cols: [[
      {field: 'username', title: '用户名'},
      {field: 'email', title: '邮箱'}
    ]]
  });
});
</script>
```

## 示例项目
查看 `src/testapp/templates/` 目录中的完整示例：
- admin_example.html
- center_example.html
- tables.html
