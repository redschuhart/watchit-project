from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_plug, name='product'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:category_slug>/', views.catalog),
    path('<slug:product_slug>/', views.product),

]