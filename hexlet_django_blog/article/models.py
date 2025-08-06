from django.db import models
from django.forms import ModelForm


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["name", "body"]