from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


# Create your models here.

class Auction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_min_value = models.IntegerField()
    bid_start_date = models.DateTimeField()
    bid_end_date = models.DateTimeField()
