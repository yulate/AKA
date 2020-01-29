from django.db import models

# Create your models here.
class Api_message (models.Model):
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

class Api_user(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    vip = models.BooleanField()
    score = models.IntegerField()

class UV(models.Model):
    uv = models.IntegerField()