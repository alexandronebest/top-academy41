from django.contrib import admin
from .models import Movie, Hall, Session

admin.site.register(Movie)
admin.site.register(Hall)
admin.site.register(Session)