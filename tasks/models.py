from django.db import models
from user.models import Users

# Create your models here.

class NormalTasks(models.Model):
    task_name = models.CharField(max_length=100, null=False, blank=True)
    task_description = models.CharField(max_length=255, null=False)
    is_completed  = models.BooleanField(default=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    task_date = models.DateField()

    def __str__(self):
        return self.task_name


class SpecialTasks(models.Model):
    Stask_name = models.CharField(max_length=100, null=False, blank=True)
    Stask_description = models.CharField(max_length=255, null=False)
    is_completed  = models.BooleanField(default=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    task_date = models.DateField()

    def __str__(self):
        return self.Stask_name


class Completedtasks(models.Model):

    t_name = models.ForeignKey(NormalTasks, on_delete=models.CASCADE)
    image = models.URLField(default = 300)
    CompletedBy = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.t_name



class SCompletedtasks(models.Model):

    t_name = models.ForeignKey(SpecialTasks, on_delete=models.CASCADE)
    image = models.URLField(default = 300)
    CompletedBy = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.t_name