from django.db import models
# from django.contrib.postgres.fields import ArrayField
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import BaseUserManager
# from slugify import slugify
# from django.urls import reverse_lazy
# import uuid
#
# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not username:
#             raise ValueError('Користувач повинен мати імя')
#         if not email:
#             raise ValueError('Користувач повинен мати електронну пошту')
#         user = self.model(
#             email=self.normalize_email(email),
#             username = username
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, email, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email=email,
#             username = username,
#             password=password,
#         )
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#
# def photo_file_name(self, filename):
#     return f"photos/{slugify(self.username)}/{filename}"
#
# class User(AbstractBaseUser, PermissionsMixin):
#     slug = models.SlugField(primary_key=True)
#     username = models.CharField(max_length = 30, verbose_name="Імя", unique=True)
    # email = models.EmailField(max_length = 70, verbose_name='Електронна Пошта', unique=True)
    # token = models.UUIDField(default=uuid.uuid4)
    # photo = models.ImageField(upload_to=photo_file_name, default='default/default_avatar.png', verbose_name="Фото")
    # is_superuser = models.BooleanField(default=False, verbose_name="Адміністратор")
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True, verbose_name="Активовано")
    # created_at = models.DateTimeField(auto_now_add = True, verbose_name="Створено")
    # updated_at = models.DateTimeField(auto_now = True, verbose_name="Оновлено")
    #
    # objects = UserManager()
    #
    # EMAIL_FIELD = "email"
    # USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["email"]
    #
    # # @property
    # # def get_liked_book(self):
    # #     return [book.title for book in self.liked_book.all()]
    # # get_liked_book.fget.short_description = 'Вподобані книги'
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.username)
    #     super(User, self).save(*args, **kwargs)
    #
    # def get_absolute_url(self):
    #     return reverse_lazy('profile', kwargs = {'user_id':self.slug})
    #
    # def __str__(self):
    #     return self.username
    #
    # class Meta:
    #     verbose_name = 'Користувач'
    #     verbose_name_plural = 'Користувачі'
