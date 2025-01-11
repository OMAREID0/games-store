from rest_framework import routers
from django.urls import path, include
from . import views



router = routers.DefaultRouter()
router.register(r'add', views.CategoryAddViewSet )


urlpatterns = [
    path('', include(router.urls)),
    path('id/<int:category_id>/', views.CategoryDetailByIdApiView.as_view(), name='Category by id'),
    path('category_name/<str:category_name>/', views.CategoryDetailByNameApiView.as_view(), name='Category by category'),
]
