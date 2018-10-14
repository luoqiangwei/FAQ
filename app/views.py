from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')

def puzzle(request):
    return render(request, 'puzzle/puzzle.html')

def result(request):
    return render(request, 'result/request')




def action(request):
    pass

def quit(request):
    pass

def checkLogin(request):
    pass

def checkRegister(request):
    pass