from __future__ import unicode_literals

from django.db import models
from polymorphic.models import PolymorphicModel
import datetime

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Director(Person):
    pass

class Pianist(Person):
    pass

class Class(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    description = models.CharField(max_length=400)

class Event(PolymorphicModel):
    director = models.ForeignKey(Director, null=True)
    location = models.ForeignKey(Location)
    pianist = models.ForeignKey(Pianist, null=True)
    date = models.DateTimeField(default=datetime.datetime.today)
    piece_of_music = models.CharField(max_length=50)
    competition_class = models.ForeignKey(Class)

class Band(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

class Ensemble(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    band = models.ForeignKey(Band)

class Participant(Person):
    band = models.ForeignKey(Band)

class Instrument(models.Model):
    name = models.CharField(max_length=30)

class SoloEvent(Event):
    participant = models.ForeignKey(Participant)
    instrument = models.ForeignKey(Instrument)

class EnsembleEvent(Event):
    ensemble = models.ForeignKey(Ensemble)

class BandEvent(Event):
    band = models.ForeignKey(Band)