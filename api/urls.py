from django.contrib import admin
from django.urls import path
""" from . import views
urlpatterns = [
    path('', views.home),
    path('welcome/', views.welcome),
] """
# OR
from .views import home, welcome
urlpatterns = [
    path('', home),
    path('welcome/', welcome),
]