from pyexpat import model
from django.db import models


class UserData(models.Model):
    """Данные пользователя"""

    CHOICES = (
        ('ЖКТ', 'ЖКТ'),
        ('Кишечник', 'кишечник'),
        ('Другое', 'другое'),
    )

    username = models.CharField(verbose_name='Никнейм', max_length=255, null=True, blank=True)
    age = models.CharField(verbose_name='Возраст', max_length=255, null=True, blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=255, null=True, blank=True)
    massa = models.CharField(verbose_name='Вес', max_length=255, null=True, blank=True)
    purpose = models.CharField(verbose_name='Цели', max_length=255, null=True, blank=True)
    decision = models.CharField(verbose_name='Решение', max_length=255, null=True, blank=True)
    problem = models.BooleanField()
    problem_two = models.BooleanField()
    problem_fre = models.BooleanField()
    problem_foo = models.BooleanField()
    problem_fiv = models.BooleanField()
    problem_sex = models.BooleanField()
    problem_sev = models.BooleanField()
    problem_ech = models.BooleanField()
    problem_noi = models.BooleanField()
    problem_thn = models.BooleanField()
    problem_elv = models.BooleanField()
    problem_lav = models.BooleanField()
    problem_ulw = models.BooleanField()
    problem_flv = models.BooleanField()
    problem_fvt = models.BooleanField()

    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"

    def __str__(self):
        return f'{self.id}'

