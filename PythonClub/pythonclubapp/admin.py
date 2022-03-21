from django.contrib import admin
from .models import Meeting,MeetMinute,Resource,Event
# Register your models here.
admin.site.register(Meeting)
admin.site.register(MeetMinute)
admin.site.register(Resource)
admin.site.register(Event)