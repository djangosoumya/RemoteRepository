from django.db import models

class ContactData(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.BigIntegerField()
    course = models.CharField(max_length=20)

class FeedbackData(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    date = models.DateField(max_length=100)
    feedback = models.CharField(max_length=100)


# Create your models here.
