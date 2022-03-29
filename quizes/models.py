from django.db import models


GENDER_CHOICES = (
    ('all', 'all'),
    ('man', 'man'),
    ('woman', 'woman'),
)

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

class Quiz(models.Model):
    """Опрос"""

    title_block = models.ForeignKey(BlockQuiz, on_delete=models.CASCADE)
    topic = models.CharField(max_length=120)
    legend = models.TextField(verbose_name='Легенда вопроса', blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='all')

    def __str__(self) -> str:
        return f"{self.title_block}-{self.topic}"

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'