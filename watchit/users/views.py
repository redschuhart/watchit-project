from django.shortcuts import render, HttpResponse, Http404, redirect
from users.forms import SigninForm, RegisterForm, User
from django.contrib import auth
from users.errors_generator import registration_err
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect(to='home')

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
    if request.user.is_authenticated:
        return redirect(to='home')
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


def logout(request):
    auth.logout(request)
    return redirect(to='home')


@login_required
def profile(request):
    user_data = User.objects.get(username=request.user)
    context = {
        'title': 'Профиль',
        'user': user_data

    }

    return render(request, template_name='users/profile.html', context=context)
