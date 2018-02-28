from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework.authentication import TokenAuthentication
from .token import get_token_from_cache, validate_token
from rest_framework import HTTP_HEADER_ENCODING, exceptions, authentication

from rest_framework.compat import authenticate

class SettingsBackend(object):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.
    Use the login name and a hash of the password. For example:
    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """
    def authenticate(self, request, ownersitecode=None, username=None, password=None):
        #print('SettingsBackend authenticate')
        #login_valid = (settings.ADMIN_LOGIN == username)
        # pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        login_valid = True
        pwd_valid = True

        if login_valid and pwd_valid:
            try:
                return self._check_password(ownersitecode, username, password)
            except:
                return None
        return None

    def _check_password(self, ownersitecode=None, usernmae=None, password=None):
        user = self.get_user(ownersitecode, usernmae)
        if user.password_type == 'MD5':
            userpassword = password
        else:
            userpassword = password

        if user.user_password == userpassword:
            return user
        else:
            return None

    def get_user(self, ownersitecode, username):
        try:
            return get_user_model().objects.get(owner_site_code=ownersitecode, user_id=username)
        except User.DoesNotExist:
            return None


class CustomTokenAuthentication(TokenAuthentication):
    """
    Simple token based authentication.
    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:
        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'Token'
    model = None

    def get_model(self):
        if self.model is not None:
            return self.model
        from rest_framework.authtoken.models import Token
        return Token

    """
    A custom token model may be used, but must have the following properties.
    * key -- The string identifying the token
    * user -- The user to which the token belongs
    """

    def authenticate(self, request):
        #print('CustomTokenAuthentication authenticate')
        auth = authentication.get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        #model = self.get_model()
        model = validate_token(key)
        if model is not None:
            return (model, key)
        else:
            raise exceptions.AuthenticationFailed('Incorrect Token')

        # try:
        #     token = model.objects.select_related('user').get(key=key)
        # except model.DoesNotExist:
        #     raise exceptions.AuthenticationFailed(_('Invalid token.'))

        # if not token.user.is_active:
        #     raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        #return (token.user, token)

    def authenticate_header(self, request):
        return self.keyword