from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': "Главная Страница"
    }
    return render(request, template_name='watchstore/index.html', context=context)


def about(request):
    return render(request, template_name='watchstore/about.html')

