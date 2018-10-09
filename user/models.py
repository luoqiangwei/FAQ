from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uuser = models.CharField(max_length=100)
    upass = models.CharField(max_length=100)
    uaccode = models.CharField(max_length=4)
    uaccodedate = models.DateTimeField(auto_now=True)