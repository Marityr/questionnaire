from django.contrib import admin
from django import forms

from .models import Question, Answer, ResultAnswers, Result_answers

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    legend = forms.CharField(required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Question
        fields = '__all__'


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

    form = PostAdminForm


class ResultAnswersAdmin(admin.ModelAdmin):
    model = ResultAnswers

    display_list = (
        'userID'
    )


class Result_answersAdmin(admin.ModelAdmin):
    model = Result_answers

    display_list = (
        'uid'
    )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(ResultAnswers, ResultAnswersAdmin)
admin.site.register(Result_answers, Result_answersAdmin)

