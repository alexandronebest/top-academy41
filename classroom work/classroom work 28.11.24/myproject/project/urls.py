from django.urls import path
from project import views

urlpatterns = [
    path('', views.home, name='home'),  # изменение на 'home'
]