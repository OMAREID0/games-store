from rest_framework import routers
from django.urls import path, include
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('', UserView.as_view()),
]