from django.urls import path
from cart import views

urlpatterns = [
    path('', views.open_cart, name='cart_overview'),
    path('addproduct/', views.add_product, name='addproduct')
]
