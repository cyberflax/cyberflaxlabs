from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.handle, name = 'service'),
    path('<int:num2>', views.handle, name = 'service'),

]