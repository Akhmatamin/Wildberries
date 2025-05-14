from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserViewSet,basename='users')
router.register(r'category', CategoryViewSet,basename='category_list')
router.register(r'sub_category', SubCategoryViewSet,basename='sub_category')
router.register(r'review', ReviewViewSet,basename='reviews')




urlpatterns = [
    path('',include(router.urls)),
    path('product/',ProductListAPIView.as_view(),name='product-list'),
    path('product/<int:pk>/',ProductDetailAPIView.as_view(),name='product_detail'),
]