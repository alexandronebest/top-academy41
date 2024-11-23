import datetime
from django.shortcuts import render

def current_day(request):
    # Получение текущего дня недели
    today = datetime.datetime.now()
    day_name = today.strftime("%A")  # Полное название дня

    # Словарь с соответствующими переведенными названиями дней
    day_dict = {
        "Monday": "Понедельник",
        "Tuesday": "Вторник",
        "Wednesday": "Среда",
        "Thursday": "Четверг",
        "Friday": "Пятница",
        "Saturday": "Суббота",
        "Sunday": "Воскресенье",
    }

    # Словарь с цветами для каждого дня недели
    color_dict = {
        "Monday": "red",
        "Tuesday": "blue",
        "Wednesday": "green",
        "Thursday": "orange",
        "Friday": "purple",
        "Saturday": "yellow",
        "Sunday": "pink",
    }

    # Получаем соответствующую надпись и цвет для текущего дня
    message = day_dict.get(day_name, "Неизвестный день")
    color = color_dict.get(day_name, "black")  # Цвет по умолчанию - черный

    return render(request, 'day/current_day.html', {'message': message, 'color': color})