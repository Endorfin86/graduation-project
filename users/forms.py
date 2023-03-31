from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError 


class UserRegister(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )

    email = forms.EmailField(
        label='Почта',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Введите почту'})
    )

    password1 = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
    
    def __init__(self, *args, **kwargs):
        super(UserRegister, self).__init__(*args, **kwargs)
        del self.fields['password2']
        

class UserUpdateForm(forms.ModelForm):
     
    username = forms.CharField(
        required=True,
        label='Логин',
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )

    email = forms.EmailField(
        required=True,
        label='Почта',
        widget=forms.TextInput(attrs={'placeholder': 'Введите почту'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']