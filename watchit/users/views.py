from django.shortcuts import render, HttpResponse, Http404
from users.forms import SigninForm, RegisterForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        data = request.POST
        return HttpResponse("<h1>Sucess<h1>")
    return render(request, template_name='users/register.html')


def signin(request):
    if request.method == 'POST':
        data = request.POST
        return HttpResponse("<h1>Sucess<h1>")
    else:
        context = {
            'form': SigninForm()
        }
        print(context['form'])
        return render(request, template_name='users/signin.html', context=context)


