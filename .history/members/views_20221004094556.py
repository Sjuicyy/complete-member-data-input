from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse


def index(request):
    mymembers=Members.objects.all().values()
    template=loader.get_template('index.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))


def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({},request))


def addrecord(request):
    x=request.POST['first']
    y=request.POST['last']
    member=Members(firstname=x,lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request,id):
    member=Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request,id):
    mymembers=Members.objects.get(id=id)
    template=loader.get_template