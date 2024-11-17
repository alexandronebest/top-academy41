from django.urls import path
from .views import note_list

urlpatterns = [
    path('', note_list, name='note_list'),
]