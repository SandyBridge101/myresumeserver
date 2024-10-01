from django.db import models
from django.utils import timezone
# Create your models here.

class Message(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.subject+' by '+self.name
    
