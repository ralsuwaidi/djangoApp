from django.shortcuts import render
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html', )

def languages(request):
    return render(request, 'dashboard/languages.html', )