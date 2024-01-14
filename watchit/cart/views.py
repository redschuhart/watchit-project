from django.shortcuts import render, redirect, HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cart.forms import UserCartForm
from cart.models import ShoppingCart
from products.models import Product


# Create your views here.
@login_required
def open_cart(request):
    products = (ShoppingCart.objects.filter(user_id=request.user).select_related
                ('product_id'))
    context = {
        'title': 'Корзина',
        'products': products
    }
    if products.exists():
        total_sum = 0
        for product in products:
            total_sum += product.product_id.price * product.quantity
        context['total'] = int(total_sum)

        total_quantity = 0
        for product in products:
            total_quantity += product.quantity
        context['total_quantity'] = total_quantity


    return render(request, template_name='cart/cart.html', context=context)


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
