from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(self):
    hey = "a"
    return HttpResponse(hey)
