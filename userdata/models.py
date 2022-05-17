from pyexpat import model
from django.db import models


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Non-binary', 'Non-binary'),
    ('Transgender', 'Transgender'),
    ('Intersex', 'Intersex'),
    ('I prefer not to say', 'I prefer not to say'),
    ('Other', 'Other'),
)

class UserData(models.Model):
    """Данные пользователя"""

    CHOICES = (
        ('ЖКТ', 'ЖКТ'),
        ('Кишечник', 'кишечник'),
        ('Другое', 'другое'),
    )

    username = models.CharField(verbose_name='Никнейм', max_length=255, null=True, blank=True)
    age = models.CharField(verbose_name='Возраст', max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='all')
    massa = models.CharField(verbose_name='Вес', max_length=255, null=True, blank=True)
    purpose = models.CharField(verbose_name='Цели', max_length=255, null=True, blank=True)
    decision = models.CharField(verbose_name='Решение', max_length=255, null=True, blank=True)

    count = models.CharField(verbose_name='Количество попыток', default=1, max_length=20)

    problem = models.BooleanField(verbose_name='1', null=True, blank=True)
    problem_two = models.BooleanField(verbose_name='2',  null=True, blank=True)
    problem_fre = models.BooleanField(verbose_name='3',  null=True, blank=True)
    problem_foo = models.BooleanField(verbose_name='4',  null=True, blank=True)
    problem_fiv = models.BooleanField(verbose_name='5',  null=True, blank=True)
    problem_sex = models.BooleanField(verbose_name='6',  null=True, blank=True)
    problem_sev = models.BooleanField(verbose_name='7',  null=True, blank=True)
    problem_ech = models.BooleanField(verbose_name='8',  null=True, blank=True)
    problem_noi = models.BooleanField(verbose_name='9',  null=True, blank=True)
    problem_thn = models.BooleanField(verbose_name='10',  null=True, blank=True)
    problem_elv = models.BooleanField(verbose_name='11',  null=True, blank=True)
    problem_lav = models.BooleanField(verbose_name='13',  null=True, blank=True)
    problem_ulw = models.BooleanField(verbose_name='14',  null=True, blank=True)
    problem_flv = models.BooleanField(verbose_name='15',  null=True, blank=True)
    problem_fvt = models.BooleanField(verbose_name='16',  null=True, blank=True)

    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"

    def __str__(self):
        return f'{self.username}'

