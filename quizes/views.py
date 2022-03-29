from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Quiz
from django.views.generic import ListView
from django.views import View
from questions.models import Question, Answer


class QuizListView(View):

    def get(self, request) -> render:
        template_name = 'webpage/index.html'

        return render(request, template_name)

    def post(self, request) -> JsonResponse:
        if request.is_ajax():
            data = request.POST
<<<<<<< Updated upstream
            # data_.pop('csrfmiddlewaretoken')
            # data_.pop('button')
            print(data['name'])

        return redirect('quiz-view', '121341324')
=======
            newuser.name = data['name']
            newuser.email = data['email']
            newuser.male = data['male']
            newuser.save()
        return JsonResponse({'uid': str(newuser)})
>>>>>>> Stashed changes


class QuizView(View):

<<<<<<< Updated upstream
    def get(self, request):
        quiz = Quiz.objects.get(pk=1)
        quizes = []
        questions = []
        for q in quiz.get_questions():
            answers = []
            answers.append(str(q))
            for a in q.get_answers():
                tmp = []
                tmp.append(a.text)
                tmp.append(a.id)
                answers.append(tmp)
            questions.append(answers)

=======
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
>>>>>>> Stashed changes
        context = {
            'obj': quiz,
            'quizes': quizes,
            'data': questions,
        }
        return render(request, 'webpage/quiz.html', context)

    def post(self, request, pk):
        if request.is_ajax():
<<<<<<< Updated upstream
            data_ = request.POST
            data_.pop('csrfmiddlewaretoken')
            data_.pop('button')
            print(request.POST)
=======
            # data_ = request.POST
            # data_.pop('csrfmiddlewaretoken')
            # data_.pop('button')
            # print(request.POST)
            # print(data_)
            pass
>>>>>>> Stashed changes

        return JsonResponse({'text': 'works'})

    def userdata() -> dict():

        context = {}
        return context

<<<<<<< Updated upstream

def save_quiz_view(request, pk):
    print('test')
    if request.is_ajax():
        answers_id = []
        answers_val = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')
        data_.pop('button')
        # data_.pop('IDuser')

        for k in data_.keys():
            print('key: ', k)
            answers_id.append(k)

        summ = 0
        for v in data_.values():
            summ = summ + int(v[0])
            answers_val.append(v[0])

        dictionary = dict(zip(answers_id, answers_val))

        # print(dictionary)
        dtr = dictionary.copy()
        dtr.update(dictionary)
        print(dtr)
    return JsonResponse({'text': 'works'})
=======
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
>>>>>>> Stashed changes
