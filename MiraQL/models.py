from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
