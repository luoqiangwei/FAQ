from django.db import models

# Create your models here.
class UserInfoManager(models.Manager):
    def emailExists(self, email):
        try:
            UserInfo.UserBase.get(uuser=email)
            return True
        except:
            return False
        # if models.Manager().get(uuser=email) != None:
        #     return True
        # else:
        #     return False
    def findByEmail(self, email):
        try:
            return UserInfo.UserBase.get(uuser=email)
        except:
            return None
        # return models.Manager().get(uuser=email)
    def create(self, email, passwd, uaccode):
        u = UserInfo()
        u.uuser = email
        u.upass = passwd
        u.uaccode = uaccode
        u.isAction = False
        u.save()
        return u

class UserInfo(models.Model):
    uuser = models.CharField(max_length=100)
    upass = models.CharField(max_length=100)
    uaccode = models.CharField(max_length=100)
    uaccodedate = models.DateTimeField(auto_now=True)
    isAction = models.BooleanField(default=False)

    UserBase = models.Manager()
    User = UserInfoManager()

class PuzzleInfo(models.Model):
    ptype = models.CharField(max_length=3)
    ptitle = models.CharField(max_length=1000)
    pa = models.CharField(max_length=200)
    pb = models.CharField(max_length=200)
    pc = models.CharField(max_length=200)
    pd = models.CharField(max_length=200)
    pkey = models.CharField(max_length=200)
    pdiff = models.CharField(max_length=200)

class MarkRecodeInfo(models.Model):
    mscore = models.IntegerField()
    mdate = models.DateTimeField(auto_now_add=True)
    uid = models.ForeignKey('UserInfo', on_delete=models.CASCADE,)