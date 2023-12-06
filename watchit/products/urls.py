from django.urls import path
from products import views


urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:category_slug>/', views.catalog, name='category'),
    path('<slug:product_slug>/', views.product, name='product_card'),

]