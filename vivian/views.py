from django.shortcuts import render
from django.http import HttpResponse
from .models import Writingprompt
from .functions import reddit
import markdown2


def index(request):
    v=reddit()
    latest_question_list = Writingprompt.objects.order_by("-score")
    return render(request, 'vivian/index.html', {'question': latest_question_list, 'raw_comment':v})
