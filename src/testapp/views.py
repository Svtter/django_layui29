from django.shortcuts import render
from django.views.generic import TemplateView
import django_tables2 as tables
from .tables import SimpleTable
from . import models


# Create your views here.
class NormalLayout(TemplateView):
    template_name = "testapp/normal_example.html"


class CenterLayout(TemplateView):
    template_name = "testapp/center_example.html"


class AdminLayout(TemplateView):
    template_name = "testapp/admin_example.html"


class TableView(tables.SingleTableView):
    table_class = SimpleTable
    queryset = models.SimpleModel.objects.all()
    template_name = "testapp/tables.html"
