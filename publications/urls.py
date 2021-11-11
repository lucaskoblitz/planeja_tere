from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publicações/', views.Publications, name='publications'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('registre-se/', views.registerPage, name='register'),
    path('associe-se/', views.sejaAssociado, name='associe'),
    path('solicitar_publicação/', views.solicitar_pub.as_view(), name='solicitarpublicação'),
    path('post_com_sucesso/', TemplateView.as_view(template_name='publications/post_sucesso.html'))
]