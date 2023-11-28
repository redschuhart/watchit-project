from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def product(request, product_id):
    return HttpResponse(f"<h1>Hello id - {product_id}<h1>")