from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.Blog, name = 'blog'), 
    path('<int:num>', views.Blog, name = 'blog'), 
    path('news/', views.news, name = 'blog'), 
    path('news<int:num>/', views.news, name = 'blog'), 
]