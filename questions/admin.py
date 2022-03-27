from django.contrib import admin
from .models import Question, Answer, ResultAnswers


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


class ResultAnswersAdmin(admin.ModelAdmin):
    model = ResultAnswers

    display_list = (
        'userID'
    )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(ResultAnswers, ResultAnswersAdmin)

