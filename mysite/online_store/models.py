from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator,MaxValueValidator

class User(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(16),
                                                       MaxValueValidator(100)],null=True,blank=True)
    status_choices = (
        ('gold', 'gold'),
        ('silver', 'silver'),
        ('bronze', 'bronze'),
        ('normal', 'normal'),
    )

    status = models.CharField(choices=status_choices,default='normal')
    phone_number =PhoneNumberField(null=True,blank=True)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name},{self.last_name}"

class Category(models.Model):
    category_img = models.ImageField(upload_to='category_images/')
    category_name = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='sub_categories')
    sub_category_name = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.sub_category_name

class Product(models.Model):
    product_name = models.CharField(max_length=40)
    price = models.PositiveIntegerField()
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name='products_sub_category')
    original = models.BooleanField(default=False)
    description = models.TextField()
    product_video = models.FileField(upload_to='product_videos/',null=True,blank=True)
    article_num = models.PositiveIntegerField(unique=True)
    date_added = models.DateField(auto_now_add=True)

    def get_avg_rating(self):
        reviews = self.all_reviews.all()
        if reviews.exists():
            return round(sum([i.rating for i in reviews ]) / len(reviews),1)
        return 0

    def get_count_user(self):
        reviews = self.all_reviews.all()
        if reviews.exists():
            return reviews.count()
        return 0

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    product_img = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"{self.product},{self.product_img}"

class Review(models.Model): # коммент
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='all_reviews')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1,6)])
    comment = models.TextField()
    date_added = models.DateField(auto_now_add=True)


    def str(self):
        return f"{self.user},{self.product}"


class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"

    def get_final_price(self):
        return sum([i.get_total_price() for i in self.items.all() ])

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)


    def __str__(self):
        return f"{self.product},{self.quantity}"

    def get_total_price(self):
        return self.quantity * self.product.price


