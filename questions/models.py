from tabnanny import verbose
from django.db import models
from quizes.models import Quiz

import uuid


class Question(models.Model):
    """Вопросы"""

    text = models.CharField(max_length=200)
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
    value_answer = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"ID - {self.id} | вопрос: {self.question.text}, вариант: {self.text}"

    class Meta:
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'


class ResultAnswers(models.Model):
    """Данные участников"""

    userID = models.UUIDField(verbose_name='Идентификатор', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Имя пользователя', max_length=10)
    gender = models.CharField(verbose_name='Пол пользователя', max_length=10)
    email = models.CharField(verbose_name='Email пользователя', max_length=10, null=True)

    def __str__(self) -> str:
        return f"{self.userID} - {self.gender}"

    class Meta:
        verbose_name = 'Учасник'
        verbose_name_plural = 'Участники'


class Result_answers(models.Model):
    
    uid = models.CharField(max_length=200)
    questions = models.CharField(max_length=500)
    result = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.uid)

    class Meta:
        verbose_name = 'Результат ответов'
        verbose_name_plural = 'Результаты ответов'
