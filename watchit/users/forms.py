from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class SigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя пользователя',
            'type': 'texts',
            'id': 'username'
        }
    ))
    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите пароль',
            'type': 'password',
            'id': 'password'
        }
    ))
    class Meta:
        model = User
        fields = ('username', 'password',)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'phone_number',
                  'first_name', 'last_name', )