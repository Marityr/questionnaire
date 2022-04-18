from django.urls import path
from django.conf import settings
from django.contrib.auth import login, logout
from .views import ParserTable

app_name = 'parsertable'

urlpatterns = [
    path('', ParserTable.as_view(), name='parstable'),
]

