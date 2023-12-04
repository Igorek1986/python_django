from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from blogapp.models import Article

class ArticleListView(ListView):
    context_object_name = "articles"
    queryset = (
        Article.objects
        .select_related("author")
        .prefetch_related("category")
        .prefetch_related("tags")
        .defer("content")
    )


class ArticleCreateView(CreateView):
    model = Article
    fields = "title", "content", "author", "category", "tags"
    success_url = reverse_lazy("blogapp:articles_list")