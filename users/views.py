from django.shortcuts import render, redirect
from .forms import UserRegister
from .forms import UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ValidationError 
from django.contrib.auth.models import User

def registration(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно зарегистрирован')
            return redirect('login')
    else:
        form = UserRegister()
    return render(request, 'users/registration.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST, instance=request.user)
        if userForm.is_valid():
            userForm.save()
            messages.success(request, 'Профиль успешно обновлен')
            return redirect('profile')
    else:
        userForm = UserUpdateForm(instance=request.user)

    data = {
        'userForm': userForm,
    }
    return render(request, 'users/profile.html', data)

