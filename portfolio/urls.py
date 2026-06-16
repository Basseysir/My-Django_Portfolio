# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Empty string means the homepage (http://127.0.0.1:8000/)
]