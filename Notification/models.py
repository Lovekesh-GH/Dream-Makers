from django.db import models

# Create your models here.

class Notification(models.Model):
    Text = models.CharField(max_length=100,null=False)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    notification_time = models.TimeField()

    def __str__(self):
        return self.date