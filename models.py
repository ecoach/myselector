import json
import base64
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

# model for logging user data
class RSSLog(models.Model):
    who = models.ForeignKey(User, to_field='username', db_column='who') 
    mwhen = models.DateTimeField()
    link = models.CharField(max_length=200)
    article = models.CharField(max_length=200)

class ELog(models.Model):
    who = models.ForeignKey(User, to_field='username', db_column='who') 
    mwhen = models.DateTimeField()
    what = models.CharField(max_length=200)


