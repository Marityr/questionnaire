from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from quizes.models import BlockQuiz, Quiz, Question, Answer

import openpyxl
import json


class ParserTable(View):
    """Парсер таблицы с вопросами"""

    def get(self, request):
        template = 'parsertable/index.html'

        book = openpyxl.open("media/WellySurvey.xlsx", read_only=True)
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
                ansvers_cause.append(row[13].value)
                answers.append(ansvers_cause)
            if row[9].value != None:
                ansvers_cause = []
                ansvers_cause.append(row[9].value)
                ansvers_cause.append(row[15].value)
                answers.append(ansvers_cause)
            if row[10].value != None:
                ansvers_cause = []
                ansvers_cause.append(row[10].value)
                ansvers_cause.append(row[17].value)
                answers.append(ansvers_cause)
            if row[11].value != None:
                ansvers_cause = []
                ansvers_cause.append(row[11].value)
                ansvers_cause.append(row[19].value)
                answers.append(ansvers_cause)
            if len(answers) > 0:
                question.append(answers)

        print(table[6])

        # block = BlockQuiz()
        # quiz = Quiz()
        # questions = Question()
        # answer = Answer()

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
                    print('Quiz -', item_block[i])
                if i > 0 :
                    for j in range(len(item_block[i])):
                        if j == 0:
                            questions = Question()
                            questions.text = item_block[i][j]
                            temp_text = item_block[i][j]
                            questions.quiz = Quiz.objects.filter(topic=tmp_topic)[0]
                            # questions.save()
                            print('##### Questions -', item_block[i][j])
                        if j > 0:
                            for d in range(len(item_block[i][j])):
                                answers = Answer()
                                answers.question = Question.objects.filter(text=temp_text)[0]
                                answers.text = item_block[i][j][d][0]
                                answers.cause = str(item_block[i][j][d][1])
                                answers.value_answer = d
                                # answers.save()
                                print('######### Answer -', item_block[i][j][d][1])



        return render(request, template, {'table': table})

    def get_maximum_rows(*, sheet_object):
        rows = 0
        for max_row, row in enumerate(sheet_object, 1):
            if not all(col.value is None for col in row):
                rows += 1
        return rows
