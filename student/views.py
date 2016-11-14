from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is your NOdues form")

# Create your views here.
