from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    Tn=input('enter a topic name')
    TO=Top.objects.get_or_create(topic_name=Tn)[0]
    TO.save()
    return HttpResponse('Topic data is inserted')



def insert_webpage(request):
    Tn=input('enter a topic')
    TO=Top.objects.get_or_create(topic_name=Tn)[0]
    TO.save()
    n=input('enter a name')
    u=input('enter a url')
    WO=Webpages.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('webpage is created')



def insert_acessrecord(request):
    Tn=input('enter a topic')
    TO=Top.objects.get_or_create(topic_name=Tn)[0]
    TO.save()
    n=input('enter a name')
    WO=Webpages.objects.get_or_create(topic_name=TO,name=n)[0]
    WO.save()
    d=input('enter a date')
    a=input('enter a name')
    ACO=AcessRecords.objects.get_or_create(name=WO,date=d,authors=a)[0]
    ACO.save()
    return HttpResponse('access records are created')