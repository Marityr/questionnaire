from django.db import models
from quizes.models import Quiz


class Question(models.Model):
    """Вопросы"""

    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.text)

    def answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    """Ответы"""

    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"вопрос: {self.question.text}, ответ: {self.text}, правильный: {self.correct}"

    class Meta:
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'
