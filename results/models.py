from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User

class Result(models.Model):
    """Результат"""

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self) -> str:
        return str(self.pk)

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
