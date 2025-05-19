from .models import Product
from django_filters.rest_framework import FilterSet

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'sub_category':['exact'],
            'price':['gt','lt'],
            'original':['exact'],
        }