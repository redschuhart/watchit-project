from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from users.field_validators import phone_validator

class User(AbstractUser):
    phone_number = models.CharField(max_length=12, validators=[phone_validator],
                                     verbose_name='Номер телефона')
    delivery_address = models.TextField(verbose_name='Адрес доставки', blank=True, null=True)
    user_avatar = models.ImageField(upload_to='users_images', blank=True, null=True,
                                    verbose_name='Фото профиля')






