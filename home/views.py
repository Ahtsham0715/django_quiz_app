from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import random
# Create your views here.


def home(request):
    return HttpResponse('Hello this is a quiz app home page')

def get_quiz(request):
    question_objs = list(Question.objects.all())
    random.shuffle(question_objs)
    data = [
        {
            'category': question.category.category_name,
            'question': question.question,
            'marks': question.marks,
            'answer': question.get_answers(),
        }
        for question in question_objs
    ]
    payload = {'status': 200, 'data': data}
    return JsonResponse(payload)