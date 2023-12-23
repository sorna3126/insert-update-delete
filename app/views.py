from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def display_topic(request):

    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')


    
    d={'topics':QLTO}
    return render(request,'display_topic.html',d)


def display_webpage(request):

    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    QLWO=Webpage.objects.filter(topic_name='Cricket')
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by('name')
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by('-name')
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by(Length('name'))
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by(Length('name').desc())
    QLWO=Webpage.objects.exclude(topic_name='Cricket').order_by('name')

    QLWO=Webpage.objects.filter(name__startswith='S')
    QLWO=Webpage.objects.filter(name__endswith='i')
    QLWO=Webpage.objects.filter(url__endswith='com')
    QLWO=Webpage.objects.filter(url__endswith='in')
    QLWO=Webpage.objects.filter(email__startswith='india')
    QLWO=Webpage.objects.filter(name__contains='a')
    QLWO=Webpage.objects.filter(url__contains='in')
    QLWO=Webpage.objects.filter(name__regex='\w+t$')

    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name__startswith='V'))
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name__startswith='S'))
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(email__startswith='msd'))


    d={'webpages':QLWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QLAO=AccessRecords.objects.all()
    QLAO=AccessRecords.objects.filter(id__lte=3)
    QLAO=AccessRecords.objects.filter(id__gt=3)
    QLAO=AccessRecords.objects.filter(date__year__gt='2000')
    QLAO=AccessRecords.objects.filter(date__year__lte='2000')
    QLAO=AccessRecords.objects.filter(date__month='04')
    QLAO=AccessRecords.objects.filter(date__day='09')
    QLAO=AccessRecords.objects.filter(pk__in=[1,4])
    QLAO=AccessRecords.objects.filter(date__year__in=['2000','1996'])


    d={'access':QLAO}
    return render(request,'display_access.html',d)


def insert_topic(request):

    tn=input('enter topic name: ')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()

    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'display_topic.html',d)


def insert_webpage(request):

    tn=input('enter topic name: ')
    n=input('enter name: ')
    u=input('enter url: ')
    e=input('enter email: ')

    TO=Topic.objects.get(topic_name=tn)

    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()


    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpage.html',d)

def insert_access(request):

    n=input('enter webpage name: ')
    a=input('enter author name: ')
    d=input('enter date: ')

    WO=Webpage.objects.get(name=n)

    NAO=AccessRecords.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()


    QLAO=AccessRecords.objects.all()
    d={'access':QLAO}
    return render(request,'display_access.html',d)

def update_webpages(request):
    Webpage.objects.all()


    #Webpage.objects.filter(topic_name='Cricket').update(name='Dhoni')
    #Webpage.objects.filter(name='Dhoni').update(url='https://Dhoni.com')
    #Webpage.objects.filter(name='Dhoni').update(topic_name='Foot Ball')
    #Webpage.objects.filter(name='Dhoni').update(topic_name='Cricket')
    #Webpage.objects.filter(topic_name='Cricket').update(name='Dhoni')

    #Webpage.objects.update_or_create(topic_name='Foot Ball',defaults={'name':'Sakthi'})
    #Webpage.objects.update_or_create(topic_name='Kabaddi',defaults={'name':'ram'})


    CTO=Topic.objects.get_or_create(topic_name='Cricket')[0]
    CTO.save()
    #Webpage.objects.update_or_create(name='Dhoni',defaults={'topic_name':CTO})
    #Webpage.objects.update_or_create(name='Virat',defaults={'topic_name':CTO})
    #Webpage.objects.update_or_create(topic_name='Cricket',defaults={'name':'Rohit'})
    Webpage.objects.update_or_create(name='Suresh Raina',defaults={'topic_name':CTO,'url':'http://suresh.in'})


    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpage.html',d)


def delete_webpage(request):
    QLWO=Webpage.objects.all()

    Webpage.objects.filter(name='Virat').delete()
    Webpage.objects.filter(url='https://Dhoni.com').delete()

    
    d={'webpages':QLWO}
    return render(request,'display_webpage.html',d)
