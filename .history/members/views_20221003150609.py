from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from 

def index(request):
    template=loader.get(_template('myfirst.html')
    return HttpResponse