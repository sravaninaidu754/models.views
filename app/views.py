from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_TOpic(request):
    TN=input('Enter your Topicname : ')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()

def insert_Webpage(request):
    TN=input('Enter your Topicname : ')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    # return HttpResponse("Topic data inserted successfully")
    n=input('Enter your name : ')
    u=input('enter your url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,n=name,url=u)[0]
    WO.save()
    return HttpResponse("Webpage data inserted successfully")

def insert_Accessrecords(request):
    TN=input('Enter your topic name : ')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    n=input('enter your name : ')
    u=input('enter your url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d=input('Enter date : ')
    A=input('enter author name : ')
    AR=Accessrecords.objects.get_or_create(name=WO,date=d,Authour=A)[0]
    AR.save()
    return HttpResponse("Aceessrecords data inserted successfully")




