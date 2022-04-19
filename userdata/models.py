from pyexpat import model
from django.db import models


class UserData(models.Model):
    """Данные пользователя"""

    username = models.CharField(verbose_name='Никнейм', max_length=255, null=True, blank=True)
    age = models.CharField(verbose_name='Возраст', max_length=255, null=True, blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=255, null=True, blank=True)
    massa = models.CharField(verbose_name='Вес', max_length=255, null=True, blank=True)
    purpose = models.CharField(verbose_name='Цели', max_length=255, null=True, blank=True)
    decision = models.CharField(verbose_name='Решение', max_length=255, null=True, blank=True)
    problem = models.CharField(verbose_name='Проблемы', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователtq"

    def __str__(self):
        return f'{self.id}'

