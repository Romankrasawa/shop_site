from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_field
from django.contrib.auth.backends import ModelBackend
from .models import User



class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def populate_user(self, request, sociallogin, data):
        """
        Adds google avatar to user.
        """
        user = super().populate_user(request, sociallogin, data)
        print(data)
        photo = sociallogin.account.extra_data['picture']
        try:
            user_field(user, "avatar_url", photo)
            user_field(user, "username", data.get("first_name"))
            user_field(user, "last_name", data.get("last_name"))
        except (KeyError, AttributeError):
            pass
        return user
    
    def save_user(self, request, user, form, commit=True):
        """
        Make user logined with allauth active.
        """
        user = super(CustomSocialAccountAdapter, self).save_user(request, user, form)
        user.is_superuser = True
        user.is_staff = True
        user.save()

class UserBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Log in using email.
        """
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

