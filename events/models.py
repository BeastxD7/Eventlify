from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.conf import settings

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=timezone.now)  # Set a default value
    time = models.TimeField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to='event_images/', 
        blank=True, 
        null=True, 
        default='/event_images/default.png'  # Path to the default image
    )
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)  # Allow nulls for first_name
    last_name = models.CharField(max_length=100, null=True)  # Allow nulls for last_name
    email = models.EmailField(null=True)                     # Field remains non-nullable
    contact = models.CharField(max_length=15, default="N/A")  # Allow nulls
    created_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.event.name}"

