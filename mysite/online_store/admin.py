from django.contrib import admin
from .models import User,Category,SubCategory,Product,Review,Cart,CartItem,ProductImage

admin.site.register(User)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ProductImage)
