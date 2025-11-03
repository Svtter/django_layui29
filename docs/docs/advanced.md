# 高级配置和扩展 (PLANNING)

## 自定义主题
1. 覆盖默认样式：
```css
/* static/layui29/css/custom.css */
.layui-card {
  border-radius: 10px;
}
```

2. 在模板中引入自定义CSS：
```html
{% block css %}
<link rel="stylesheet" href="{% static 'layui29/css/custom.css' %}">
{% endblock %}
```

## 扩展组件
### 创建自定义组件
1. 在 `templates/layui29/component/` 下新建模板文件
2. 使用现有组件作为基础：
```html
<!-- templates/layui29/component/custom_widget.html -->
<div class="custom-widget">
  {% include "layui29/component/tables.html" with table_id=table_id %}
</div>
```

## 高级配置
### 全局配置
```python
# settings.py
LAYUI29_CONFIG = {
    'HTMX_VERSION': '1.9.4',
    'LAYUI_THEME': 'dark',  # 可选: default/dark
    'AUTO_INIT_JS': True    # 是否自动初始化JS
}
```

### 性能优化
1. 按需加载组件：
```javascript
layui.config({
  base: '/static/layui29/js/'
}).use(['table', 'layer'], function(){
  var table = layui.table;
  var layer = layui.layer;
});
```

## 与Django REST framework集成
```python
# serializers.py
from rest_framework import serializers

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

# views.py
from rest_framework.viewsets import ModelViewSet
from .serializers import DataSerializer

class DataViewSet(ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
```

## 多语言支持
1. 创建翻译文件：
```python
# app.py
from django.utils.translation import gettext_lazy as _

class Layui29Config(AppConfig):
    verbose_name = _('Layui29 Admin')
```

2. 在模板中使用：
```html
{% load i18n %}
<button>{% trans "Submit" %}</button>
