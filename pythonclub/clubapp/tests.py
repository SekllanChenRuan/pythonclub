from django.test import TestCase
from .models import Meeting, MeetingMinute, Resource, Event
from .views import index, getResource, getMeeting, getMeetingDetails
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.

# Test for Models.
class MeetingTest(TestCase):
    def test_string(self):
        title=Meeting(meetingtitle="Help With Code!")
        self.assertEqual(str(title), title.meetingtitle)
    
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinuteTest(TestCase):
    def test_string(self):
        text=MeetingMinute(minutestext="It was nice")
        self.assertEqual(str(text), text.minutestext)
    
    def test_table(self):
        self.assertEqual(str(MeetingMinute._meta.db_table), 'meetingminute')

class ResourceTest(TestCase):
    def test_string(self):
        resource=Resource(resourcename="Intro to Python")
        self.assertEqual(str(resource), resource.resourcename)
    
    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'Resource')

class EventTest(TestCase):
    def test_string(self):
        eventname=Event(eventtitle="First Meeting")
        self.assertEqual(str(eventname), eventname.eventtitle)
    
    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'Event')

# Test for views.

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
class GetMeetingTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)

class GetMeetingDetailsTest(TestCase):
# Create sample test data.    
    def setUp(self):
        self.u=User.objects.create(username="CodingBatMan")
        self.meet=Meeting.objects.create(
            meetingtitle='Second Meeting',
            meetingdate='2019-05-09',
            meetingtime='12:00:00',
            location='A Cafe Somewhere',
            agenda="To talk about coding problems"
        )
        self.minutes=MeetingMinute.objects.create(
            meeting=self.meet,
            minutestext="Some filler",
        )
        self.minutes.attendance.add(self.u)
        
# Test view with id as parameter.
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('meetingdetail', args=(self.meet.id,)))
        self.assertEqual(response.status_code, 200)

# Test context.   
    def test_meetdetails(self):
        meetdetails=self.meet
        self.assertEqual(meetdetails, self.meet)

    def test_meetminute(self):
        meetminute=self.minutes
        self.assertEqual(meetminute, self.minutes)
    

