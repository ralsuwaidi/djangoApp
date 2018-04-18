from django.shortcuts import render
from django.http import HttpResponse
from .models import Writingprompt
from .functions import pop_reddit
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import markdown2


def index(request):

    pop_reddit()

    latest_question_list = Writingprompt.objects.order_by("-pub_date")
    paginator = Paginator(latest_question_list, 5)

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'vivian/index.html', {'question': contacts, })


class IndexView(generic.ListView):
    queryset = Writingprompt.objects.order_by('-pub_date')
    paginate_by = 4
    context_object_name = 'question'
    template_name = 'vivian/index.html'
