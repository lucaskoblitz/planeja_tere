from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publications/', views.Publications, name='publications'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
]