from django import forms
from cart.models import ShoppingCart


class UserCartForm(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        fields = ('user_id', 'product_id')
