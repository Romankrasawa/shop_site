from django.shortcuts import render
from django.dispatch import receiver
from allauth.socialaccount.signals import pre_social_login
# Create your views here.
# @receiver(pre_social_login)
# def populate_profile(sender, **kwargs):
#     u = UserProfile( >>FACEBOOK_DATA<< )
#     u.save()
