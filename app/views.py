from django.shortcuts import render
from .email import sendEmail
from .models import *
import uuid
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')

def puzzle(request):
    num = [0] * 20
    for i in range(0, 20):
        num[i] = random.randint(1, PuzzleInfo.objects.filter().count())
    store = []
    o = 1
    for i in num:
        puz = PuzzleInfo.objects.get(pk=i)
        store.append({'num':o ,'ptype':puz.ptype, 'ptitle':puz.ptitle, 'pa':puz.pa, 'pb':puz.pb, 'pc':puz.pc, 'pd':puz.pd, 'pkey': puz.pkey, 'pdiff':puz.pdiff})
        o += 1
    request.session['puzzle'] = store
    puzz = {'puzz': store}
    print(store)
    return render(request, 'puzzle/puzzle.html', puzz)

def result(request):
    return render(request, 'result/request')




def action(request):
    email = request.GET['email']
    vcode = request.GET['vcode']
    user = UserInfo.User.findByEmail(email)
    if user == None:
        msg = {'msg' : '账户不存在'}
        return render(request, 'index.html', msg)
    if vcode == user.uaccode:
        user.isAction = True
        user.save()
        msg = {'msg' : '账户已激活'}
    return render(request, 'index.html', msg)

def quit(request):
    del request.session['user']
    return render(request, 'index.html')

def checkLogin(request):
    email = request.POST['email']
    passwd = request.POST['password']
    user = UserInfo.User.findByEmail(email)
    if user == None:
        msg = {'msg' : '账户不存在'}
        return render(request, 'user/login.html', msg)
    if user.isAction == False:
        msg = {'msg' : '账户未激活'}
        return render(request, 'user/login.html', msg)
    if user.upass == False:
        msg = {'msg' : '密码不正确'}
        return render(request, 'user/login.html', msg)
    request.session['user'] = user.pk
    # print(request.session['user'])
    return render(request, 'index.html')
    

def checkRegister(request):
    email = request.POST['email']
    passwd = request.POST['password']
    repasswd = request.POST['repassword']
    if len(passwd) < 8 or passwd != repasswd:
        msg = {'msg' : '填写信息有误（密码需要大于7位等）'}
        return render(request, 'user/register.html', msg)
    # print(UserInfo.User.emailExists(email))
    if UserInfo.User.emailExists(email):
        msg = {'msg' : '该邮箱已被注册'}
        return render(request, 'user/register.html', msg)
    vcode = uuid.uuid4()
    UserInfo.User.create(email, passwd, str(vcode))
    sendEmail(email, email, str(vcode))
    return render(request, 'index.html')

def checkPuzzle(request):
    n = 100 / 20
    grade = 0
    date = ''
    for i in range(1, 21):
        if request.GET[str(i)] == request.GET[str(i) + "key"]:
            grade += n
            date += request.GET[str(i) + "id"] + ":" + request.GET[str(i) + "key"] + ";"
    content = {'grade': grade}
    mark = MarkRecodeInfo()
    mark.mscore = grade
    mark.mdate = date
    mark.uid = UserInfo.UserBase.get(pk=request.session['user'])
    mark.save()
    return render(request, 'result/result.html', content)
