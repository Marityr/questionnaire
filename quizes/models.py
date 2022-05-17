from django.db import models
import uuid


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

    title_block = models.ForeignKey('BlockQuiz', on_delete=models.CASCADE)
    topic = models.CharField(max_length=120)
    legend = models.TextField(verbose_name='Легенда вопроса', blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='all')
    low = models.CharField(max_length=120, verbose_name='low', default=0, blank=True, null=True)
    medium = models.CharField(max_length=120, verbose_name='medium', default=0, blank=True, null=True)
    hard = models.CharField(max_length=120, verbose_name='hard', default=0, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.topic}"

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    """Вопросы"""

    text = models.CharField(max_length=200)
    legend = models.TextField(verbose_name='Легенда вопроса', blank=True, null=True)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
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
    cause = models.CharField(max_length=200, blank=True, null=True)
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
    cause = models.CharField(max_length=200, blank=True, null=True)
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
    causes = models.CharField(max_length=200)
    result = models.CharField(max_length=20)
    count = models.CharField(verbose_name='Количество попыток', default=1, max_length=20)
    color = models.CharField(max_length=200, default='notcolor', blank=True, null=True)

    def __str__(self) -> str:
        return str(self.uid)

    class Meta:
        verbose_name = 'Результат ответов'
        verbose_name_plural = 'Результаты ответов'


class NewAnsvers(models.Model):
    """Новая схема сохранения результатов с количеством попыток для отчетности"""

    userID = models.CharField(verbose_name='Идентификатор', max_length=255)
    count = models.CharField(verbose_name='Попытка', max_length=255)
    quiz = models.CharField(verbose_name='Опросник', max_length=255)
    question = models.CharField(verbose_name='Вопрос', max_length=255)
    ansver_values = models.CharField(verbose_name='Ответ', max_length=255)
    cause = models.CharField(verbose_name='Потологии', max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.userID

    class Meta:
        verbose_name = 'NEW Результат ответов'
        verbose_name_plural = 'NEW Результаты ответов'
