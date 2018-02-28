from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, UpdateAPIView
)
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Emailschedule, Schedulemaster
from .serializers import (
    AlarmSchedulesSerializer, EmailSchedulesSerializer, ScheduleDetailSerializer, ScheduleSerializer
)

from rest_framework import mixins, views


class ScheduleAPIView(ListCreateAPIView):
    """알람 관련 스케쥴 리스트/등록"""
    permission_classes = [AllowAny,]
    serializer_class = ScheduleSerializer

    def get_queryset(self, request, *args, **kwargs):
        query_params = self.request.query_params
        user_no = query_params.get('user_no')
        schedule_type = query_params.get('schedule_type')

        queryset_list = Schedulemaster.objects.all()
        if user_no and schedule_type:
            queryset_list = Schedulemaster.objects.filter(user_no=user_no, schedule_type=schedule_type).all()
        elif user_no and not schedule_type:
            queryset_list = Schedulemaster.objects.filter(user_no=user_no).order_by('-first_insert_time').all()
        elif schedule_type and not user_no:
            queryset_list = Schedulemaster.objects.filter(schedule_type=schedule_type).order_by('-first_insert_time').all()
        return queryset_list

    def post(self, request, *args, **kwargs):
        data = self.request.data

        serialzier = ScheduleSerializer(data=data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data, status=status.HTTP_201_CREATED)
        return Response(serialzier.errors, status=status.HTTP_400_BAD_REQUEST)

class ScheduleDetailAPIView(RetrieveUpdateDestroyAPIView):
    """알람 관련 스케쥴 수정/삭제"""
    permission_classes = [AllowAny]
    serializer_class = ScheduleDetailSerializer

    def patch(self, request, schedule_no, *args, **kwargs):
        schedulemaster = Schedulemaster.objects.filter(no=schedule_no).all()
        if not schedulemaster:
            return Response({"message": "invalid scheduleNo"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ScheduleDetailSerializer(schedulemaster.first(), self.request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailSchedulesAPIView(ListCreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = EmailSchedulesSerializer

    def get_queryset(self, *args, **kwargs):
        query_params = self.request.query_params
        emailSchedule_obj = None

        if query_params.get('userno'):
            emailSchedule_obj = Emailschedule.objects.filter(user_no=query_params['userno']).order_by('-first_insert_time')
        else:
            emailSchedule_obj = Emailschedule.objects.all()
        return emailSchedule_obj

    def post(self, request, *args, **kwargs):
        """schedules add"""
        data = self.request.data

        serilaizer = EmailSchedulesSerializer(data=data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AlarmSchedulesAPIVIew(ListCreateAPIView):
#     permission_classes = [AllowAny, ]
#     serializer_class = AlarmSchedulesSerializer
#
#     def get(self):
#         pass
#     def post(self):
#         pass