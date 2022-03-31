from django.contrib import admin
from django import forms

from .models import Quiz, BlockQuiz

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    legend = forms.CharField(required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Quiz
        fields = '__all__'

class QuizAdmin(admin.ModelAdmin):
    model = Quiz

    list_filter = (
        'title_block',
        # 'gender',
    )

    form = PostAdminForm


admin.site.register(Quiz, QuizAdmin)
admin.site.register(BlockQuiz)