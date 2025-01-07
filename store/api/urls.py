from django.urls import path
from .views import getGameByCategoryid, getGameByCategoryName, add_game, modify_game, RegisterView, LoginView, UserView, LogoutView



urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('games/category/<str:name>', getGameByCategoryName, name='byname'),
    path('games/id/<int:id>', getGameByCategoryid, name='byid'),
    path('games/add/', add_game, name='add_game'),
    path('games/modify/id/<int:pk>', modify_game, name='modify_game'),
]