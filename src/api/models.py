import uuid

from django.db import models


# Create your models here.

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    capacity = models.IntegerField(null=False, blank=False)


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    date = models.DateField(auto_now=False)
    type = models.CharField(max_length=10, null=True, blank=False)


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    date = models.DateField(auto_now=False)
    capacity = models.IntegerField(null=True, blank=False)
    customer_id = models.CharField(null=False, max_length=50)
