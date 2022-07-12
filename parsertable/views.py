from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from requests import Response

from quizes.models import BlockQuiz, Quiz, Question, Answer, CauseModel

import openpyxl
import json


class ParserTable(View):
    """Парсер таблицы с вопросами"""

    def get(self, request):
        template = 'parsertable/index.html'

        book = openpyxl.open("media/WellySurvey2.xlsx", read_only=True)
        sheet = book.active

        i = 0
        # max_rows = ParserTable.get_maximum_rows(sheet_object=sheet)
        table = []
        tmp_block, tmp_question = '', ''
        for row in sheet.rows:
            if i == 0:
                i += 1
                continue
            # блоки вопросов
            if row[1].value != None:
                if tmp_block != row[1].value:
                    group = []
                    group.append(f'{row[1].value}')
                    tmp_block = row[1].value
                    table.append(group)
            # вопросы
            if row[7].value != None:
                if tmp_question != row[7].value:
                    question = []
                    question.append(f'{row[7].value}')
                    tmp_question = row[7].value
                    group.append(question)
            # ответы
            answers = []
            if row[8].value != None:
                ansvers_cause = []
                ansvers_cause.append(row[8].value)
                ansvers_cause.append('0')
                answers.append(ansvers_cause)
            if row[9].value != None:
                ansvers_cause = []
                ansvers_cause.append(row[9].value)
                ansvers_cause.append(f'{row[13].value},{row[15].value},{row[17].value},{row[19].value}')
                answers.append(ansvers_cause)
            if row[10].value != None:
                ansvers_cause = []
                ansvers_cause.append(row[10].value)
                ansvers_cause.append(f'{row[13].value},{row[15].value},{row[17].value},{row[19].value}')
                answers.append(ansvers_cause)
            if row[11].value != None:
                ansvers_cause = []
                ansvers_cause.append(row[11].value)
                ansvers_cause.append(f'{row[13].value},{row[15].value},{row[17].value},{row[19].value}')
                answers.append(ansvers_cause)
            if len(answers) > 0:
                question.append(answers)

        print(table[6])

        block = BlockQuiz()
        quiz = Quiz()
        questions = Question()
        answer = Answer()

        iter = 0
        titles = 'ALL BLOCK'
        block = BlockQuiz()
        block.title = titles
        # block.save()
        for item_block in table:
            for i in range(len(item_block)):
                if i == 0:
                    quiz = Quiz()
                    quiz.topic = item_block[i]
                    quiz.title_block = BlockQuiz.objects.get(title=titles)
                    tmp_topic = item_block[i]
                    # quiz.save()
                    # print('Quiz -', item_block[i])
                if i > 0 :
                    for j in range(len(item_block[i])):
                        if j == 0:
                            questions = Question()
                            questions.text = item_block[i][j]
                            temp_text = item_block[i][j]
                            questions.quiz = Quiz.objects.filter(topic=tmp_topic)[0]
                            # questions.save()
                            # print('##### Questions -', item_block[i][j])
                        if j > 0:
                            for d in range(len(item_block[i][j])):
                                answers = Answer()
                                answers.question = Question.objects.filter(text=temp_text)[0]
                                answers.text = item_block[i][j][d][0]
                                answers.cause = str(item_block[i][j][d][1])
                                answers.value_answer = d
                                answers.save()
                                # print('######### Answer -', item_block[i][j][d][1])



        return render(request, template, {'table': table})

    def get_maximum_rows(*, sheet_object):
        rows = 0
        for max_row, row in enumerate(sheet_object, 1):
            if not all(col.value is None for col in row):
                rows += 1
        return rows


class Problem_add(View):

    def get(self, request):
        template = 'parsertable/problem.html'
        book = openpyxl.open("media/WellySurvey2.xlsx", read_only=True)
        sheet = book.active
        
        i = 0
        table = []
        question = []
        for row in sheet.rows:
            if i == 0:
                i += 1
                continue
            # блоки вопросов
            if row[1].value != None:
                tmp = []
                question.append(row[7].value)
                question.append(row[8].value)


        context = {
            'table': question,
        }
        return render(request, template, context)

class ParserCause(View):

    def get(self, request):
        book = openpyxl.open("media/cause.xlsx", read_only=True)
        sheet = book.active

        for row in sheet.rows:
            cause = CauseModel()
            if row[1].value is None:
                break

            cause.name = row[2].value
            if row[3].value is None:
                cause.text_body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            else:
                cause.text_body = row[3].value
            if row[4].value is None:
                cause.text_cause = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            else:
                cause.text_cause = row[4].value
            cause.save()
            print(row[0].value)
        
        return JsonResponse({"work": "true"})
