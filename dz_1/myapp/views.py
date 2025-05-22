from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Это главная страница.</h1>")

def test_view(request):
    return HttpResponse("<h1>Это страница TEST</h1><p>Это страница test.</p>")

def data_view(request):
    return HttpResponse("<h1>Это страница DATA</h1><p>Это страница data.</p>")
