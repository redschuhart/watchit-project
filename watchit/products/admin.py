from django.contrib import admin
from products.models import ProductBrand, ProductCategory, Product, ProductType
# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductBrand)
admin.site.register(ProductType)
