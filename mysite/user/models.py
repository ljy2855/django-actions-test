from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)

# Create your models here.
