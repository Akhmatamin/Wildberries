from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet,basename='users')
router.register(r'review', ReviewViewSet,basename='reviews')




urlpatterns = [
    path('',include(router.urls)),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('product/',ProductListAPIView.as_view(),name='product-list'),
    path('product/<int:pk>/',ProductDetailAPIView.as_view(),name='product_detail'),
    path('category/',CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:pk>/',CategoryDetailAPIView.as_view(),name='category_detail'),
    path('sub_category/',SubCategoryListAPIView.as_view(),name='sub_category_list'),
    path('sub_category/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='sub_category_detail'),
    path('cart/',CartViewSet.as_view(),name='cart_detail'),
    path('cart_items/',CartItemViewSet.as_view({'get':'list','post':'create'})),
    path('Cart_items/<int:pk>/',CartItemViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
]