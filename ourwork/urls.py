from django.contrib import admin
from django.urls import path,include
from . import views
from . models import ourwork_cat


    
urlpatterns = [
    path('', views.work, name = 'service'),
    path('<slug:num1>/', views.work, name = 'service'),

]