from django.db import models
from django.contrib.auth.models import User


class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=50)
    journal = models.TextField()
    sentiment = models.CharField(max_length=20, blank=True)
    stress_level = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mood