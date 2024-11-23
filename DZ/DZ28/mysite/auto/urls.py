from django.urls import path
from . import views

urlpatterns = [
    path('auto/', views.auto_gl, name='auto_gl'),
    path('toyota/', views.toyota, name='toyota'),
    path('honda/', views.honda, name='honda'),
    path('renault/', views.renault, name='renault'),
    ]
         
