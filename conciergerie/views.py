from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .usermanagement import *
from .models import Utilisateur, Service, PlaceType, Place, Event, Participants, Activite, TypeActivite

@login_required
def index(request):
    user = ''
    if request.user:
        user = request.user
    util = Utilisateur.objects.filter(user=user)
    activites = []
    activite = Activite.objects.filter(user=util[0]).order_by('date')[:3]
    for e in activite:
        date =e.event.date
        e.day =date.strftime('%d')
        e.month = date.strftime('%B')
        e.date = e.date.strftime('%A %d %B %Y')
        e.event.date = date.strftime('%A %d %B %Y')
        activites.append(e)
    return render(request, 'index.html', {'avatar': util[0].avatar, 'activites': activites})


@login_required
def create_event(request):
    user = ''
    if request.user:
        user = request.user
    util = Utilisateur.objects.filter(user=user)
    services = Service.objects.all()
    placetypes = PlaceType.objects.all()

    if len(request.POST) > 0:
        post = request.POST
        title = post['title']
        desc = post['desc']
        date = post['date']
        hour = post['hour']
        minutes = post['minutes']
        if post['place']!="":
            place = Place.objects.filter(id=post['place'])[0]
        else:
            place = "L'entreprise"
        service = Service.objects.filter(id=post['service'])[0]

        event = Event()
        event.title = title
        event.desc = desc
        event.place = place
        event.organizer = util[0]
        event.service = service

        realdate = datetime.strptime(date, "%d-%m-%Y")
        realdate = realdate.replace(minute=int(minutes), hour=int(hour), second=0)

        event.date = realdate

        event.save()
        invites = post['invite'].split(",")
        for invite in invites:
            u = User.objects.filter(email=invite)
            if not u:
                pass
            else:
                u = Utilisateur.objects.filter(user=u[0])
                p = Participants()
                p.event = event
                p.invited = u[0]
                p.status = "pending"
                p.save()
                act = Activite()
                act.date = datetime.now()
                act.type = TypeActivite.objects.filter(id=2)[0]
                act.event = event
                act.user = u[0]
                act.save()
        a = Activite()
        a.date = datetime.now()
        a.type = TypeActivite.objects.filter(id=1)[0]
        a.event = event
        a.user = util[0]
        a.save()
        return redirect("/")
    else:
        return render(request, 'create_event.html',
                      {'avatar': util[0].avatar, 'services': services, 'placetypes': placetypes})


def getplace(request):
    placetype = request.GET.get('placetype', None)
    places = Place.objects.filter(placetype=placetype)
    json = {'results': []}
    for result in places:
        temp = result.__dict__
        temp['_state'] = ""
        json['results'].append(temp)
    return JsonResponse(json, safe=False)
