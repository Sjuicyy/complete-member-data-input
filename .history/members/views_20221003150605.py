from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from 

def index(request):
    template=loader.get_template('myfirst.html')
    return HttpResponse