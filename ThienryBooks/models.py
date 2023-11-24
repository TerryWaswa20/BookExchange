from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Parent(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=80)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=16)
    confirm_password = models.CharField(max_length=16)

    def __str__(self):
        return self.first_name + '   ' + self.last_name + ' ' + self.email + '  ' + self.username + ' ' + self.password


class Hiring(models.Model):
    official_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    location = models.CharField(max_length=80)
    book_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.official_name + '  ' + self.location


class Purchase(models.Model):
    official_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=14)
    location = models.CharField(max_length=80)

    def __str__(self):
        return self.official_name + ' ' + self.location


