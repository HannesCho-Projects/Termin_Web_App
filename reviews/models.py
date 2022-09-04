from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    communication = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    cleanliness = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    location = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    check_in = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    value = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    house = models.ForeignKey(
        "houses.House", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.house}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "Avg."
