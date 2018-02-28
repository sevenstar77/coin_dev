import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coin_dev.settings')

app = Celery('coin_dev')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(30.0, send_schedules_email.s('send_schedules_email'), name='send_schedules_email')
    #sender.add_periodic_task(20.0, auto_trading_schedules.s('auto_trading_schedules'), name='auto_trading_schedules')

@app.task
def auto_trading_schedules(args):
    """자동 매수/매도 order 테스크"""
    #from coinone.gateway.client.client import CoinOnePrivateAPIGateway
    from gateway.coinone.client import CoinOnePrivateAPIGateway
    from order.models import Ordermaster

    #TODO 나의 balance 등의 평균단가와 수량 가져오는 api/ 현재가격 api를 이용하여 수익률 계산 / 목표수익률과 비교하여 이상일 시 주문
    #account에 평균단가나오는 api 아직 못찾음
    ordermaster_data = {}
    user_no = 1
    price = 5000
    qty = 1
    currency = 'btc'
    payload = {
        'price': price,
        'qty': qty,
        'currency': currency
    }

    #제한 주문
    res_data = CoinOnePrivateAPIGateway.order_limit_buy(**payload)

    if res_data is not None:
        result = res_data.get('result', None)
        if result == 'success':
            ordermaster_data['order_id'] = res_data.get('orderId', None)
            ordermaster_data['price'] = price
            ordermaster_data['qty'] = qty
            ordermaster_data['currency'] = currency
            ordermaster_data['order_status'] = 'ORS001'
            ordermaster_data['user_no'] = user_no

            order_obj = Ordermaster.objects.create(**ordermaster_data)

@app.task
def delete_order_schedules(args):
    from gateway.coinone.client import CoinOnePrivateAPIGateway
    from order.models import Ordermaster

    Ordermaster.objects.filter(

    )

@app.task
def send_schedules_email(arg):
    """
    emailschedule에 있는 목록 메일 발송 스케쥴
    30분 단위로 발송한다.
    """

    from utils.mail import mail
    from schedules.models import Emailschedule, Schedulemaster
    from django.utils import timezone
    from gateway.coinone.client import ConinOnePublicAPIGateway

    # emailSchedules = Emailschedule.objects.filter(from_date__lte=timezone.now(), to_date__gte=timezone.now()).\
    #                 filter(is_email_receive='true', schedule_type='STT01').all()

    emailSchedules = Schedulemaster.objects.filter(from_date__lte=timezone.now(), to_date__gte=timezone.now()).\
                            filter(is_email_receive='true').all()


    #TODO 대량 스케쥴시 coinone api 호출 방법 변경 할것! 한꺼번에 currency 종류별로 호출해서 데이터 저장 후 사용 할것
    for emailSchedule in emailSchedules:
        params = {'currency': emailSchedule.currency}
        res_json = ConinOnePublicAPIGateway.connect(url=settings.COINONE_TICKER, methodType='GET', params=params,
                                                    payload=None)

        currency = res_json.get('currency', None)
        low_price = res_json.get('low', None)
        current_price = res_json.get('last', None)

        if currency == emailSchedule.currency:
            payload = {
                'name': emailSchedule.name,
                'receiveMail': emailSchedule.email,
                'currency': currency,
                'current_price': current_price,
                'low_price': low_price
            }
            mail.schedule_send_email(payload)


if __name__ =='__main__':
    app.start()
