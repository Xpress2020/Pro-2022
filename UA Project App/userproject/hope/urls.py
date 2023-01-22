from django.contrib import admin
from django.urls import path, include
from hope import views

urlpatterns = [
    path('',views.index, name="hope"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
]
