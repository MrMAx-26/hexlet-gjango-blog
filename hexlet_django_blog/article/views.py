from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/indexx.html",
            context={
                "articles": articles,
            },
        )
        
