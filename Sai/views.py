from django.shortcuts import render


# Create your views here.

def Sai(request):
    return render(request,'display1.html')

def Ironman(request):
    return render(request,'display2.html')
