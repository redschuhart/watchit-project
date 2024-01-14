from django.db import models
from users.models import User
from products.models import Product


class ShoppingCart(models.Model):
    quantity = models.PositiveSmallIntegerField(blank=False, null=False, default=1,
                                                verbose_name='Колличество товара')
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE,
                                   verbose_name='Товар')
    created = models.DateTimeField(auto_now_add=True)

    def sum(self):
        return self.quantity * self.product_id.price

    def __str__(self):
        return f'{self.user_id.username}|{self.product_id.product_name}|{self.quantity}'
