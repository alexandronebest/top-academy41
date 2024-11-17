from django.urls import path
from .views import blog

urlpatterns = [
    path('blog/', blog, name='post_list'),
]