from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Quiz
from django.views.generic import ListView
from django.views import View
from questions.models import ResultAnswers, Result_answers
import json


class QuizListView(View):

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
        quiz = Quiz.objects.get(pk=1)
        quizes = []
        questions = []
        for q in quiz.get_questions():
            answers = []
            answers.append(str(q))
            answers.append(q.legend)
            for a in q.get_answers():
                tmp = []
                tmp.append(a.text)
                tmp.append(a.tultype)
                tmp.append(a.id)
                tmp.append(a.min_bal)
                tmp.append(a.max_bal)
                answers.append(tmp)
            questions.append(answers)

        context = {
            'obj': quiz,
            'quizes': quizes,
            'data': questions,
        }
        return render(request, 'webpage/quiz.html', context)

    def post(self, request, uid):
        if request.is_ajax():
            data_ = request.POST
            data_.pop('csrfmiddlewaretoken')
            data_.pop('button')
            print(request.POST)

        return JsonResponse({'text': 'works'})


def save_quiz_view(request, uid):
    if request.is_ajax():
        answers_id = []
        answers_val = []
        
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')
        data_.pop('button')
        questions_name = data_['questions']
        print(questions_name)
        data_.pop('questions')

        for k in data_.keys():
            answers_id.append(k)

        summ = 0
        tmp_result = 0
        for v in data_.values():
            summ = summ + int(v[0])
            answers_val.append(v[0])
            tmp_result = tmp_result + int(v[0])

        dictionary = dict(zip(answers_id, answers_val))

        result_ansvers = Result_answers()
        result_ansvers.uid = uid
        result_ansvers.questions = questions_name
        result_ansvers.result = tmp_result
        result_ansvers.save()

        addanswer = ResultAnswers.objects.get(userID=uid)
        addanswer.result_bal = int(addanswer.result_bal) + summ
        addanswer.questuins = int(addanswer.questuins) + int(len(dictionary)) 
        old_answers = addanswer.answers

        if len(old_answers) == 0:
            old_answers = dict()
            addanswer.answers = dictionary
        else:
            a = json.loads(old_answers.replace("'",'"'))
            tmp = a.copy()
            tmp.update(dictionary)
            addanswer.answers = tmp
        addanswer.save()
    return JsonResponse({'text': 'works'})


def result_answers(request, uid):
    result_user = Result_answers.objects.filter(uid=uid)

    all_result = []
    for item in result_user:
        tmp = []
        tmp.append(item.questions)
        tmp.append(item.result)
        all_result.append(tmp)
    
    dictory = dict()
    # for item in result_user:
    #     print(item)

    return JsonResponse({'result': all_result})
