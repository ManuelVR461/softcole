from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_inscripciones(request):
    return HttpResponse("index de inscripciones ");