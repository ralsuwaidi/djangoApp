from django.shortcuts import render
from django.http import HttpResponse
from .models import Writingprompt
from .functions import reddit

<<<<<<< HEAD

def index(request):
    v=reddit()
=======
def index(request):
>>>>>>> b6a1f70d0fb60e7eeee3ed739e3ac89a12228be2
    latest_question_list = Writingprompt.objects.all()
    return render(request, 'vivian/index.html', {'question': latest_question_list})
