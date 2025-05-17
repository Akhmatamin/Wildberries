from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserViewSet,basename='users')
router.register(r'review', ReviewViewSet,basename='reviews')




urlpatterns = [
    path('',include(router.urls)),
    path('product/',ProductListAPIView.as_view(),name='product-list'),
    path('product/<int:pk>/',ProductDetailAPIView.as_view(),name='product_detail'),
    path('category/',CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:pk>/',CategoryDetailAPIView.as_view(),name='category_detail'),
    path('sub_category/',SubCategoryListAPIView.as_view(),name='sub_category_list'),
    path('sub_category/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='sub_category_detail'),
]