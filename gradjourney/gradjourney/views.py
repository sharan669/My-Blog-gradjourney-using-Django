from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'homepage.html');
    #return HttpResponse('homepage')

def about(request):
    return render(request,'about.html');
    #return Http Response('about') #sending in a respnose with a string about
