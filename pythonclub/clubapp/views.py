from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinute, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getResource(request):
    resource_list=Resource.objects.all()
    return render(request, 'clubapp/resource.html', {'resource_list': resource_list})

def getMeeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'clubapp/meeting.html', {'meeting_list': meeting_list})

def getMeetingDetails(request, id):
    meetdetail=get_object_or_404(MeetingMinute, pk=id)
    minutes=MeetingMinute.objects.filter(meeting=id)
    context={
        'meetdetails': meetdetail,
        'meetminute': minutes,
    }
    return render(request, 'clubapp/meetingdetail.html', context=context)