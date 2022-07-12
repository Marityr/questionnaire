# from urllib import request
from re import template
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from requests import request

from feedback.models import Feedback
from .forms import LoginForm
from django.contrib.auth.models import User

from django.views import View

from userdata.models import UserData
from .models import Quiz, BlockQuiz, Question, ResultAnswers, Result_answers, Answer, NewAnsvers, CauseModel
from userdata.forms import UserDataForm
from feedback.forms import FeedbackForm

import json
import base64


from matplotlib import colors, pyplot as plt
import numpy as np

import  subprocess
import os


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
            count = userdata.count
        except UserData.DoesNotExist:
            form = UserDataForm()
            count = 0

        try:
            userdata = UserData.objects.get(username=request.user)
        except UserData.DoesNotExist:
            userdata = 'none'

        context = {
            'form': form,
            'userdata': userdata,
            'count': count,
        }

        return render(request, template_name, context)


    def post(self, request):
        if request.method == 'POST':
            form = UserDataForm(request.POST)
            # print(request.POST)
            try:
                userdata = UserData.objects.get(username=request.user)
                userdata.age = request.POST['age']
                userdata.gender = request.POST['gender']
                userdata.massa = request.POST['massa']
                userdata.purpose = request.POST['purpose']
                userdata.decision = request.POST['decision']
                # if request.POST.get('problem'):
                #     userdata.problem = True
                # else:
                #     userdata.problem = False
                # if request.POST.get('problem_two'):
                #     userdata.problem_two = True
                # else:
                #     userdata.problem_two = False
                # if request.POST.get('problem_fre'):
                #     userdata.problem_fre = True
                # else:
                #     userdata.problem_fre = False
                # if request.POST.get('problem_foo'):
                #     userdata.problem_foo = True
                # else:
                #     userdata.problem_foo = False
                # if request.POST.get('problem_fiv'):
                #     userdata.problem_fiv = True
                # else:
                #     userdata.problem_fiv = False
                # if request.POST.get('problem_sex'):
                #     userdata.problem_sex = True
                # else:
                #     userdata.problem_sex = False
                # if request.POST.get('problem_sev'):
                #     userdata.problem_sev = True
                # else:
                #     userdata.problem_sev = False
                # if request.POST.get('problem_noi'):
                #     userdata.problem_noi = True
                # else:
                #     userdata.problem_noi = False
                # if request.POST.get('problem_ech'):
                #     userdata.problem_ech = True
                # else:
                #     userdata.problem_ech = False
                # if request.POST.get('problem_thn'):
                #     userdata.problem_thn = True
                # else:
                #     userdata.problem_thn = False
                # if request.POST.get('problem_elv'):
                #     userdata.problem_elv = True
                # else:
                #     userdata.problem_elv = False
                # if request.POST.get('problem_lav'):
                #     userdata.problem_lav = True
                # else:
                #     userdata.problem_lav = False
                # if request.POST.get('problem_ulw'):
                #     userdata.problem_ulw = True
                # else:
                #     userdata.problem_ulw = False
                # if request.POST.get('problem_flv'):
                #     userdata.problem_flv = True
                # else:
                #     userdata.problem_flv = False
                # if request.POST.get('problem_fvt'):
                #     userdata.problem_fvt = True
                # else:
                #     userdata.problem_fvt = False
                userdata.save()
            except UserData.DoesNotExist:
                userdata = UserData()
                userdata.username = request.user
                userdata.age = request.POST['age']
                userdata.gender = request.POST['gender']
                userdata.massa = request.POST['massa']
                userdata.purpose = request.POST['purpose']
                userdata.decision = request.POST['decision']
                # if request.POST.get('problem'):
                #     userdata.problem = True
                # else:
                #     userdata.problem = False
                # if request.POST.get('problem_two'):
                #     userdata.problem_two = True
                # else:
                #     userdata.problem_two = False
                # if request.POST.get('problem_fre'):
                #     userdata.problem_fre = True
                # else:
                #     userdata.problem_fre = False
                # if request.POST.get('problem_foo'):
                #     userdata.problem_foo = True
                # else:
                #     userdata.problem_foo = False
                # if request.POST.get('problem_fiv'):
                #     userdata.problem_fiv = True
                # else:
                #     userdata.problem_fiv = False
                # if request.POST.get('problem_sex'):
                #     userdata.problem_sex = True
                # else:
                #     userdata.problem_sex = False
                # if request.POST.get('problem_sev'):
                #     userdata.problem_sev = True
                # else:
                #     userdata.problem_sev = False
                # if request.POST.get('problem_noi'):
                #     userdata.problem_noi = True
                # else:
                #     userdata.problem_noi = False
                # if request.POST.get('problem_ech'):
                #     userdata.problem_ech = True
                # else:
                #     userdata.problem_ech = False
                # if request.POST.get('problem_thn'):
                #     userdata.problem_thn = True
                # else:
                #     userdata.problem_thn = False
                # if request.POST.get('problem_elv'):
                #     userdata.problem_elv = True
                # else:
                #     userdata.problem_elv = False
                # if request.POST.get('problem_lav'):
                #     userdata.problem_lav = True
                # else:
                #     userdata.problem_lav = False
                # if request.POST.get('problem_ulw'):
                #     userdata.problem_ulw = True
                # else:
                #     userdata.problem_ulw = False
                # if request.POST.get('problem_flv'):
                #     userdata.problem_flv = True
                # else:
                #     userdata.problem_flv = False
                # if request.POST.get('problem_fvt'):
                #     userdata.problem_fvt = True
                # else:
                #     userdata.problem_fvt = False
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
        userdata = UserData.objects.get(username=request.user)
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
                answers.append(q.legend)
                for a in q.get_answers():
                    tmp = []
                    tmp.append(a.value_answer)
                    tmp.append(a.cause)
                    tmp.append(a.text)
                    answers.append(tmp)
                    pass
                questions.append(answers)
            all_block.append(questions)
        
        # print(len(all_block))
        context = {
            'questions': all_block,
            'uid': uid,
            'countdata': userdata.count,
        }

        print(userdata.count)

        return render(request, 'webpage/quiz.html', context)

    def post(self, request):
        if request.is_ajax():
            pass

        return JsonResponse({'text': 'works'})


def save_quiz(request, uid):
    """Сохранение блока опроса"""

    if request.is_ajax():
        data = request.POST
        userdata = UserData.objects.get(username=request.user)
        count = userdata.count
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
                # print(data['result_block'], colors.hard)
                color = 'hard'
            elif int(data['result_block']) > int(colors.medium):
                # print(data['result_block'], colors.medium)
                color = 'medium'
            elif int(data['result_block']) > int(colors.low):
                # print(data['result_block'], colors.low)
                color = 'low'
            else:
                color = 'this'
            addanswer.uid = uid
            addanswer.questions = data['name_block']
            addanswer.color = color
            # print( data['cuase_block'])
            addanswer.result = data['result_block']
            l = data['cuase_block'].split(',')
            addanswer.causes =  data['cuase_block']

            addanswer.count = count

            addanswer.save()
            result = {'Answers': 'add save'}
        except Result_answers.DoesNotExist:
            addanswer = Result_answers()
            colors = Quiz.objects.get(topic=data['name_block'])
            if int(data['result_block']) > int(colors.hard):
                # print(data['result_block'], colors.hard)
                color = 'hard'
            elif int(data['result_block']) > int(colors.medium):
                # print(data['result_block'], colors.medium)
                color = 'medium'
            elif int(data['result_block']) > int(colors.low):
                # print(data['result_block'], colors.low)
                color = 'low'
            else:
                color = 'this'
            addanswer.uid = uid
            addanswer.questions = data['name_block']
            addanswer.color = color
            addanswer.uid = uid
            addanswer.questions = data['name_block']
            addanswer.result = data['result_block']
            l = data['cuase_block'].split(',')
            addanswer.causes = str(data['cuase_block'])

            # print(data['name_block'])

            addanswer.count = count

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

    return JsonResponse({'result_all': result_all})


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
        form = FeedbackForm()

        context = {
            'form': form,
        }

        return render(request, template, context)

    def post(self, request):
        userdata = UserData.objects.get(username=request.user)
        user_data = User.objects.get(username=request.user)

        message = f"{user_data.username}-{user_data.email}"
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')        

        if request.method == 'POST':
            data = Feedback()
            data.userID = base64_message
            data.email = user_data.email
            form = FeedbackForm(request.POST, instance=data)
            
            form.save()

            # data = Feedback()
            # form = FeedbackForm(request.POST)
            # data.userID = base64_message
            # data.email = user_data.email
            # data.rate = form['rate']
            # data.like = form['like']
            # data.dislike = form['dislike']
            # data.save()


        return redirect('quizes:resultpages', int(userdata.count) -2)


class ResulrPage(View):

    def get(self, request, count):
        template = 'nwe/result.html'
        user_data = User.objects.get(username=request.user)
        message = f"{user_data.username}-{user_data.email}"
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        result = Result_answers.objects.filter(count=count, uid=base64_message)

        result_user = Result_answers.objects.filter(count=count, uid=base64_message)
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
                        tmp2.append(it[2])
                        tmp2.append(it[0])
                        tmp2.append(it[1])
                        
                        for cause_item in it[3]:
                            tmp3 = []
                            if cause_item == 'None':
                                break
                            try:
                                cause = CauseModel.objects.get(name=str(cause_item))
                                tmp3.append(cause.name)
                                tmp3.append(cause.text_body)
                                tmp3.append(cause.name)
                                tmp3.append(cause.text_cause)
                                # print(cause.id)
                                tmp2.append(tmp3)
                            except CauseModel.DoesNotExist:
                                print('none model')
                if tmp2:
                    tmp.append(tmp2)
            result_all.append(tmp)
        graf_name = []
        for item in result_user:
            graf_name.append(item.questions)

        colors = []    
        values = []
        for item in result_user:
            if item.color == 'hard':
                colors.append('rgba(238, 38, 78, 1)')
                values.append(3)
            if item.color == 'medium':
                colors.append('rgba(252, 213, 113, 1)')
                values.append(2)
            if item.color == 'low':
                colors.append('rgba(128, 204, 40, 1)')
                values.append(1)
            if item.color == 'this':
                colors.append('rgba(247, 247, 247, 1)')
                values.append(0)
        context = {
            'resultdata': result,
            'result_all': result_all,
            'graf_name': graf_name,
            'colors': colors,
            'values': values,
        }

        return render(request, template, context)


class NewSaveAnsver(View):

    def post(self, request, uid):
        if request.is_ajax():
            data = request.POST
            userdata = UserData.objects.get(username=request.user)
            count = userdata.count
            
            answer = data['answer'].split(' # ')
            answer_data = []

            for item in answer:
                tmp = item.split(" | ")
                answer_data.append(tmp)

            # for item in answer_data:
            #     print(item[0], ' -- ', item[1])

            try:
                for item in answer_data:
                    newanswers = NewAnsvers.objects.get(count=count, userID=uid, question=item[0])
                    newanswers.userID = uid
                    newanswers.count = count
                    newanswers.quiz = data['name_block']
                    newanswers.question = item[0]
                    newanswers.ansver_values = item[1]
                    newanswers.save()
            except NewAnsvers.DoesNotExist:
                for item in answer_data:
                    newanswers = NewAnsvers()
                    newanswers.userID = uid
                    newanswers.count = count
                    newanswers.quiz = data['name_block']
                    newanswers.question = item[0]
                    newanswers.ansver_values = item[1]
                    newanswers.save()
        
        result = {'Answers': 'add save'}
        return JsonResponse(result)


class NewResult(View):

    def get(self, request, count):
        template = 'nwe/newresult.html'

        user_data = User.objects.get(username=request.user)
        message = f"{user_data.username}-{user_data.email}"
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        result = Result_answers.objects.filter(count=count, uid=base64_message)

        result_user = Result_answers.objects.filter(count=count, uid=base64_message)
        block = BlockQuiz.objects.all()
        

        all_result = []
        for item in result_user:
            tmp = []
            tmp.append(item.questions)
            tmp.append(item.result)
            tmp.append(item.color)
            tmp.append(list_cause(item.causes))
            # print(item.causes)
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
                        tmp2.append(it[2])
                        tmp2.append(it[0])
                        tmp2.append(it[1])
                        
                        for cause_item in it[3]:
                            tmp3 = []
                            if cause_item == 'None':
                                break
                            try:
                                # print(cause_item)
                                cause = CauseModel.objects.get(name=str(cause_item))
                                tmp3.append(cause.name)
                                tmp3.append(cause.text_body)
                                tmp3.append(cause.name)
                                tmp3.append(cause.text_cause)
                                # print(cause.id)
                                tmp2.append(tmp3)
                            except CauseModel.DoesNotExist:
                                print('none model')
                if tmp2:
                    tmp.append(tmp2)
            result_all.append(tmp)

        graf_name = []
        gn = 0
        for item in result_user:
            gn = gn + 1
            # graf_name.append(gn)
            graf_name.append(item.questions)

        colors = []    
        values = []
        for item in result_user:
            if item.color == 'hard':
                colors.append('rgba(238, 38, 78, 1)')
                values.append(3)
            if item.color == 'medium':
                colors.append('rgba(252, 213, 113, 1)')
                values.append(2)
            if item.color == 'low':
                colors.append('rgba(128, 204, 40, 1)')
                values.append(1)
            if item.color == 'this':
                colors.append('rgba(247, 247, 247, 1)')
                values.append(0)
        context = {
            'resultdata': result,
            'result_all': result_all,
            'graf_name': graf_name,
            'colors': colors,
            'values': values,
        }

        # print(result_all)

        return render(request, template, context)
    

class CountItr(View):
    """Увелечение количества счетчкика попыток"""

    def get(self, request):
        data = UserData.objects.get(username=request.user)
        data.count = int(data.count) + 1
        print("iter plus")
        data.save()
    
        return JsonResponse({'Count': 'true'})



class Testpage(View):

    def get(self, request, count):
        template = "testpage/newresultpage.html"

        user_data = User.objects.get(username=request.user)
        message = f"{user_data.username}-{user_data.email}"
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        result = Result_answers.objects.filter(count=count, uid=base64_message)

        result_user = Result_answers.objects.filter(count=count, uid=base64_message)

        print(result)

        block = BlockQuiz.objects.all()
        

        all_result = []
        for item in result_user:
            tmp = []
            tmp.append(item.questions)
            tmp.append(item.result)
            tmp.append(item.color)
            tmp.append(list_cause(item.causes))
            # print(item.causes)
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
                        tmp2.append(it[2])
                        tmp2.append(it[0])
                        tmp2.append(it[1])
                        
                        for cause_item in it[3]:
                            tmp3 = []
                            if cause_item == 'None':
                                break
                            try:
                                cause = CauseModel.objects.get(name=str(cause_item))
                                tmp3.append(cause.name)
                                tmp3.append(cause.text_body)
                                tmp3.append(cause.text_cause)
                                print(cause.id)
                                tmp2.append(tmp3)
                            except CauseModel.DoesNotExist:
                                print('none model')
                if tmp2:
                    tmp.append(tmp2)
            result_all.append(tmp)
        context = {
            'resultdata': result,
            'result_all': result_all,
        }

        return render(request, template, context)



class DataResult(View):

    def get(self, request, name, count):
        template = 'nwe/newresult.html'

        user_data = User.objects.get(username=name)
        message = f"{user_data.username}-{user_data.email}"
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        result = Result_answers.objects.filter(count=count, uid=base64_message)

        result_user = Result_answers.objects.filter(count=count, uid=base64_message)
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
                        tmp2.append(it[2])
                        tmp2.append(it[0])
                        tmp2.append(it[1])
                        
                        for cause_item in it[3]:
                            tmp3 = []
                            if cause_item == 'None':
                                break
                            try:
                                cause = CauseModel.objects.get(name=str(cause_item))
                                tmp3.append(cause.name)
                                tmp3.append(cause.text_body)
                                tmp3.append(cause.name)
                                tmp3.append(cause.text_cause)
                                # print(cause.id)
                                tmp2.append(tmp3)
                            except CauseModel.DoesNotExist:
                                print('none model')
                if tmp2:
                    tmp.append(tmp2)
            result_all.append(tmp)
        graf_name = []
        for item in result_user:
            graf_name.append(item.questions)

        colors = []    
        values = []
        for item in result_user:
            if item.color == 'hard':
                colors.append('rgba(238, 38, 78, 1)')
                values.append(3)
            if item.color == 'medium':
                colors.append('rgba(252, 213, 113, 1)')
                values.append(2)
            if item.color == 'low':
                colors.append('rgba(128, 204, 40, 1)')
                values.append(1)
            if item.color == 'this':
                colors.append('rgba(247, 247, 247, 1)')
                values.append(0)
        context = {
            'resultdata': result,
            'result_all': result_all,
            'graf_name': graf_name,
            'colors': colors,
            'values': values,
        }

        # print(base64_message)
        # print(count)
        # print(Result_answers.objects.filter(uid='YXJ0ZW0ta3Vob21leGFodWsuYWlAZ21haWwuY29t'))

        return render(request, template, context)