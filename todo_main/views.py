from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    
    # return HttpResponse('<h1>This is my home page </h1>')
    return render(request,'home.html')