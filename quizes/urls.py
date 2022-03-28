from django.urls import path
from .views import (
    QuizListView,
    QuizView,
    save_quiz_view,
    result_answers,
)

app_name = 'quizes'

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<str:uid>/', QuizView.as_view(), name='quiz-view'),

    path('<str:uid>/save/', save_quiz_view, name='save-quiz-view'),
    path('<str:uid>/result/', result_answers, name='result-quiz-view'),
    # path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]

