from django.urls import path
from . import views
from django.contrib.auth import views as logViews

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('login', logViews.LoginView.as_view(template_name='users/login.html'),  name='login'),
    path('logout', logViews.LogoutView.as_view(template_name='users/logout.html'),  name='logout'),
    path('profile', views.profile, name='profile'),
]
