from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


def validate_phone(number):
    if len(number) != 11 or not number.isdigit():
        raise ValidationError('معذرة  رقم التليفون غير صحيح')
    



class User(AbstractUser):
    full_name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='photo_user')
    phone=models.CharField(max_length=25,validators=[validate_phone])
    job=models.CharField(max_length=75)
    notes=models.TextField(max_length=1500,null=True,blank=True)

    first_name=None
    last_name=None


    def __str__(self):
        return self.full_name
