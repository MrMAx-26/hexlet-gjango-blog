from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


class IndexView(View):


    def get(self, request, *args, **kwargs):
        return HttpResponse("My app name is Hexlet-blog")
        

def index(request, tags: str, article_id: int):
    context = {
        'article_id': article_id,
        'tags': tags
    }
    return render(request, 'articles/indexx.html', context)
