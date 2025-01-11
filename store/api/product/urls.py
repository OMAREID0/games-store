from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'add', views.ProductAddViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('id/<int:product_id>/', views.ProductDetailByIdApiView.as_view(), name='Product by id'),
    path('category/<int:category_id>/', views.ProductDetailByCategoryApiView.as_view(), name='Product by category'),
]