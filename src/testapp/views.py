from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class CenterLayout(TemplateView):
    template_name = "testapp/center_example.html"