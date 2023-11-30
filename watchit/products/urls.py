from django.urls import path
from products import views

urlpatterns = [
    path('test/', views.test),
    path('<slug:product_slug>/', views.product),

]