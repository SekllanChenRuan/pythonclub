from django.shortcuts import render
from .models import Meeting, MeetingMinute, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getResource(request):
    resource_list=Resource.objects.all()
    return render(request, 'clubapp/resource.html', {'resource_list': resource_list})