from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

