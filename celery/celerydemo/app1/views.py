from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add


def index1(request):
    add.delay(60)
    return HttpResponse("<h1>test1</h1>")
