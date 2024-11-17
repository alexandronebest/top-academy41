
from django.shortcuts import render, get_object_or_404
from .models import Post
# def blog(request):
#     posts = Post.objects.all()
#     return render(request, "list.html", {'posts': posts})


def blog(request):
    posts = Post.objects.all()
    return render(request, "myblog/templates/blog/post_list.html", {'posts': posts})