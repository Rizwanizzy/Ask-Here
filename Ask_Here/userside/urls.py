from django.urls import path
from . import views

urlpatterns = [

    path('home', views.home , name='home'),
    # path('register', views.auth_register , name='register'),
    # path('logout', views.auth_logout , name='logout'),
]