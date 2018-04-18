from django.shortcuts import render
from django.http import HttpResponse
from .models import Writingprompt
<<<<<<< HEAD
from .functions import reddit, pop_reddit
from .forms import NameForm
=======
from .functions import pop_reddit
>>>>>>> 303555820719c5155f46b36ef59ee9d29ff9dc01
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import markdown2

pagn_num=3

def index(request):
<<<<<<< HEAD


# if this is a POST request we need to process the form data
    #if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        pop_reddit()

        latest_question_list = Writingprompt.objects.order_by("-pub_date")
        paginator=Paginator(latest_question_list, 5)

        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request, 'vivian/index.html', {'question': contacts,})

    #else:
        #form = NameForm()

    #latest_question_list = Writingprompt.objects.order_by("-score")[:5]
    #return render(request, 'vivian/index.html', {'question': latest_question_list, 'raw_comment': v})
=======

    pop_reddit()

    latest_question_list = Writingprompt.objects.order_by("-pub_date")
    paginator = Paginator(latest_question_list, pagn_num)

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'vivian/index.html', {'question': contacts, })

>>>>>>> 303555820719c5155f46b36ef59ee9d29ff9dc01

class IndexView(generic.ListView):
    queryset = Writingprompt.objects.order_by('-pub_date')
    paginate_by = 4
    context_object_name = 'question'
    template_name = 'vivian/index.html'

def hot(request):

    latest_question_list = Writingprompt.objects.order_by("-score")
    paginator = Paginator(latest_question_list, pagn_num)

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'vivian/index.html', {'question': contacts, })

def date(request):

    latest_question_list = Writingprompt.objects.order_by("-pub_date")
    paginator = Paginator(latest_question_list, pagn_num)

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'vivian/index.html', {'question': contacts, })
