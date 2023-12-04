from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product, ProductBrand, ProductCategory
from django.http import Http404
# Create your views here.


def product(request, product_slug):
    print(product_slug)
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


def product_plug(request):
    raise Http404


def catalog(request, category_slug=None):
    categories = ProductCategory.objects.all()
    if not category_slug:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id__category_slug=category_slug)
    context = {
        'title': 'catalog',
        'products': products,
        'categories': categories

    }
    return render(request, template_name='products/catalog.html', context=context)


def category(request, category_slug):
    context = {

    }
    return render(request, template_name='products/category.html', context=context)