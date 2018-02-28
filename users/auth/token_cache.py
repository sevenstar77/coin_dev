from django.core.cache import cache

def set_cache(user_no, token):
        cache.set('token:userno:' + user_no, token, timeout=None)
        cache.set('token:value:'+ token, user_no, timeout=None)


def get_token_from_cache(user_no):
    try:
        token = cache.get('token:userno:' + user_no)
    except:
        token = None
    return token

def get_userno_from_cache(token):
    try:
        user_no = cache.get('token:value:' + str(token))
    except:
        user_no = None
    return user_no

def delete_token_cache(user_no, token):
    cache.delete('token:userno:'+ user_no)
    cache.delete('token:value:'+ token)