# 组件使用文档

## 表格组件

### 基本用法
```html
{% include "layui29/component/tables.html" with table_id="dataTable" %}

<script>
layui.use('table', function(){
  layui.table.render({
    elem: '#dataTable',
    url: '/api/data/',
    cols: [[
      {field: 'id', title: 'ID', width: 80},
      {field: 'name', title: '名称'},
      {field: 'status', title: '状态'}
    ]]
  });
});
</script>
```

### 配置选项
| 参数 | 类型 | 说明 |
|------|------|------|
| elem | string | 表格容器选择器 |
| url | string | 数据接口地址 |
| cols | array | 表头配置 |
| page | bool/object | 分页配置 |
| toolbar | string | 工具栏模板 |
| defaultToolbar | array | 默认工具栏 |

### 分页表格
```javascript
layui.table.render({
  elem: '#pagedTable',
  url: '/api/paged-data/',
  page: true,
  cols: [[
    {field: 'id', title: 'ID'},
    {field: 'username', title: '用户名'}
  ]]
});
```

### 工具栏
```javascript
layui.table.render({
  elem: '#toolTable',
  toolbar: '#toolbarDemo',
  cols: [[
    {field: 'id', title: 'ID'},
    {field: 'content', title: '内容'}
  ]]
});
```

### 表格事件
```javascript
layui.table.on('tool(dataTable)', function(obj){
  var data = obj.data;
  var layEvent = obj.event;
  
  if(layEvent === 'edit'){
    layer.msg('编辑操作: '+ JSON.stringify(data));
  }
});
