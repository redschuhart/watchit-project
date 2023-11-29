from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.


class ProductCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(blank=False, null=False, max_length=255)
    category_description = models.TextField(blank=None, null=None)

    def __str__(self):
        return f'{self.category_name}'


class ProductBrand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(blank=False, null=False, max_length=255)
    brand_description = models.TextField(blank=None, null=None)

    def __str__(self):
        return f"{self.brand_name}"


class ProductType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(blank=False, null=False, max_length=255)

    def __str__(self):
        return f"{self.type_name}"

class Product(models.Model):
#TODO add model number and backlight type, watch type field and model for watchtype
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True, blank=False, null=False)
    product_name = models.CharField(blank=False, null=False, max_length=255)
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
    backlight_type = models.CharField(blank=False, null=False, max_length=255)
    type_id = models.ForeignKey(to=ProductType, on_delete=models.CASCADE)
    glass = models.CharField(blank=False, null=False, max_length=255)
    calendar = models.CharField(max_length=255, default=False)
    size = models.CharField(blank=False, null=False, max_length=255)
    sex = models.CharField(blank=False, null=False, max_length=255, default='Мужские')

    def __str__(self):
        return f'{self.product_name}'




