from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.work, name = 'service'),
    path('<int:num2>', views.work, name = 'service'),

]