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


# TODO post data verification
def signin(request):
    if request.method == 'POST':
        post_data = request.POST
        user = auth.authenticate(username=post_data['username'], password=post_data['password'])
        if user:
            auth.login(request, user)
            return render(request, template_name='users/success_signin.html')
        return render(request, template_name='users/fail_signin.html')
    else:
        context = {
            'form': SigninForm()
        }
        print(request.user.is_authenticated)
        return render(request, template_name='users/signin.html', context=context)
