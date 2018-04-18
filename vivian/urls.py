from django.urls import path
from .functions import reddit, pop_reddit

from . import views
pop_reddit()
urlpatterns = [
    path('', views.index,  name='index'),
    path('hot/', views.index,  name='index'),
]
