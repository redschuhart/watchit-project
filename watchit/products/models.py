from django.db import models
from django.core.validators import MaxValueValidator


class ProductCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(blank=False, null=False, max_length=255,
                                     verbose_name='Название категории')
    category_slug = models.CharField(max_length=255, blank=False, null=False,
                                     verbose_name='Слаг категории')
    category_description = models.TextField(blank=None, null=None,
                                            verbose_name='Описание категории')

    def __str__(self):
        return f'{self.category_name}'


class ProductBrand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(blank=False, null=False, max_length=255,
                                  verbose_name='Название бренда')
    brand_description = models.TextField(blank=None, null=None,
                                         verbose_name='Описание бренда')

    def __str__(self):
        return f"{self.brand_name}"


class ProductType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(blank=False, null=False, max_length=255,
                                 verbose_name='Тип часов')

    def __str__(self):
        return f"{self.type_name}"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True, blank=False, null=False)
    product_name = models.CharField(blank=False, null=False, max_length=255, unique=True,
                                    verbose_name='Название'
                                    )
    product_slug = models.CharField(max_length=255, null=False, blank=False,
                                    verbose_name='Модель товара'
                                    )
    time_create = models.TimeField(auto_now_add=True)
    time_update = models.TimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(blank=False, null=False, default=0,
                                           verbose_name='Колличество на складе'
                                           )
    short_description = models.TextField(blank=False, null=False,
                                         verbose_name='Краткое описание'
                                         )

    discount = models.PositiveIntegerField(blank=False, null=False, default=0,
                                           validators=[
                                               MaxValueValidator(50, message='Скидка не может быть больше 100%')],
                                           verbose_name='Размер скидки в %'
                                           )
    price = models.DecimalField(blank=False, null=False, max_digits=12,
                                decimal_places=2, verbose_name='Цена'
                                )
    description = models.TextField(blank=False, null=False, verbose_name='Описание товара')
    main_image = models.ImageField(upload_to='products_images', verbose_name='Фото'
                                   )
    made_in = models.CharField(blank=False, null=False, max_length=255,
                               verbose_name='Страна производства'
                               )
    movement = models.CharField(blank=False, null=False, max_length=255,
                                verbose_name='Механизм')
    category_id = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE,
                                    verbose_name='Категория')
    case_material = models.CharField(blank=False, null=False, max_length=255,
                                     verbose_name='Материал корпуса'
                                     )
    color = models.CharField(blank=False, null=False, max_length=255,
                             verbose_name='Цвет'
                             )
    brand_id = models.ForeignKey(to=ProductBrand, on_delete=models.CASCADE,
                                 verbose_name='Название бренда'
                                 )
    water_resistance = models.IntegerField(blank=False, null=False,
                                           validators=[MaxValueValidator(500)],
                                           verbose_name='Водозащита в метрах')
    backlight = models.BooleanField(blank=False, null=False,
                                    verbose_name='Подсветка')
    backlight_type = models.CharField(blank=False, null=False, max_length=255,
                                      verbose_name='Тип подсветки'
                                      )
    type_id = models.ForeignKey(to=ProductType, on_delete=models.CASCADE,
                                verbose_name='Тип часов'
                                )
    glass = models.CharField(blank=False, null=False, max_length=255,
                             verbose_name='Стекло'
                             )
    calendar = models.CharField(max_length=255, default=False,
                                verbose_name='Календарь'
                                )
    size = models.CharField(blank=False, null=False, max_length=255,
                            verbose_name='Размеры')
    sex = models.CharField(blank=False, null=False, max_length=255,
                           verbose_name='Мужские/женские'
                           )

    def __str__(self):
        return f'{self.product_name}'
