from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('<slug:num1>/', views.handle, name = 'service'),
    path('<slug:num1>/<slug:num2>', views.handle, name = 'service'),

]