from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinute, Resource, Event
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

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

@login_required
def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm
    else:
        form=MeetingForm()
    return render(request, 'clubapp/newmeeting.html', {'form': form})

@login_required
def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm
    else:
        form=ResourceForm()
    return render(request, 'clubapp/newresource.html', {'form': form})

def loginMessage(request):
    return render(request, 'clubapp/loginmessage.html')

def logoutMessage(request):
    return render(request, 'clubapp/logoutmessage.html')