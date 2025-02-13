from django.shortcuts import render

def index(request):
    return render(request, 'store/index.html')  # Возвращаем шаблон index.html

def profile(request):
    return render(request, 'store/profile.html')