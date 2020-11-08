from django.urls import path, re_path, register_converter
from . import views

urlpatterns = [
    path('login1', views.login1),
    path('home', views.home)
]