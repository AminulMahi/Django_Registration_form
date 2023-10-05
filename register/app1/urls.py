from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='mainpage'),
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.LogIn, name='login'),
    path('homepage/', views.HomePage, name='homepage'),
    path('logout/', views.LogOutPage, name='logout')
]