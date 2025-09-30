from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="listings")

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,
                                related_name="bookings")
    guest = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="bookings")
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["listing", "guest", "check_in", "check_out"],
                name="unique_booking"
            )
        ]

    def __str__(self):
        return f"Booking by {self.guest.username} for {self.listing.title}"


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,
                                related_name="reviews")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="reviews")
    rating = models.PositiveSmallIntegerField()  # e.g., 1–5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=1, rating__lte=5),
                name="valid_rating_range"
            )
        ]

    def __str__(self):
        return f"Review for {self.listing.title} by {self.reviewer.username}"
