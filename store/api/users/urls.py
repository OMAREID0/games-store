from rest_framework import routers
from django.urls import path, include
from .views import RegisterView, LoginView, UserView, LogoutView

router = routers.DefaultRouter()
router.register(r'', UserView)

urlpatterns = [
    path('users/register', RegisterView.as_view()),
    path('users/login', LoginView.as_view()),
    path('users/logout', LogoutView.as_view())
]