# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


# null is database-related. 
#    When a field has null=True it can store a database entry as NULL, meaning no value.
# blank is validation-related. 
#    If blank=True then a form will allow an empty value, whereas
#    if blank=False then a value is required.