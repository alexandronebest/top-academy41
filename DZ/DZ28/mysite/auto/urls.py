from django.urls import path
from . import views

urlpatterns = [
    path('', views.auto_gl, name='auto_gl'), 
]