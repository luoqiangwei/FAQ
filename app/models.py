from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uuser = models.CharField(max_length=100)
    upass = models.CharField(max_length=100)
    uaccode = models.CharField(max_length=4)
    uaccodedate = models.DateTimeField(auto_now=True)

class PuzzleInfo(models.Model):
    ptype = models.CharField(max_length=1)
    ptitle = models.CharField(max_length=500)
    pa = models.CharField(max_length=200)
    pb = models.CharField(max_length=200)
    pc = models.CharField(max_length=200)
    pd = models.CharField(max_length=200)
    pkey = models.CharField(max_length=200)
    pdiff = models.CharField(max_length=200)

class MarkRecodeInfo(models.Model):
    uid = models.ForeignKey(UserInfo)
    mscore = models.IntegerField()
    mdate = models.DateTimeField(auto_now_add=True)