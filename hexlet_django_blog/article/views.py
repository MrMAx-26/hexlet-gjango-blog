from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(
        request,
        "articles/indexx.html",
        context={
            "name": "Article",
        },
    )