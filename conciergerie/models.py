from django.db import models
from django.contrib.auth.models import User


class Utilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.TextField()
    avatar = models.ImageField()


class PlaceType(models.Model):
    name = models.TextField()


class Service(models.Model):
    name = models.TextField()


class Place(models.Model):
    name = models.TextField()
    desc = models.TextField()
    tag1 = models.TextField()
    tag2 = models.TextField()
    tag3 = models.TextField()
    placetype = models.ForeignKey(
        'PlaceType',
        on_delete=models.CASCADE,
    )
    cost = models.TextField(null=True)
    nbvotes = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    img = models.ImageField(null=True)


class SercicePlaceType(models.Model):
    placetype = models.ForeignKey(
        'PlaceType',
        on_delete=models.CASCADE,
    )
    service = models.ForeignKey(
        'Service',
        on_delete=models.CASCADE,
    )


class Event(models.Model):
    title = models.TextField()
    desc = models.TextField()
    organizer = models.ForeignKey(
        'Utilisateur',
        on_delete=models.CASCADE,
    )
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        null=True
    )
    service = models.ForeignKey(
        'Service',
        on_delete=models.CASCADE,
        null=True
    )
    date = models.DateTimeField(null=True)


class Participants(models.Model):
    invited = models.ForeignKey(
        'Utilisateur',
        on_delete=models.CASCADE,
    )
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
    )
    status = models.TextField()


class TypeActivite(models.Model):
    name = models.TextField()


class Activite(models.Model):
    date = models.DateTimeField(null=True)
    type = models.ForeignKey(
        'TypeActivite',
        on_delete=models.CASCADE,
    )
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'Utilisateur',
        on_delete=models.CASCADE,
    )