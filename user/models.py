from django.db import models
from django.db.models import Model, CASCADE
from django.db.models.fields import CharField, EmailField, IntegerField, BooleanField, URLField
import uuid
# Create your models here.


class Users(Model):
     """
     User Details
     """
     
     id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
     username = CharField('username', max_length=255, null=False, unique=True,
                          blank=False)

     phone = CharField('phone', max_length=13, null=False, unique=False)

     email = EmailField('email', unique=True)
     score = IntegerField('score',default=0)
     profileImage = URLField('profileImage', max_length=255, null=True, blank=True)

     def __str__(self) -> str:
         return self.username
