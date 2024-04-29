import django_tables2 as tables
from . import models


class SimpleTable(tables.Table):
    class Meta:
        model = models.SimpleModel
        template_name = "layui29/component/tables.html"
