from rest_framework import serializers
from .models import User,Category,Product,ProductImage,SubCategory,Review,Cart,CartItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name','category_img']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['sub_category_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name','sub_categories']


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id','sub_category_name']



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product_img']



class ProductListSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(read_only=True, many=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_user = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id','images','product_name','price','original','get_avg_rating','get_count_user']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_user(self,obj):
        return obj.get_count_user()


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(read_only=True, many=True)
    date_added = serializers.DateField(format='%d-%m-%Y')
    sub_category = SubCategorySerializer()

    class Meta:
        model = Product
        fields = ['id','images','product_video','product_name','price','original','sub_category','description','article_num','date_added']

class SubCategoryDetailSerializer(serializers.ModelSerializer):
    products_sub_category = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = SubCategory
        fields = ['sub_category_name','products_sub_category']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

