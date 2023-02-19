from django.shortcuts import render, redirect
from django.http import HttpResponse


def myView(request):
    return render(request, 'hello.html')

def anotherHello(request):
    return HttpResponse("<h1> This is another app </h1>")

