"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   # ✅ path added
from news.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", ArticleListView.as_view(), name="home"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),

]
