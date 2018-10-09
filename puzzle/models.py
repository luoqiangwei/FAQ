from django.db import models

# Create your models here.
class PuzzleInfo(models.Model):
    ptype = models.CharField(max_length=1)
    ptitle = models.CharField(max_length=500)
    pa = models.CharField(max_length=200)
    pb = models.CharField(max_length=200)
    pc = models.CharField(max_length=200)
    pd = models.CharField(max_length=200)
    pkey = models.CharField(max_length=200)
    pdiff = models.CharField(max_length=200)