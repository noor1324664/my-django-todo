from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    is_done = models.BooleanField(default = False)
    user_id = models.IntegerField(default = -1)
    list_id = models.IntegerField(default = -1)

class List(models.Model):
    name = models.CharField(max_length = 200)
    user_id = models.IntegerField(default = -1)