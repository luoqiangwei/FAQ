from django.conf.urls import url
from . import views
from django.urls import path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('^$', views.index),
]

# urlpatterns += staticfiles_urlpatterns()