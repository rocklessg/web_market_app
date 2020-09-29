from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    seat_available = models.IntegerField()
    image_url = models.CharField(max_length=2085)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()