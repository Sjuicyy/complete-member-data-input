from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

def index(request):
    mymembers=Members.objects.all().views
    output=''
    for x in mymembers:
        output+=x