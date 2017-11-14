from django.db import models
import json
# Create your models here.
class Place(models.Model):
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    place_name = models.CharField(max_length=255)
    created_date = models.DateField()

    def __str__(self):
        return self.place_name

class ZipCodePlace(models.Model):
    zipcode = models.IntegerField()
    lat = models.TextField()
    lng = models.TextField()

    def __str__(self):
        return self.zipcode
