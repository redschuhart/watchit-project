from users import views
from django.urls import path


urlpatterns = [
    path('registration/', views.register, name='register'),
    path('signin/', views.signin, name='signin')
]