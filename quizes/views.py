from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from django.views import View

from .models import Quiz, BlockQuiz
from questions.models import Question, ResultAnswers, Result_answers

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
        for item in quiz_all:
            quiz = Quiz.objects.get(pk=item.id)
            questions = []
            questions.append(str(item.title_block))
            questions.append(str(item.topic))
            questions.append(str(item.legend))
            for q in quiz.get_questions():
                answers = []
                answers.append(str(q))
                for a in q.get_answers():
                    tmp = []
                    tmp.append(a.value_answer)
                    tmp.append(a.text)
                    answers.append(tmp)
                    pass
                questions.append(answers)
            all_block.append(questions)
        context = {
            'questions': all_block,
            'uid': uid,
        }

        return render(request, 'webpage/quiz.html', context)

    def post(self, request):
        if request.is_ajax():
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
            colors = Quiz.objects.get(topic=data['name_block'])
            if int(data['result_block']) > int(colors.hard):
                print(data['result_block'], colors.hard)
                color = 'hard'
            elif int(data['result_block']) > int(colors.medium):
                print(data['result_block'], colors.medium)
                color = 'medium'
            elif int(data['result_block']) > int(colors.low):
                print(data['result_block'], colors.low)
                color = 'low'
            else:
                color = 'this'
            addanswer.uid = uid
            addanswer.questions = data['name_block']
            addanswer.result = data['result_block']
            addanswer.color = color
            addanswer.save()
            result = {'Answers': 'add save'}

    return JsonResponse(result)
    

def result_quiz(request, uid):
    result_user = Result_answers.objects.filter(uid=uid)
    block = BlockQuiz.objects.all()
    

    all_result = []
    for item in result_user:
        tmp = []
        tmp.append(item.questions)
        tmp.append(item.result)
        tmp.append(item.color)
        all_result.append(tmp)

    result_all = []
    for item in block:
        tmp = []
        tmp.append(item.title)
        print(item.title)
        quiz = Quiz.objects.filter(title_block=item.id)
        for obj in quiz:
            tmp2 = []
            # print(obj.topic)
            for it in all_result:
                if it[0] == obj.topic:
                    tmp2.append(it[0])
                    tmp2.append(it[1])
                    tmp2.append(it[2])
                    print(it[0], it[1], it[2])
            if tmp2:
                tmp.append(tmp2)
        result_all.append(tmp)

    return JsonResponse({'result': result_all})
