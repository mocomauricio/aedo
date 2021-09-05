import os
from uuid import uuid4

from django.db import models
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


def path_and_rename(instance, filename):
    path = 'photos/profile'
    ext = filename.split('.')[-1]

    # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)

    # return the whole path to the file
    return os.path.join(path, filename)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'


    photo = models.ImageField(
        verbose_name = 'foto',
        upload_to=path_and_rename, 
        max_length=255, 
        default='default-profile.jpg',
    )

    first_name = models.CharField(
        verbose_name='nombres', 
        max_length=150
    )

    last_name = models.CharField(
        verbose_name='apellidos', 
        max_length=150
    )

    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )


    is_staff = models.BooleanField(
        verbose_name= 'staff',
        default=False
    )

    is_active = models.BooleanField(
        verbose_name = 'activo',
        default=True
    )

    date_joined = models.DateTimeField(
        verbose_name = 'fecha de Creacion', 
        default=timezone.now
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        first_name = self.first_name.split(' ')[0]
        last_name = self.last_name.split(' ')[0]
        short_name = '%s %s' % (first_name, last_name)
        return short_name

    def __str__(self):
        return self.get_full_name()
