from django.urls import path
from products import views

urlpatterns = [
    path('<int:product_id>/', views.product)
]