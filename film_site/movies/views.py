from django.shortcuts import render

def home(request):
    return render(request, 'movies/home.html')

def about(request):
    return render(request, 'movies/about.html')

def films(request):
    return render(request, 'movies/films.html')

def contacts(request):
    return render(request, 'movies/contacts.html')