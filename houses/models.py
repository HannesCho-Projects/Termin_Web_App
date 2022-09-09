from django.db import models
from django_countries.fields import CountryField
from users.models import User
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class HouseType(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name = "Houes Type"


class Amenity(AbstractItem):

    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """Facility Model Definition"""

    pass

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("House", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


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
    host = models.ForeignKey(
        "users.User", related_name="houses", on_delete=models.CASCADE
    )
    house_type = models.ForeignKey(
        "HouseType", related_name="houses", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="houses", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="houses", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="houses", blank=True)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)
