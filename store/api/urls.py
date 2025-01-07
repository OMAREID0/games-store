from django.urls import path, include
from api import views


urlpatterns = [
    path('', views.home, name="home"),
    path('user/', include('api.users.urls')),
    path('category/', include('api.category.urls')),
]