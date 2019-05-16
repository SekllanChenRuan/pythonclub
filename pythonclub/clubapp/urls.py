from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getResource/', views.getResource, name='resources'),
    path('getMeeting/', views.getMeeting, name='meetings'),
    path('getMettingDetails/<int:id>', views.getMeetingDetails, name='meetingdetail'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newResource/', views.newResource, name='newresource'),
 ]

