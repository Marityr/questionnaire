from tabnanny import verbose
from django.db import models
from quizes.models import Quiz

import uuid


MALE_CHOICES = (
    ('all', 'all'),
    ('man', 'man'),
    ('woman', 'woman'),
)


class Question(models.Model):
    """Вопросы"""

    text = models.CharField(max_length=200)
    male = models.CharField(max_length=6, choices=MALE_CHOICES, default=all, blank=True, null=True)
    step = models.IntegerField(verbose_name='Позиция в опросе', blank=True, null=True, default=0)
    legend = models.TextField(verbose_name='Легенда вопроса', blank=True, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    """Ответы"""

    text = models.CharField(max_length=200)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    tultype = models.TextField(verbose_name='Подсказка к ответу', blank=True, null=True)
    min_bal = models.IntegerField(verbose_name='Минимальное значение ответа', default=0)
    max_bal = models.IntegerField(verbose_name='Максимальное значение ответа')
=======
    #TODO добавить значение ответов
>>>>>>> Stashed changes
=======
    #TODO добавить значение ответов
>>>>>>> Stashed changes
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"ID - {self.id} | вопрос: {self.question.text}, вариант: {self.text}"

    class Meta:
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'


class ResultAnswers(models.Model):
    """Результаты ответа для статистики"""

    def random_number():
        import random
        rand = random.randrange(1000, 10001, 1)
        return rand

    userID = models.UUIDField(verbose_name='Идентификатор', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Имя пользователя', max_length=10)
    male = models.CharField(verbose_name='Пол пользователя', max_length=10)
    email = models.CharField(verbose_name='Email пользователя', max_length=10, null=True)
    questuins = models.TextField(verbose_name='Пройденые ответы')
    answers = models.TextField(verbose_name='Ответы пользователя')
    result_bal = models.CharField(verbose_name='Результат для подсчета', max_length=10)

    def __str__(self) -> str:
        return f"{self.userID} - {self.male} - {self.result_bal}"

    class Meta:
        verbose_name = 'Результат ответов'
        verbose_name_plural = 'Результаты ответов'

