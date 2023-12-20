from django.shortcuts import render, HttpResponse, Http404, redirect
from users.forms import SigninForm, RegisterForm
from django.contrib import auth
from users.errors_generator import registration_err

# Create your views here.


def register(request):
    form = RegisterForm()
    context = {
        'title': 'Регистрация',
        'form': form

    }

    if request.method == 'POST':
        post_data = request.POST
        register_form = RegisterForm(data=post_data)
        if register_form.is_valid():
            register_form.save()
            return redirect(to='signin')
        else:
            context['errors'] = registration_err(post_data)

    return render(request, template_name='users/register.html', context=context)


def signin(request):
    context = {
        'form': SigninForm(),
        'title': 'Войти'
    }

    if request.method == 'POST':
        post_data = request.POST
        user = auth.authenticate(username=post_data['username'], password=post_data['password'])
        if user:
            auth.login(request, user)
            return redirect(to='home')
        context['wrong_data'] = 'Не правильный логин или пароль'

    return render(request, template_name='users/signin.html', context=context)
