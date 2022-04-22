from django.shortcuts import render
from django.views.generic import (
    TemplateView
)

# Create your views here.

class IndexHomeView(TemplateView):
    template_name = "home/index.html"

class DashboardIndexView(TemplateView):
    template_name = "dashboard/dashboard_index.html"
