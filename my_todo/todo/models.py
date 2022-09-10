from operator import mod
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Todo(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Название задачи')
    description = models.CharField(max_length=250,
                                   verbose_name='Описание задачи')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата публикации')
    update_at = models.DateTimeField(auto_now=True,
                                     verbose_name='Обновлено')
    date_duo = models.DateTimeField()
    status = models.BooleanField()
