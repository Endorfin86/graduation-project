from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse

class Links(models.Model):
    fulllink = models.CharField('Длинная ссылка', max_length=250)
    shortlink = models.CharField('Сокращенная ссылка', max_length=100, unique=True)
    creator = models.ForeignKey(User, verbose_name='Создатель', on_delete=models.CASCADE)

    def __str__(self):
        return f'/link/{self.shortlink}'
    # Напиши тест для этой функции основываясь на библиотеке Pytest   
    def get_absolute_url(self):
        return reverse('addlink', kwargs={'username': self.creator})

    class Meta:
       verbose_name = 'Ссылка' 
       verbose_name_plural = 'Ссылки' 
