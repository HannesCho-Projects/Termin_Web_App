from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    houses = models.ManyToManyField("houses.House", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_houses(self):
        return self.houses.count()

    count_houses.short_description = "Number of Houses"
