from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Meeting(models.Model):
    meetingTitle=models.CharField(max_length=255)
    meetingDate=models.DateField(auto_now=False, auto_now_add=False)
    meetingTime=models.TimeField(auto_now=False, auto_now_add=False)
    meetingLocation=models.CharField(max_length=255)
    meetingAgenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingTitle

    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetMinute(models.Model):
    meetingId=models.ForeignKey(Meeting,on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minuteText=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingId

    class Meta:
        db_table='meetMinute'
        verbose_name_plural='meetingMinutes'

class Resource(models.Model):
    resourceName=models.CharField(max_length=255)
    resourceType=models.CharField(max_length=255)
    userId=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateEntered=models.DateField(auto_now=False, auto_now_add=False)
    resourceUrl=models.URLField(null=True, blank=True)
    resourceDescription=models.CharField(max_length=255)

    def __str__(self):
        return self.resourceName

    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventTitle=models.CharField(max_length=255)
    eventLocation=models.CharField(max_length=255)
    eventDate=models.DateField(auto_now=False, auto_now_add=False)
    eventTime=models.TimeField(auto_now=False, auto_now_add=False)
    eventDescription=models.CharField(max_length=255)
    eventPoster=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventTitle

    class Meta:
        db_table='event'
        verbose_name_plural='events'