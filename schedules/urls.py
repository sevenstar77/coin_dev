from django.conf.urls import url, include
from .views import ScheduleAPIView, ScheduleDetailAPIView, EmailSchedulesAPIView#, AlarmSchedulesAPIVIew

urlpatterns = [
    url(r'^scheduledetail/(?P<schedule_no>.+)/$', ScheduleDetailAPIView.as_view(), name='scheduleDetail'),
    url(r'^emailschedules', EmailSchedulesAPIView.as_view(), name='emailschedules'),
    url(r'^schedule', ScheduleAPIView.as_view(), name='schedule'),

    #url(r'^alarmSchedules', AlarmSchedulesAPIVIew.as_view(), name='alarmschedules'),
]