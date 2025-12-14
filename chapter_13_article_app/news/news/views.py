from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"
    login_url = "login"

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"
    login_url = "login"
    
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

class ArticleCreateView(PermissionRequiredMixin, CreateView):
    model = Article
    fields = ("title", "body")
    template_name = "article_new.html"
    permission_required = "news.add_article"

class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    model = Article
    fields = ("title", "body")
    template_name = "article_edit.html"
    permission_required = "news.change_article"

class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    permission_required = "news.delete_article"
