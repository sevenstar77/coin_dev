from django.db import models
from django.utils import timezone
from django.db import (
    DEFAULT_DB_ALIAS, DJANGO_VERSION_PICKLE_KEY, DatabaseError, connection,
    connections, router, transaction,
)

class EmailscheduleManager(models.Manager):
    def create_object(self, **validated_data):
        user_no = validated_data.get('user_no')

        emailschedule = self.model(
            user_no=validated_data.get('user_no', None),
            name=validated_data.get('name', None),
            email=validated_data.get('email', None),
            is_email_receive=validated_data.get('is_email_receive', 'false'),
            schedule_type=validated_data.get('schedule_type', 'STT01'),
            currency=validated_data.get('currency', 'ltc'),
            from_date=validated_data.get('from_date'),
            to_date=validated_data.get('to_date'),
            first_insert_uno=validated_data.get('first_insert_uno', user_no),
            first_insert_time=timezone.now(),
            last_update_uno=validated_data.get('last_update_uno', user_no),
            last_update_time=timezone.now()
        )
        emailschedule.save()

        return emailschedule

class SchedulemasterManager(models.Manager):

    def create_object(self, **validated_data):
        user_no = validated_data.get('user_no', 10000)
        schedule_type = validated_data.get('schedule_type', None)
        price = validated_data.get('price', None)
        target_up_price = validated_data.get('target_up_price', None)
        target_down_price = validated_data.get('target_down_price', None)
        target_up_percent = validated_data.get('target_up_percent', None)
        target_down_percent = validated_data.get('target_down_percent', None)

        if schedule_type is None:
            if target_down_price is not None or target_down_price is not None:
                schedule_type = 'STT02'
            elif (target_up_percent is not None or target_down_percent is not None) and price:
                schedule_type = 'STT03'
            else:
                schedule_type = 'STT01'

        schedulemaster = self.model(
            user_no=user_no,
            name=validated_data.get('name', None),
            email=validated_data.get('email', None),
            is_email_receive=validated_data.get('is_email_receive', 'false'),
            schedule_type=schedule_type,
            currency=validated_data.get('currency'),
            price=validated_data.get('price'),
            target_up_price=target_up_price,
            target_down_price=target_down_price,
            target_up_percent=target_up_percent,
            target_down_percent=target_down_percent,
            from_date=validated_data.get('from_date'),
            to_date=validated_data.get('to_date'),
            first_insert_uno=validated_data.get('first_insert_uno', user_no),
            first_insert_time=timezone.now(),
            last_update_uno=validated_data.get('last_update_uno', user_no),
            last_update_time=timezone.now()
            #**validated_data
        )

        schedulemaster.save()
        return schedulemaster