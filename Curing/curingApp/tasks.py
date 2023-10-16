# your_app/tasks.py

from celery import Celery
from django.utils import timezone
from datetime import timedelta
from .models import Pole, CuringSchedule
app = Celery('Curing')
@app.task
def generate_curing_schedules():

    poles_to_cure = Pole.objects.filter(project_name='Ashoka') 

    start_date = timezone.now().replace(hour=11, minute=0, second=0, microsecond=0) + timedelta(days=1)  

    for _ in range(10):
        for pole in poles_to_cure:
            curing_schedule = CuringSchedule.objects.create(pole=pole, start_date=start_date)
           
        start_date += timedelta(days=1)
