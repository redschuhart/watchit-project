from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.


class ProductCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(blank=False, null=False, max_length=255)
    category_description = models.TextField(blank=None, null=None)


class ProductBrand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(blank=False, null=False, max_length=255)
    brand_description = models.TextField(blank=None, null=None)


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, unique=True, blank=False, null=False)
    time_create = models.TimeField(auto_now_add=True)
    time_update = models.TimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(blank=False, null=False, default=0)
    discount = models.PositiveIntegerField(blank=False, null=False, default=0, validators=[MaxValueValidator(100)])
    price = models.DecimalField(blank=False, null=False, max_digits=7, decimal_places=2)
    description = models.TextField(blank=False, null=False)
    main_image = models.ImageField(upload_to='products_images')
    made_in = models.CharField(blank=False, null=False, max_length=255)
    movement = models.CharField(blank=False, null=False, max_length=255)
    category_id = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    case_material = models.CharField(blank=False, null=False, max_length=255)
    color = models.CharField(blank=False, null=False, max_length=255)
    brand_id = models.ForeignKey(to=ProductBrand, on_delete=models.CASCADE)
    water_resistance = models.IntegerField(blank=False, null=False, validators=[MaxValueValidator(500)])
    backlight = models.BooleanField(blank=False, null=False)
    glass = models.CharField(blank=False, null=False, max_length=255)
    calendar_day = models.BooleanField(blank=False, null=False)
    calendar_date = models.BooleanField(blank=False, null=False)
    calendar_full = models.BooleanField(blank=False, null=False)
    size = models.CharField(blank=False, null=False, max_length=255)





