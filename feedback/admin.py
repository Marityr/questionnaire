from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(ModelAdmin):
    list_display = (
        'id',
        'userID',
        'email',
        'created_at',
        'rate'
    )

