from __future__ import unicode_literals

import unicodedata

from django.contrib.auth import password_validation
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password
)
from django.db import models
from django.utils.crypto import get_random_string, salted_hmac
from django.utils.deprecation import CallableFalse, CallableTrue
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

class AbstractBaseUser(models.Model):

    #custom error 로 인하여 삭제
    #password = models.CharField(_('password'), max_length=128)
    #last_login = models.DateTimeField(_('last login'), blank=True, null=True)

    is_active = True

    REQUIRED_FIELDS = []

    class Meta:
        abstract = True

    def get_username(self):
        "Return the identifying username for this User"
        return getattr(self, self.USERNAME_FIELD)

    def __init__(self, *args, **kwargs):
        super(AbstractBaseUser, self).__init__(*args, **kwargs)
        # Stores the raw password if set_password() is called so that it can
        # be passed to password_changed() after the model is saved.
        self._password = None

    def __str__(self):
        return self.get_username()

    def clean(self):
        setattr(self, self.USERNAME_FIELD, self.normalize_username(self.get_username()))

    def save(self, *args, **kwargs):
        super(AbstractBaseUser, self).save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None

    def natural_key(self):
        return (self.get_username(),)

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return CallableFalse

    @property
    def is_authenticated(self):
        #print('is_authenticated~')
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return CallableTrue

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        # Set a value that will never be a valid hash
        self.password = make_password(None)

    def has_usable_password(self):
        return is_password_usable(self.password)

    def get_full_name(self):
        raise NotImplementedError('subclasses of AbstractBaseUser must provide a get_full_name() method')

    def get_short_name(self):
        raise NotImplementedError('subclasses of AbstractBaseUser must provide a get_short_name() method.')

    def get_session_auth_hash(self):
        """
        Return an HMAC of the password field.
        """
        key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        return salted_hmac(key_salt, self.password).hexdigest()

    @classmethod
    def get_email_field_name(cls):
        try:
            return cls.EMAIL_FIELD
        except AttributeError:
            return 'email'

    @classmethod
    def normalize_username(cls, username):
        return unicodedata.normalize('NFKC', force_text(username))