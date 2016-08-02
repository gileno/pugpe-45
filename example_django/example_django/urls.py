from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello World')

urlpatterns = [
    url(r'^$', hello)
]
