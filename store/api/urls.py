from django.urls import path, include
from .views import getGameByCategoryid, getGameByCategoryName, add_game, modify_game, RegisterView, LoginView, UserView, LogoutView



urlpatterns = [
    path('user/', include('api.users.urls')),
    path('category/', include('api.category.urls')),
]