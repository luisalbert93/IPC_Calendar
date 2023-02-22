from datetime import datetime
from django.db import models
from django.urls import reverse
from django.db.models import Q

from calendarapp.models import EventAbstract
from accounts.models import User

class EventManager(models.Manager):
    def get_all_events(self, user):
        events = Event.objects.filter(is_active=True, is_deleted=False)
        return events

    def get_running_events(self, user):
        running_events = Event.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now().date(),
        ).order_by("start_time")
        return running_events

    def get_my_events(self, user):
        my_events = Event.objects.filter(user=user, is_active=True, is_deleted=False)
        return my_events

    def get_other_events(self, user):
        other_events = Event.objects.filter(~Q(user=user), is_active=True, is_deleted=False)
        return other_events

class Event(EventAbstract):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    objects = EventManager()

    def __str__(self):
        return self.title

   