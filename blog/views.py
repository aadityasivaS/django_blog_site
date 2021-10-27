from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    paginate_by = 10
    model = Post
    template_name = "list.html"


def postDetailView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "detail.html", {"post": post})
