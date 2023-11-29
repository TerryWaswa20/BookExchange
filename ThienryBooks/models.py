from django.db import models
from django.contrib.auth.models import User
import datetime


class Hiring(models.Model):
    official_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    location = models.CharField(max_length=80)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    book_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.official_name + '  ' + self.location


class Purchase(models.Model):
    official_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=14)
    location = models.CharField(max_length=80)

    def __str__(self):
        return self.official_name + ' ' + self.location


class Exchange(models.Model):
    owner_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    book_title = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
    book_needed = models.CharField(max_length=50)
    upload_book = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.owner_name + ' ' + self.book_title + ' ' + self.book_author


class Order(models.Model):
    customer = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, default='')
    datetime = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    address = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.customer