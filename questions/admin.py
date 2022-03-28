from django.contrib import admin
from .models import Question, Answer, ResultAnswers, Result_answers


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


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

