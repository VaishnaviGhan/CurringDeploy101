from django.db import models
class Pole(models.Model):
    project_name = models.CharField(max_length=255)
    pole_constructed = models.DateField()

class CuringSchedule(models.Model):
    pole = models.ForeignKey(Pole, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
