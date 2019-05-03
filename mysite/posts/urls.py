from django.urls import re_path, include, path
from django.views.generic import ListView, DetailView
from posts.models import Post

urlpatterns = [
    re_path('^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="posts/posts.html")),
    re_path('(?P<pk>(\d+))', DetailView.as_view(model=Post, template_name="posts/entry.html")),
]
