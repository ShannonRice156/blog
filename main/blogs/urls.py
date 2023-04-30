'''A module which holds all url information for project'''

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('blog/<str:pk>/', views.blog, name="blog"),
]
