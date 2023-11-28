from django.shortcuts import render

# Create your views here.

TEMPLATE_PATH = 'watchstore/'

def index(request):
    context = {
        'title': "Главная Страница"
    }
    return render(request, template_name=TEMPLATE_PATH+'index.html', context=context)


def about(request):
    return render(request, template_name=TEMPLATE_PATH+'about.html')

