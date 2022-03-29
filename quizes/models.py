from django.db import models


DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

<<<<<<< Updated upstream
=======
class BlockQuiz(models.Model):

    #TODO добавить легенду и блок промежутоыного текста
    title = models.CharField(max_length=120, verbose_name='Название блока')
    low = models.CharField(max_length=120, verbose_name='low', default=0, editable=False)
    medium = models.CharField(max_length=120, verbose_name='medium', default=0, editable=False)
    hard = models.CharField(max_length=120, verbose_name='hard', default=0, editable=False)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

>>>>>>> Stashed changes
class Quiz(models.Model):
    """Опрос"""

    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text='время на тест')
    required_scoore_to_pass = models.IntegerField(help_text='нужный результат в %')
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self) -> str:
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'