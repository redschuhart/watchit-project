from django.shortcuts import render, HttpResponse, Http404

# Create your views here.


def register(request):
    return render(request, template_name='users/register.html')


def signin(request):
    return render(request, template_name='users/signin.html')