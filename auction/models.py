from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.models import User


# Create your models here.

class Auction(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="default.jpg", upload_to="items-pics")
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_min_value = models.IntegerField("Bid Starting Value")
    bid_start_date = models.DateField("Bid Starting Date")
    bid_end_date = models.DateField("Bid Ending Date")

    def get_absolute_url(self):
        return reverse('auction-detail', kwargs={'pk': self.pk})
