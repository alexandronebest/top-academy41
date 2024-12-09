from django.db import models


class Project(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
      return self.name


class User(models.Model):
  username = models.CharField(max_length=100)
  email = models.EmailField()
  
  def __str__(self):
      return self.username


class Task(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  status = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  due_date = models.DateField()
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  performers = models.ManyToManyField(User)
  
  def __str__(self):
      return f'{self.title} ({self.status})'