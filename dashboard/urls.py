from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('languages/', views.languages,  name='languages'),
     path('languages/your-name/', views.get_name,  name='name'),
]
