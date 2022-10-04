from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import 

def index(request):
    mymembers=Members.objects.all().views