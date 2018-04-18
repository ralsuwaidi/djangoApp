from django.shortcuts import render
from django.http import HttpResponse
from .models import Writingprompt
from .functions import reddit, pop_reddit
from .forms import NameForm
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import markdown2


def index(request):


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

class IndexView(generic.ListView):
    queryset = Writingprompt.objects.order_by('-pub_date')
    paginate_by = 4
    context_object_name = 'question'
    template_name = 'vivian/index.html'
