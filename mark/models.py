from django.db import models
from user.models import UserInfo

# Create your models here.
class MarkRecodeInfo(models.Model):
    uid = models.ForeignKey(UserInfo)
    mscore = models.IntegerField()
    mdate = models.DateTimeField(auto_now_add=True)