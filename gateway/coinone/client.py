import copy
import base64
import hmac
import hashlib
import time
import traceback
import requests
import simplejson as json
from django.conf import settings


def str_2_byte(s, encode='utf-8'):
    return bytes(s, encode)

class ConinOnePublicAPIGateway():
    TIMEOUT = 30

    def __init__(self):
        pass

    @classmethod
    def _get(cls, url, params):
        try:
            response = requests.get(url=url, params=params, timeout=cls.TIMEOUT)
            if response.status_code != 200:
                return {}
            rs_json = response.json()
            result = rs_json.get('result')

            if result == 'error':
                return {}
            #print('rs_json ::' , rs_json)
            return rs_json

        except ValueError:
            return {}
        except TimeoutError:
            return {}

    @classmethod
    def connect(cls, url, methodType, params, payload):
        if methodType == 'GET':

            rs_json = cls._get(url, params)
            return rs_json

class CoinOnePrivateAPIGateway():
    """
    conine one api gateway
      - https://api.coinone.co.kr/
    """

    TIMEOUT = 30
    SECRET_KEY = settings.COINONE_SECRET_KEY
    ACCESS_TOKEN = settings.COINONE_ACCESS_TOKEN

    BASE_URLS = 'https://api.coinone.co.kr/'

    # headers = {'Content-type': "application/json",
    #            'X-COINONE-PAYLOAD': X-COINONE-PAYLOAD,
    #            'X-COINONE-SIGNATURE': self.get_x_coinone_signature(payload), SECRET_KEY)
    #            }


    def __init__(self):
        pass

    @classmethod
    def x_coinone_signature(cls, payload):
        signature = hmac.new(str_2_byte(cls.SECRET_KEY.upper()), payload, hashlib.sha512)
        return signature.hexdigest()

    # @classmethod
    # def str_2_byte(s, encode='utf-8'):
    #     print('s :: ', s)
    #     return bytes(s, encode)

    @classmethod
    def x_coinone_payload(cls, payload):
        payload['nonce'] = int(time.time()*1000)
        dumped_json = json.dumps(payload)
        encoded_json = base64.b64encode(str_2_byte(dumped_json))
        return encoded_json

    @classmethod
    def get_headers(cls, payload):
        hedaers = {}

        encoded_json = cls.x_coinone_payload(payload)
        hedaers['Content-type'] = "application/json"
        hedaers['X-COINONE-PAYLOAD'] = encoded_json
        hedaers['X-COINONE-SIGNATURE'] = cls.x_coinone_signature(encoded_json)
        return hedaers

    @classmethod
    def get_encoded_payload(cls, payload):
        payload['nonce'] = int(time.time()*1000)
        dumped_json = json.dumps(payload)
        encoded_json = base64.b64encode(str_2_byte(dumped_json))
        return encoded_json

    @classmethod
    def _request(cls, url, payload):
        headers = cls.get_headers(payload)
        encoded_json = cls.get_encoded_payload(payload)

        try:
            response = requests.post(url, json=encoded_json, headers=headers, timeout=cls.TIMEOUT)
            if response.status_code != 200:
                return {}
            res_json = response.json()
            #print('res_json : ', res_json)
            result = res_json.get('result')

            if result == 'error':
                return {}
        except ValueError:
            return {}
        except TimeoutError:
            return {}
        return res_json

    @classmethod
    def account_balance(cls, **kwargs):
        payload = {
            'access_token': cls.ACCESS_TOKEN
        }
        balance_res = cls._request(settings.COINONE_ACCOUNT_BALANKCE, payload)
        return balance_res

    @classmethod
    def account_userinfo(cls, **kwargs):
        payload = {
            'access_token': cls.ACCESS_TOKEN
        }
        userinfo_res = cls._request(settings.COINONE_ACCOUNT_USER_INFO, payload)
        return userinfo_res

    @classmethod
    def order_limit_buy(cls, **kwargs):
        price = kwargs.get('price')
        qty = kwargs.get('qty')
        currency = kwargs.get('currency')
        payload = {
            'access_token': cls.ACCESS_TOKEN,
            'price': price,
            'qty': qty,
            'currency': currency,
        }
        limit_buy_res = cls._request(settings.COINONE_ORDER_LIMIT_BUY, payload)
        return limit_buy_res

    @classmethod
    def order_cancel(cls, **kwargs):
        order_id = kwargs.get('order_id')
        currency = kwargs.get('currency')
        price = kwargs.get('price')
        qty = kwargs.get('qty')
        is_ask = kwargs.get('is_ask')
        payload = {
            'order_id': order_id,
            'currency': currency,
            'price': price,
            'qty': qty,
            'is_ask': is_ask,
        }
        orercancel_res = cls._request(settings.COINONE_ORDER_CANCEL, payload)
        return orercancel_res

    @classmethod
    def order_info(cls, **kwargs):
        order_id = kwargs.get('order_id')
        currency = kwargs.get('currency')

        payload = {
            'order_id': order_id,
            'currency': currency
        }
        orerinfo_res = cls._request(settings.COINONE_ORDER_INFO, payload)
        return orerinfo_res