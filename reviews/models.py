from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    rating_val = "default=1, validators = [MaxValueValidator(5), MinValueValidator(1)]"
    review = models.TextField()
    accuracy = models.PositiveIntegerField(rating_val)
    communication = models.PositiveIntegerField(rating_val)
    cleanliness = models.PositiveIntegerField(rating_val)
    location = models.PositiveIntegerField(rating_val)
    check_in = models.PositiveIntegerField(rating_val)
    value = models.PositiveIntegerField(rating_val)
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "houses.House", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

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
