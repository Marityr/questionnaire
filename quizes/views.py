from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from django.views import View

from .models import Quiz, BlockQuiz
from questions.models import ResultAnswers, Result_answers

import json


class HomePage(View):

    def get(self, request) -> render:
        template_name = 'webpage/index.html'

        return render(request, template_name)

    def post(self, request) -> JsonResponse:
        if request.is_ajax():
            newuser = ResultAnswers()
            data = request.POST
            newuser.name = data['name']
            newuser.email = data['email']
            newuser.male = data['male']
            newuser.save()
        return JsonResponse({'uid': str(newuser)})


class QuizView(View):

    def get(self, request, uid):
        quiz_all = Quiz.objects.all()
        all_block = []
        # print(len(quiz_all))
        for item in quiz_all:
            quiz = Quiz.objects.get(pk=item.id)
            questions = []
            questions.append(str(item.title_block))
            questions.append(str(item.topic))
            for q in quiz.get_questions():
                answers = []
                answers.append(str(q))
                for a in q.get_answers():
                    # tmp = []
                    # tmp.append(a.text)
                    # tmp.append(a.id)
                    answers.append(a.text)
                    pass
                questions.append(answers)
            all_block.append(questions)
        context = {
            'questions': all_block,
        }

        return render(request, 'webpage/quiz.html', context)

    def post(self, request):
        if request.is_ajax():
            # data_ = request.POST
            # data_.pop('csrfmiddlewaretoken')
            # data_.pop('button')
            # print(request.POST)
            # print(data_)
            pass

        return JsonResponse({'text': 'works'})


def save_quiz(request, uid):
    if request.is_ajax():
        data = request.POST
        
        try:
            Result_answers.objects.get(
                uid=uid,
                questions=data['name_block']
            )
            result = {'Answers': 'not add'}
        except Result_answers.DoesNotExist:
            addanswer = Result_answers()
            addanswer.uid = uid
            addanswer.questions = data['name_block']
            addanswer.result = data['result_block']
            addanswer.save()
            result = {'Answers': 'add save'}

    return JsonResponse(result)
    

def result_quiz(request, uid):
    result_user = Result_answers.objects.filter(uid=uid)

    all_result = []
    for item in result_user:
        tmp = []
        tmp.append(item.questions)
        tmp.append(item.result)
        all_result.append(tmp)
    return JsonResponse({'result': all_result})
