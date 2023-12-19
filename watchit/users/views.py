from django.shortcuts import render, HttpResponse, Http404, redirect
from users.forms import SigninForm, RegisterForm
from django.contrib import auth


# Create your views here.


# TODO register form
def register(request):
    if request.method == 'POST':
        post_data = request.POST

    else:
        return render(request, template_name='users/register.html')



def signin(request):
    context = {
        'form': SigninForm()
    }
    if request.method == 'POST':
        post_data = request.POST
        user = auth.authenticate(username=post_data['username'], password=post_data['password'])
        if user:
            auth.login(request, user)
            return redirect(to='home')
        context['wrong_data'] = 'Не правильный логин или пароль'


    return render(request, template_name='users/signin.html', context=context)
