from django.urls import path
from .views import (
    QuizListView,
    QuizView,
    # quiz_view,
    # quiz_data_view,
    # save_quiz_view,
)

app_name = 'quizes'

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', QuizView.as_view(), name='quiz-view'),

    # path('<pk>/save/', save_quiz_view, name='save-quiz-view'),
    # path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]

