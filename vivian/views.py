from django.shortcuts import render
from django.http import HttpResponse
from .models import Writingprompt
from .functions import reddit


def index(request):
    v=reddit()
    latest_question_list = Writingprompt.objects.all()
    return render(request, 'vivian/index.html', {'question': latest_question_list})
