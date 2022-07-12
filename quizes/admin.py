from django.contrib import admin
from django import forms
from django.contrib.admin.options import ModelAdmin, TabularInline, StackedInline

from .models import Quiz, BlockQuiz, Question, Answer, ResultAnswers, Result_answers, NewAnsvers, CauseModel

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    legend = forms.CharField(required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Quiz
        fields = '__all__'

class QuizAdmin(admin.ModelAdmin):
    model = Quiz

    list_filter = (
        'id',
        # 'gender',
    )

    form = PostAdminForm

class PostAdminForm(forms.ModelForm):
    legend = forms.CharField(required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Question
        fields = '__all__'


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

    list_filter = (
        'quiz',
    )
    search_fields = (
        'text',
    )

    form = PostAdminForm


class ResultAnswersAdmin(admin.ModelAdmin):
    model = ResultAnswers

    display_list = (
        'userID',
        'count',
    )


@admin.register(Result_answers)
class Result_answersAdmin(ModelAdmin):

    display_list = (
        'id',
        'uid',
        'count',
    )

    list_filter = (
        'uid',
        'count',
    )


    search_fields = (
        'uid',
    )

@admin.register(NewAnsvers)
class NewAnswersAdmin(ModelAdmin):
    list_display = (
        'userID',
        'count',
        'quiz',
        'question',
        'ansver_values'
    )

    list_filter = (
        # 'quiz',
        'count',
    )


class PostAdminForm(forms.ModelForm):
    text_body = forms.CharField(required=False, widget=CKEditorUploadingWidget())
    text_cause = forms.CharField(required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = CauseModel
        fields = '__all__'

@admin.register(CauseModel)
class CauseModelAdmin(admin.ModelAdmin):
    model = CauseModel

    search_fields = (
        'name',
    )

    list_filter = (
        'name',
    )

    form = PostAdminForm


admin.site.register(Quiz, QuizAdmin)
admin.site.register(BlockQuiz)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(ResultAnswers, ResultAnswersAdmin)
# admin.site.register(Result_answers, Result_answersAdmin)

