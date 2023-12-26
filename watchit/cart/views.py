from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def open_cart(request):
    context = {
        'title': 'Корзина'
    }
    return render(request, template_name='cart/cart.html')
