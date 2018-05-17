from django.shortcuts import render
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html', )

def languages(request):
    return render(request, 'dashboard/languages.html', )

from .forms import NameForm
from django.http import HttpResponseRedirect

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'dashboard/languages.html', {'form': form})