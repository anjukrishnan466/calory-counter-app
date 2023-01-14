"""focaloid_learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('food_index', views.food_index, name="food_index"),
    path('food_store', views.food_store, name="food_store"),
    path('food_edit/<int:pk>', views.food_edit, name="food_edit"),
    path('food_delete/<int:pk>/', views.food_delete, name="food_delete"),
    path('activity_index', views.activity_index, name="activity_index"),
    path('activity_store', views.activity_store, name="activity_store"),
    path('activity_edit/<int:pk>', views.activity_edit, name="activity_edit"),
    path('activity_delete/<int:pk>/',
         views.activity_delete, name="activity_delete"),
    path('food/', views.FoodViews.as_view()),
    path('food_approve/<int:pk>', views.food_approve, name="food_approve"),
    path('activity_approve/<int:pk>', views.activity_approve, name="activity_approve")



]
