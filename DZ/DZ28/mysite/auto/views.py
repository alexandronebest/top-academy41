from django.shortcuts import render
from .models import Auto

def auto_gl(request):
       autos = Auto.objects.all()
       return render(request, 'auto/auto_gl.html', {'autos': autos})

def toyota(request):
       autos = Auto.objects.all()
       return render(request, 'auto/toyota.html', {'autos': autos})

def honda(request):
       autos = Auto.objects.all()
       return render(request, 'auto/honda.html', {'autos': autos})

def renault(request):
       autos = Auto.objects.all()
       return render(request, 'auto/renault.html', {'autos': autos})