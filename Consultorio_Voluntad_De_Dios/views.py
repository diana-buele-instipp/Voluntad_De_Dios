from django.shortcuts import render
from django. http import HttpResponse
# Create your views here.
def holamundo(request):
    return HttpResponse("<h1>hola mundo, aprendiendo a programar en python</h1>")
def inicio(request):
    return render(request,'inicio.html')
def servicios(request):
    return render(request,'servicios.html')
def informacion(request):
    return render(request,'informacion.html')