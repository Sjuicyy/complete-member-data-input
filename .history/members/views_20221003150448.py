from django.shortcuts import render
from django.http import HttpResponse
from django

def index(request):
    return HttpResponse("Hello world!")