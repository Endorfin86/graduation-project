from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('mylinks/<str:username>', views.CreateLinks.as_view(), name='addlink'),
]