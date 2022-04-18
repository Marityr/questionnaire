from django.urls import path
from django.conf import settings
from .views import FormProfile
  
app_name = 'userdata'

urlpatterns = [
    path('profile/', FormProfile.as_view(), name='profiles'),
]

