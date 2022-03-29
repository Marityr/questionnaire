from django.urls import path
from .views import (
<<<<<<< Updated upstream
    QuizListView,
    QuizView,
    # quiz_view,
    # quiz_data_view,
    save_quiz_view,
=======
    HomePage,
    QuizView, 
    save_quiz,
    result_quiz,
>>>>>>> Stashed changes
)

app_name = 'quizes'

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<uid>/', QuizView.as_view(), name='quiz-view'),
<<<<<<< Updated upstream

    path('<pk>/save/', save_quiz_view, name='save-quiz-view'),
    # path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
=======
    path('<uid>/save/', save_quiz, name='quiz-save'),
    path('<uid>/result/', result_quiz, name='quiz-result'),
>>>>>>> Stashed changes
]

