from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField 
    pub_date = models.DateTimeField("date published")

