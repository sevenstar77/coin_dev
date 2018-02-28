from rest_framework.serializers import ModelSerializer, CharField
from .models import Emailschedule, Schedulemaster


class ScheduleSerializer(ModelSerializer):

    class Meta:
        model = Schedulemaster
        #fields = '__all__'
        fields = ('name', 'email', 'is_email_receive', 'schedule_type', 'currency', 'from_date', 'to_date',
                  'price', 'target_up_price', 'target_down_price', 'target_up_percent', 'target_down_percent')

    def create(self, validated_data):
        schedule = Schedulemaster.objects.create_object(**validated_data)
        return schedule

class ScheduleDetailSerializer(ModelSerializer):

    class Meta:
        model = Schedulemaster
        fields = '__all__'


class EmailSchedulesSerializer(ModelSerializer):
    class Meta:
        model = Emailschedule
        fields = ('user_no', 'name', 'email', 'is_email_receive', 'schedule_type', 'currency', 'from_date'
                  , 'to_date')

        # def validate_mail_currency_schedule_type(self, value):
        #     pass

    def create(self, validated_data):
        emailschedule = Emailschedule.objects.create_object(**validated_data)
        return emailschedule

class AlarmSchedulesSerializer(ModelSerializer):
    pass