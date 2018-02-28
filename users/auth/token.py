import binascii
import os
from django.core.cache import cache
from ..models import usermaster
from django.db import models
from .token_cache import get_token_from_cache, set_cache, get_userno_from_cache, delete_token_cache

def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()

def get_or_create_token(user):
    user_no = str(user.user_no)
    token = get_token_from_cache(user_no)
    if token is None:
        token = generate_key()
        set_cache(user_no, token)
    return token

def validate_token(token):
    user_no = get_userno_from_cache(token)
    if user_no is not None:
        return usermaster.objects.get(user_no=user_no)
    else:
        return None

def delete_token(user):
    user_no = user.user_no
    token = get_token_from_cache(user_no)
    if token is not None:
        delete_token_cache(user_no, token)