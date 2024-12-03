from django.shortcuts import render
from project.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})

