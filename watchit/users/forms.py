from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User


class SigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя пользователя',
            'type': 'texts',
            'id': 'username',
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
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя',
            'type': 'text',
            'id': 'inputFirstName'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите фамилию',
            'type': 'text',
            'id': 'inputLastName'
        }
    ))

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя пользователя',
            'type': 'text',
            'id': 'inputUsername',
            'aria-describedby': "usernameHelp"
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите адрес эл.почты',
            'type': 'text',
            'id': 'inputEmailAddress',
            'aria-describedby': "emailHelp"
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите пароль',
            'type': 'password',
            'id': 'inputPassword',
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Подтвердите пароль',
            'type': 'password',
            'id': 'inputConfirmPassword',
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email',
                  'first_name', 'last_name',)


class ChangeUserForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'type': 'text',
            'id': 'inputFirstName',
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'type': 'text',
        }
    ))

    phone_number = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'type': 'text',
        }
    ))
    delivery_address = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'type': 'text',
        }
    ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'delivery_address')
