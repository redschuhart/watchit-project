from django.shortcuts import render, redirect, HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cart.forms import UserCartForm
from cart.models import ShoppingCart
from products.models import Product


# Create your views here.
@login_required
def open_cart(request):
    context = {
        'title': 'Корзина'
    }
    return render(request, template_name='cart/cart.html')


@login_required
def add_product(request):
    user_id = request.user
    product_id = request.POST.get('product_id')

    if request.method == 'POST':
        form = UserCartForm(data={
            'user_id': user_id,
            'product_id': product_id
        })
        print(request.POST)
        if form.is_valid():
            data, is_created = ShoppingCart.objects.get_or_create(
                user_id=user_id,
                product_id=Product.objects.get(product_id=product_id)
            )
            if not is_created:
                data.quantity += 1
                data.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        raise Http404

    raise Http404
