from django.shortcuts import render
from django.http import HttpResponse
from .models import Writingprompt
from .functions import reddit
from .forms import NameForm

import markdown2


def index(request):
    v = reddit()
    
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:

        latest_question_list = Writingprompt.objects.order_by("-score")[:5]
        return render(request, 'vivian/index.html', {'question': latest_question_list, 'raw_comment': v})

    else:
        form = NameForm()

    latest_question_list = Writingprompt.objects.order_by("-pub_date")[:5]
    return render(request, 'vivian/index.html', {'question': latest_question_list, 'raw_comment': v})
