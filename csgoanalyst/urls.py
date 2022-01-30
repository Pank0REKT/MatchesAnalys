from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from core.views import index, rating

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('rating', rating)
]
