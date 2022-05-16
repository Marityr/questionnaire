from django.urls import path
from django.conf import settings
from django.contrib.auth import login, logout
from .views import (
    HomePage,
    QuizView, 
    save_quiz,
    result_quiz,
    UserUid,
    Dashboard,
    LastPage,
    ResulrPage,
    NewSaveAnsver,
    NewResult,
    CountItr,
)

app_name = 'quizes'

urlpatterns = [
    path('', HomePage.as_view(), name='main-view'),
    path('home/', Dashboard.as_view(), name='home'),
    path('home/<uid>/', QuizView.as_view(), name='quiz-view'),
    path('home/<uid>/save/', save_quiz, name='quiz-save'),
    path('home/<uid>/result/', result_quiz, name='quiz-result'),
    path('user-data/<str:usermane>/', UserUid.as_view(), name='user-data'),
    path('final/', LastPage.as_view(), name='lastpage'),
    path('resultpages/<count>/', ResulrPage.as_view(), name='resultpages'),
    path('resultpage/<count>/', NewResult.as_view(), name='result-count'),
    path('home/<uid>/newsaveansver/', NewSaveAnsver.as_view(), name='newsaveansver'),
    path('counter/', CountItr.as_view(), name='counter'),
]

