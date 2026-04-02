from datetime import datetime
from django.db import models
from django.utils import timezone
from datetime import timedelta



# Create your models here.

class Post(models.Model):

    title=models.CharField(max_length=100)
    body=models.CharField(max_length=1000000)
    created_at=models.DateTimeField(default=timezone.now,blank=True)

    def was_published_in_past(self):
        now = timezone.now()
        return  self.created_at <= now
    
    def was_published_recently(self):
        now = timezone.now()
        return  now - timedelta(days=1) <=self.created_at <= now 
    







