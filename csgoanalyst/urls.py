from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from core.views import index, rating, description, analys

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main', index),
    path('rating', rating),
    path('description', description),
    path('analys', analys)
]
