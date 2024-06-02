from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')


def all(request):
    
    return render(request,'all.html')

