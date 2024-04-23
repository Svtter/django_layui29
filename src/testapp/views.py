from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class NormalLayout(TemplateView):
    template_name = "testapp/normal_example.html"


class CenterLayout(TemplateView):
    template_name = "testapp/center_example.html"


class AdminLayout(TemplateView):
    template_name = "testapp/admin_example.html"
