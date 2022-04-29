# from urllib import request
from re import template
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from requests import request
from .forms import LoginForm
from django.contrib.auth.models import User

from django.views import View

from userdata.models import UserData
from .models import Quiz, BlockQuiz, Question, ResultAnswers, Result_answers, Answer
from userdata.forms import UserDataForm

import json
import base64


class HomePage(View):

    def get(self, request):
        template_name = 'nwe/index.html'

        form = LoginForm()

        context = {
            'form': form,
        }
        return render(request, template_name, context)


    def post(self, request) -> JsonResponse:
        if request.is_ajax():
            newuser = ResultAnswers()
            data = request.POST
            newuser.name = data['name']
            newuser.email = data['email']
            newuser.male = data['male']
            newuser.save()
        return JsonResponse({'uid': str(newuser)})


class Dashboard(View):
    def get(self, request):
        template_name='dashboard/home.html'

        try:
            userdata = UserData.objects.get(username=request.user)
            data = {
                'age': userdata.age,
            }
            form = UserDataForm(instance=userdata)
        except UserData.DoesNotExist:
            form = UserDataForm()

        try:
            userdata = UserData.objects.get(username=request.user)
        except UserData.DoesNotExist:
            userdata = 'none'

        context = {
            'form': form,
            'userdata': userdata
        }

        return render(request, template_name, context)


    def post(self, request):
        if request.method == 'POST':
            form = UserDataForm(request.POST)
            # print(request.POST)
            print()
            try:
                userdata = UserData.objects.get(username=request.user)
                userdata.age = request.POST['age']
                userdata.gender = request.POST['gender']
                userdata.massa = request.POST['massa']
                userdata.purpose = request.POST['purpose']
                userdata.decision = request.POST['decision']
                if request.POST.get('problem'):
                    userdata.problem = True
                if request.POST.get('problem_two'):
                    userdata.problem_two = True
                if request.POST.get('problem_fre'):
                    userdata.problem_fre = True
                userdata.save()
            except UserData.DoesNotExist:
                userdata = UserData()
                userdata.username = request.user
                userdata.age = request.POST['age']
                userdata.gender = request.POST['gender']
                userdata.massa = request.POST['massa']
                userdata.purpose = request.POST['purpose']
                userdata.decision = request.POST['decision']
                if request.POST.get('problem'):
                    userdata.problem = True
                if request.POST.get('problem_two'):
                    userdata.problem_two = True
                if request.POST.get('problem_fre'):
                    userdata.problem_fre = True
                userdata.save()

        user_data = User.objects.get(username=request.user)
        message = f"{user_data.username}-{user_data.email}"
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        return redirect('quizes:quiz-view', f'{base64_message}')


class QuizView(View):
    """Опросник"""
    
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
                    tmp.append(a.cause)
                    tmp.append(a.text)
                    answers.append(tmp)
                    pass
                questions.append(answers)
            all_block.append(questions)
        
        print(len(all_block))
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
    """Сохранение блока опроса"""

    if request.is_ajax():
        data = request.POST
        
        try:
            Result_answers.objects.get(
                uid=uid,
                questions=data['name_block']
            )
            addanswer = Result_answers.objects.get(
                uid=uid,
                questions=data['name_block']
            )
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
            addanswer.color = color
            print( data['cuase_block'])
            addanswer.result = data['result_block']
            addanswer.causes = data['cuase_block']

            addanswer.save()
            result = {'Answers': 'add save'}
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
            addanswer.color = color
            addanswer.uid = uid
            addanswer.questions = data['name_block']
            addanswer.result = data['result_block']
            addanswer.causes = str(data['cuase_block'])

            print(data['name_block'])
            addanswer.save()
            result = {'Answers': 'add save'}

    return JsonResponse(result)

def list_cause(string):

    cause = string.split(',')
    data_cause = []
    for i in range(len(cause)):
        if cause[i] != '0':
            data_cause.append(cause[i])
    
    new_list = []
    for item in data_cause:
        if data_cause.count(item) >= 2:
            new_list.append(item)

    list2 = [] 
    for item in new_list: 
        if item not in list2: 
            list2.append(item) 

    if len(list2) == 0:
        return [''] 

    return list2  
    

def result_quiz(request, uid):
    """Результат опроса"""

    result_user = Result_answers.objects.filter(uid=uid)
    block = BlockQuiz.objects.all()
    

    all_result = []
    for item in result_user:
        tmp = []
        tmp.append(item.questions)
        tmp.append(item.result)
        tmp.append(item.color)
        tmp.append(list_cause(item.causes))
        all_result.append(tmp)

    result_all = []
    for item in block:
        tmp = []
        tmp.append(item.title)
        # print(item.title)
        quiz = Quiz.objects.filter(title_block=item.id)
        for obj in quiz:
            tmp2 = []
            # print(obj.topic)
            for it in all_result:
                if it[0] == obj.topic:
                    tmp2.append(it[0])
                    tmp2.append(it[1])
                    tmp2.append(it[2])
                    tmp2.append(it[3])
                    # print(it[0], it[1], it[2])
            if tmp2:
                tmp.append(tmp2)
        result_all.append(tmp)

    return JsonResponse({'result': result_all})


class UserUid(View):
    """UID по никнейму и почте"""

    def get(self, request, usermane):
        user_data = User.objects.get(username=usermane)

        message = f"{user_data.username}-{user_data.email}"
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        return JsonResponse({'user_data': base64_message})


class LastPage(View):

    def get(self, request):
        template = 'nwe/lastpage.html'

        return render(request, template)

    def post(self, request):
        return redirect('quizes:resultpage')


class ResulrPage(View):

    def get(self, request):
        template = 'nwe/result.html'
        user_data = User.objects.get(username=request.user)

        message = f"{user_data.username}-{user_data.email}"
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        context = {
            'uid': base64_message,
        }
        return render(request, template, context)
