from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

def index(request):
    mymembers=Members.objects.all().values()
    template=loader.get_template('index.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))


def add(request):
    template=loader.get_template('add.h')