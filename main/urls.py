from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-quiz/', views.create_quiz, name='create_quiz'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('quiz/<int:pk>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/create_question/', views.create_question, name='create_question'),
]

