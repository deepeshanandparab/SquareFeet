from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    building_name = models.CharField(max_length=100)
    wing = models.CharField(max_length=10)
    floor = models.IntegerField(default=0)
    flat_no = models.IntegerField(default=0)
    bedroom = models.IntegerField(default=0)
    bathroom = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    parking_available = models.CharField(max_length=10)
    two_wheeler = models.IntegerField(default=0)
    four_wheeler = models.IntegerField(default=0)
    yearly_maintenance = models.IntegerField(default=0)
    furnishing = models.CharField(max_length=20)
    gym = models.CharField(max_length=3)
    swimming_pool = models.CharField(max_length=3)
    playground = models.CharField(max_length=3)
    power_backup = models.CharField(max_length=3)
    club_house = models.CharField(max_length=3)
    area = models.IntegerField(default=0)
    pincode = models.IntegerField(default=0)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    date_added = models.DateTimeField('property_added')
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.type