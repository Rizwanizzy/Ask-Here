from django.db import models
from authentication.models import CustomUser
# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    query = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Question ({self.date} {self.time})"