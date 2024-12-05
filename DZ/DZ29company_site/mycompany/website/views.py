from django.shortcuts import render
from .models import Service
from .forms import ContactForm

def home(request):
    services = Service.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка формы (например, отправка по электронной почте)
            # Далее вы можете обработать данные из формы
            pass

    return render(request, 'website/home.html', {'services': services, 'form': form})