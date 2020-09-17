from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def learn(request):
    return render(request, 'learn.html')

def teach(request):
    return render(request, 'teach.html')

def projects(request):
    return render(request, 'projects.html')

def about(request):
    return render(request, 'about.html')
