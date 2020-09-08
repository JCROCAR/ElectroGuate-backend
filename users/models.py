from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.utils import timezone
from utils.mixins import SoftDestroyModelMixin
from utils.models.base import BaseModel

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class UserManager(BaseUserManager):
    """
    Define the methods that are called when using the 'python manage.py createsuperuser' command.
    """
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password=None, **extra_fields):
        """
        Define normal user creation.
        """
        # Uncomment if the 'is_superuser' field is not overridden
        #extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    def create_superuser(self, email, password, **extra_fields):
        """
        Define the creation of superusers.
        """
        # Uncomment if the 'is_superuser' field is not overridden
        #extra_fields.setdefault('is_superuser', True)
        #if extra_fields.get('is_superuser') is not True:
        #    raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields) 

class User(AbstractBaseUser, BaseModel , SoftDestroyModelMixin):
    """
    Model for 'User', Users and registration.
    Overwrite the DRF base class. 
    """
    # Cancellation of fields not required
    #   is_superuser = models.BooleanField('is_superuser', default=False)
    username = None
    last_login = None
    is_superuser = None
    
    str_name = models.CharField(max_length=45, blank=False)
    str_surname = models.CharField(max_length=45, blank=False)
    str_email = models.EmailField('email_address', unique=True)
    str_role = models.CharField(max_length=25, blank=True, default="usuario")
    str_phone_number = models.CharField(max_length=12, blank=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'str_email'
    REQUIRED_FIELDS = ['str_name', 'str_phone_number']


# SIGNAL PARA CREACIÓN DEL TOKEN AL CREAR USUARIO
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
