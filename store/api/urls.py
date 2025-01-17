from django.urls import path, include
from api import views


urlpatterns = [
    path('', views.home, name="home"),
    path('user/', include('api.users.urls')),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('order/', include('api.order.urls')),
]