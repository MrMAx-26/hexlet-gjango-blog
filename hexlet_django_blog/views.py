from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse


class HomePageView(TemplateView):
    template_name = "base.html"
    

def about(request):
    return render(request, "about.html")