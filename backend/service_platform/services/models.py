from django.db import models
from django.contrib.auth.models import User




class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    bio = models.TextField()
    phone_number = models.CharField(max_length=15)


    def __str__(self):
        return f'{self.user.useranme}'