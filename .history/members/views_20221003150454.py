from django.shortcuts import render
from django.http import HttpResponse
from django.template imp

def index(request):
    return HttpResponse("Hello world!")