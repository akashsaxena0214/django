from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout views
    path('accounts/', include('accounts.urls')),  # signup view
    path('', include('pages.urls')),  # homepage & static pages
]
