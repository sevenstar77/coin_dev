import mimetypes
import smtplib
import socket
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import traceback
from django.conf import settings

#시간관계상 메일 서버 구축 x
#python email lib 로 임시 처리
#TODO 메일서버 구축 후 변경 할것!

HOST = 'smtp.gmail.com'
PORT = 587

def _contents(name, currency, current_price, low_price):

    html = """
            <html>
                <head><head>
                <body>
                    <p><b>안녕하세요. {name} 님<b></p>
                    coin_dev 에 메일 알람 등록해주신 정보입니다.<br> 
                    coin 종류 : {currency}<br>
                    현재가 : {current_price} 원<br>
                    24시간 내 최저가 : {low_price} 원 <br>
                    입니다. 감사합니다. 
                </body>
            </html>
            """.format(name=name, currency=currency, current_price=current_price, low_price=low_price)
    return html

def _send_email(payload):
    is_succeed = False
    sender = settings.SENDER_EMAIL
    password = settings.SENDER_PASSWORD

    name = payload.get('name')
    receiverMail = payload.get('receiveMail')
    currency = payload.get('currency')
    current_price = payload.get('current_price')
    low_price = payload.get('low_price')
    msg = MIMEBase('multipart', 'alternative')

    msg['Subject'] = 'gmail send test'
    msg['From'] = sender
    msg['To'] = receiverMail

    #TODO payload 데이터 가공하여 _contents 로 전달
    html = _contents(name, currency, current_price, low_price)

    html_text = MIMEText(html, 'html')
    msg.attach(html_text)
    s = smtplib.SMTP(HOST, PORT)

    try:
        s.starttls()
        s.login(sender, password)
        s.sendmail(sender, [receiverMail], msg.as_string())
        is_succeed = True
    except:
        is_succeed = False
    finally:
        s.close()

    return is_succeed

def schedule_send_email(payload):
    _send_email(payload)


