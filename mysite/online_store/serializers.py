from rest_framework import serializers
from .models import User,Category,Product,ProductImage,SubCategory,Review,Cart,CartItem
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name',
                  'age','phone_number','status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect username or password")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user' : {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }




class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']


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

class ReviewSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(format='%d-%m-%Y')
    user = UserSimpleSerializer()
    class Meta:
        model = Review
        fields = ['user','rating','comment','date_added']


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(read_only=True, many=True)
    date_added = serializers.DateField(format='%d-%m-%Y')
    sub_category = SubCategorySerializer()
    all_reviews = ReviewSerializer(read_only=True, many=True)


    class Meta:
        model = Product
        fields = ['id','images','product_video','product_name','price','original','sub_category','description',
                  'article_num','date_added','all_reviews']

class SubCategoryDetailSerializer(serializers.ModelSerializer):
    products_sub_category = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = SubCategory
        fields = ['sub_category_name','products_sub_category']



class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),
                                                    write_only=True,source='product')
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['id','product','product_id','quantity','total_price']

    def get_total_price(self,obj):
        return obj.get_total_price()


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id','user','items','total_price']

    def get_total_price(self,obj):
        return obj.get_total_price()
