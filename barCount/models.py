from django.db import models

# Create your models here.

class Room(models.Model):
    num = models.IntegerField(primary_key=True, unique=True)
    debt = models.FloatField(default=0, blank=False)
    lastClearTime = models.DateTimeField()

