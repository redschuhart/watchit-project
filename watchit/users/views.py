from django.shortcuts import render, HttpResponse, Http404, redirect
from users.forms import SigninForm, RegisterForm, ChangeUserForm
from users.models import User
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

    context = {
        'title': 'Профиль',
        'user': request.user

    }

    return render(request, template_name='users/profile.html', context=context)


@login_required
def change_profile(request):
    context = {
        'title': 'Изменить данные',
    }

    if request.method == 'POST':
        form = ChangeUserForm(data=request.POST, instance=request.user)
        print(form.changed_data)
        if form.is_valid():
            form.save()
            return redirect(to='profile')
        else:
            print('Not valid')
            context['errors'] = registration_err(request.POST)
    form = ChangeUserForm(instance=request.user)
    context['form'] = form
    return render(request, template_name='users/change_info.html', context=context)
