from django.urls import path
from . import views

urlpatterns = [

    path('home', views.home , name='home'),
    path('question/<int:id>', views.question , name='question'),
    # path('logout', views.auth_logout , name='logout'),
]
