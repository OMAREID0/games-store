from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.ProductAddViewSet)


router2 = routers.DefaultRouter()
router2.register(r'', views.ProductViewSet)


urlpatterns = [
    path('', include(router2.urls)),
    path('add/', include(router.urls)),
    path('id/<int:product_id>/', views.ProductDetailByIdApiView.as_view(), name='Product by id'),
    path('category/<int:Category>/', views.ProductDetailByCategoryApiView.as_view(), name='Product by category'),
]
