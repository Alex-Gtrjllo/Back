from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET(-1))
    address = models.CharField(max_length = 255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def _str_ (self):
        return self.user
    
class ProfileTwo(models.Model):
    profileModel = models.ForeignKey(User, on_delete = models.SET(-1))
    address = models.CharField(max_length = 255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def _str_ (self):
        return self.user

class ProfileUser(models.Model):
    name = models.CharField(max_length = 255, null=False)
    surnames = models.CharField(max_length = 255, null=False)
    age = models.IntegerField()
    email = models.EmailField()

    def _str_ (self):
        return self.user