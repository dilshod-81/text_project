from django.db import models

# Create your models here.

class Auth(models.Model):
    login = models.CharField()
