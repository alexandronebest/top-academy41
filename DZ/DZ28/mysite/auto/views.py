from django.shortcuts import render
from .models import Auto

def auto_gl(request):
       autos = Auto.objects.all()
       return render(request, 'auto/auto_gl.html', {'autos': autos})