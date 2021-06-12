from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "pages/homes.html", context)


def post_page(request, post_id):
    context = {
        'post': Post.objects.get(id=post_id)
    }
    return render(request, "pages/post.html", context)
