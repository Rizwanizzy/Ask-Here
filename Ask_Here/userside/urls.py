from django.urls import path
from . import views

urlpatterns = [

    path('home', views.home , name='home'),
    path('question/<int:id>', views.question , name='question'),
    path('like-answer', views.like_answer, name='like_answer'),
    path('profile', views.profile, name='profile'),
]
