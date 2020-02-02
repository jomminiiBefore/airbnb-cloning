from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition """

    review = models.TextField()
    Accuracy = models.TextField()
    communication = models.TextField()
    cleanliness = models.TextField()
    location = models.TextField()
    check_in = models.TextField()
    value = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"
