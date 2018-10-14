from django.conf.urls import url
from . import views
from django.urls import path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('^$', views.index),
    path('user/login.html', views.login),
    path('user/register.html', views.register),
    path('puzzle/puzzle.html', views.puzzle),
    path('result/result.html', views.result),
    path('action', views.action),
    path('quit', views.quit),
    path('checkLogin', views.checkLogin),
    path('checkRegister', views.checkRegister),
]

# urlpatterns += staticfiles_urlpatterns()