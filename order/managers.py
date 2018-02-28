from django.db.models import Manager
from django.utils import timezone
import traceback

class OrdermasterManger(Manager):
    def create(self, **validated_data):

        user_no = validated_data.get('user_no')
        validated_data['first_insert_uno'] = user_no
        validated_data['last_update_uno'] = user_no
        validated_data['first_insert_time'] = timezone.now()
        validated_data['last_update_time'] = timezone.now()

        ordermaster = self.model(
                        **validated_data
                    )

        ordermaster.save()
        return ordermaster