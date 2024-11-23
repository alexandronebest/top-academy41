# from django.db import models
# from django.urls import path
# from . import views

# class Mysic(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     published_date = models.DateTimeField(auto_now_add=True)
# urlpatterns = [
#     path('', views.music_text, name='music_text'),
#     path('fr/', views.music_text_fr, name='music_text_fr'),
#     path('de/', views.music_text_de, name='music_text_de'),
#     path('es/', views.music_text_es, name='music_text_es'),
#     ]


from django.db import models

class Music(models.Model):
    content = models.TextField()
    
    def __str__(self):
        return self.content