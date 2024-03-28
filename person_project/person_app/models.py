from django.db import models

CHOICES = (('male','male'),('female','female'), ('other','other'))

class Person(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    email = models.EmailField()
    address = models.TextField()
    gender = models.CharField(max_length=20, choices=CHOICES)
    city = models.CharField(max_length = 50)
    pincode = models.IntegerField()
