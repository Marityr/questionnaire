from django.urls import path
from .views import (
    HomePage,
    QuizView, 
    save_quiz,
    result_quiz,
)

app_name = 'quizes'

urlpatterns = [
    path('', HomePage.as_view(), name='main-view'),
    path('<uid>/', QuizView.as_view(), name='quiz-view'),
    path('<uid>/save/', save_quiz, name='quiz-save'),
    path('<uid>/result/', result_quiz, name='quiz-result'),
]

