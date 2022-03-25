from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.views import View
from questions.models import Question, Answer


class QuizListView(ListView):
    
    model = Quiz
    template_name = 'webpage/index.html'


class QuizView(View):

    def get(self, request, pk):
        quiz = Quiz.objects.get(pk=pk)
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
        print(questions)
        context = {
            'obj': quiz,
            'quizes': quizes,
            'data': questions,
        }
        return render(request, 'webpage/quiz.html', context)

    def post(self, request, pk):

        return JsonResponse({'text': 'works'})

    
# def quiz_view(request, pk):
#     quiz = Quiz.objects.get(pk=pk)
#     return render(request, 'webpage/quiz.html', {'obj': quiz})


# def quiz_data_view(request, pk):
#     quiz = Quiz.objects.get(pk=1)
#     questions = []
#     for q in quiz.get_questions():
#         answers = []
#         for a in q.get_answers():
#             tmp = []
#             tmp.append(a.pk)
#             tmp.append(a.text)
#             answers.append(tmp)
#         questions.append({str(q): answers})

#     return JsonResponse({
#         'data': questions,
#         'time': quiz.time,
#     })

# def save_quiz_view(request, pk):

#     if request.is_ajax():
#         answers_id = []
#         answers_val = []
#         data = request.POST
#         data_ = dict(data.lists())

#         data_.pop('csrfmiddlewaretoken')
#         data_.pop('IDuser')

#         for k in data_.keys():
#             print('key: ', k)            
#             answers_id.append(k)

#         summ = 0
#         for v in data_.values():
#             summ = summ + int(v[0])
#             answers_val.append(v[0])

#         dictionary = dict(zip(answers_id, answers_val))

#         print(dictionary)
#         print(summ)
#     return JsonResponse({'text': 'works'})