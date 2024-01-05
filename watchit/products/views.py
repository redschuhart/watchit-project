from django.shortcuts import render
from products.models import Product, ProductBrand, ProductCategory
from django.http import Http404
# Create your views here.


def product(request, product_slug):
    data = Product.objects.filter(product_slug=product_slug).first()
    if data:
        context = {
            'data': data,
            'price': int(data.price),
            'new_price': int(int(data.price) * (1 -data.discount / 100))

        }
        print(data.main_image)
        return render(request, template_name='products/product_card.html', context=context)
    else:
        raise Http404


def catalog(request, category_slug=None):
    categories = ProductCategory.objects.all()
    products = Product.objects.all() if not category_slug else (
        Product.objects.filter(category_id__category_slug=category_slug))

    order_options = {
        'ASC': 'price',
        'DESC': '-price'
    }
    order_by = order_options.get(request.GET.get('ORDER-BY'))
    if order_by:
        products = products.order_by(order_by)
    context = {
        'title': 'Каталог',
        'products': products,
        'categories': categories

    }
    return render(request, template_name='products/catalog.html', context=context)
