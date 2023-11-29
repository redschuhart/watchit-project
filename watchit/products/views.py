from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product, ProductBrand, ProductCategory
from django.http import Http404
# Create your views here.


def product(request, product_id):
    data = Product.objects.filter(product_id=product_id).first()
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

def test(request):
    return render(request, template_name='products/index.html')