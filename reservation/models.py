from django.db import models
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Room(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    startTime = models.DateTimeField('start date')
    endTime = models.DateTimeField('end date')
    reason = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='reservation', on_delete=models.CASCADE)
    def __str__(self):
        return self.reason
