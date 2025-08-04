from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse


class HomePageView(TemplateView):
    template_name = 'base.html'


    def home(request):
        return render(request, "base.html")
    

def about(request):
    return render(request, "about.html")