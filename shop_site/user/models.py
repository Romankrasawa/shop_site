from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from slugify import slugify
from django.urls import reverse_lazy
from uuid import uuid4

class UserManager(BaseUserManager):

    def create_user(self, email, username, last_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not first_name:
            raise ValueError('Користувач повинен мати імя')
        if not email:
            raise ValueError('Користувач повинен мати електронну пошту')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, last_name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            username=username,
            last_name=last_name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

def photo_file_name(self, filename):
    return f"avatar/{slugify(self.email)}/{filename}"

class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    username = models.CharField(max_length = 30, verbose_name="Імя")
    last_name = models.CharField(max_length = 30, verbose_name="Прізвище")
    email = models.EmailField(max_length = 70, verbose_name='Електронна Пошта', unique=True)
    avatar = models.ImageField(upload_to=photo_file_name, default='default/default_avatar.png', verbose_name="Аватар")
    avatar_url = models.URLField(verbose_name="Аватар url", null=True, blank=True)
    is_superuser = models.BooleanField(default=False, verbose_name="Адміністратор")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, verbose_name="Активовано")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now = True, verbose_name="Оновлено")

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"   
    REQUIRED_FIELDS = ["email","last_name"]

    @property
    def get_avatar(self):
        return self.avatar_url if self.avatar_url else self.avatar.url
    get_avatar.fget.short_description = 'Аватар'

    # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
