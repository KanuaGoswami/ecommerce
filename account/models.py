from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .managers import customerUserManager

# Create your models here.

class customUser(AbstractUser):
    phone = models.CharField(max_length=10,unique=True)
    address = models.CharField(max_length=100)
  
    ADMIN = 1
    SELLER = 2
    USER =3
      
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (SELLER, 'Seller'),
        (USER, 'User'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=[]
    objects = customerUserManager()
    gst = models.CharField(max_length=15,blank=True, null=True)
    image = models.ImageField(upload_to='upload')



# class seller(customUser):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
    



    