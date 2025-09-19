from django.db import models

class UserActive(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    code = models.CharField()