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
            # data_.pop('csrfmiddlewaretoken')
            # data_.pop('button')
            print(data['name'])

        return redirect('quiz-view', '121341324')


class QuizView(View):

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

        context = {
            'obj': quiz,
            'quizes': quizes,
            'data': questions,
        }
        return render(request, 'webpage/quiz.html', context)

    def post(self, request, pk):
        if request.is_ajax():
            data_ = request.POST
            data_.pop('csrfmiddlewaretoken')
            data_.pop('button')
            print(request.POST)

        return JsonResponse({'text': 'works'})

    def userdata() -> dict():

        context = {}
        return context


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
