from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

from rest_framework_simplejwt.tokens import RefreshToken

from apps.common.models import BaseModel


class User(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)
    
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    
    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
        
class UserProfile(BaseModel):
    image = models.ImageField(default='users/default.png', upload_to='users/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    