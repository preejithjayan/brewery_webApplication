from django.db import models
from django.contrib.auth.models import User
import uuid

class Brewery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255, default='Unknown')
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    website_url = models.URLField()

class Review(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
