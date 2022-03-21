from django.test import TestCase
from pythonclubapp.forms import MeetingForm
from .models import Meeting, MeetMinute, Resource, Event
from .forms import MeetingForm,ResourceForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
# Create your tests here.
class MeetingTest(TestCase):
    def setup(self):
        
        meeting=Meeting(meetingTitle='meetingTest', meetingDate='10/25/2022',meetingTime='12:00', meetingLocation='virtual')
        return meeting

    def test_string(self):
        meet = self.setup()
        self.assertEqual(str(meet),meet.meetingTitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table),'meeting')

class ResourceTest(TestCase):
   def test_string(self):
       res=Resource(resourceName="library")
       self.assertEqual(str(res), res.resourceName)

   def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
   def test_string(self):
       event=Event(eventTitle="Testing event table")
       self.assertEqual(str(event), event.eventTitle)

   def test_table(self):
       self.assertEqual(str(Event._meta.db_table), 'event')

class NewMeetingForm(TestCase):
    def test_meetingForm(self):
        data={
            'meetingTitle':'testing',
            'meetingDate':'2022-3-6',
            'meetingTime':'12:00:00',
            'meetingLocation':'Library test',
            'meetingAgenda':'test'
        }
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)

class NewResourceForm(TestCase):
    def test_resourceForm(self):
        data={
            'resourcName':'testing',
            'resourceType':'2022-3-6',
            'dateEntered':'12:00:00',
            'resourceUrl':'https://www.microsoft.com',
            'resourceDescription':'test'
        }
        form=ResourceForm(data)
        self.assertTrue(form.is_valid)

class New_Meeting_Authenticaiton_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='user1',password='P@ssw0rd1')
        self.meeting=Meeting.objects.create(
            meetingTitle = 'test title',
            meetingDate = '2022-3-10',
            meetingTime = '13:00:00',
            meetingLocation = 'test office',
            meetingAgenda = 'testing'
        )

