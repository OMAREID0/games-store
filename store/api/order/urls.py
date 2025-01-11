from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.OrderViewSet)

urlpatterns = [
    path('create/', views.CreateOrderView.as_view(), name='order'),
    path('', include(router.urls))
]
