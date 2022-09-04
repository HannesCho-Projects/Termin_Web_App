from django.db import models
from django_countries.fields import CountryField
from users.models import User


class House(models.Model):

    """House Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=140)
    guests = models.PositiveIntegerField()
    beds = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    baths = models.PositiveIntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
