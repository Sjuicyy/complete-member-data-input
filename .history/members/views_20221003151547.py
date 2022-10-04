from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .mem

def index(request):
    mymembers=Members.objects.all().views