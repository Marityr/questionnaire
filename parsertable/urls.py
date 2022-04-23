from django.urls import path
from django.conf import settings
from django.contrib.auth import login, logout
from .views import ParserTable, Problem_add

app_name = 'parsertable'

urlpatterns = [
    path('', ParserTable.as_view(), name='parstable'),
    path('problem/', Problem_add.as_view(), name='problem add'),
]

