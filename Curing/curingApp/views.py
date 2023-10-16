from django.shortcuts import render
from .models import Pole,CuringSchedule
from django.utils import timezone
from datetime import timedelta
from Logfile import logdata

from django.shortcuts import render
from .models import Pole, CuringSchedule
from django.utils import timezone
from datetime import timedelta

def generate_curing_schedules(request):
    # Define your criteria to select poles for curing
    poles_to_cure = Pole.objects.filter(project_name='Gangpur_Road')  # Add your filter criteria here
    schedules_generated = []  # Create an empty list to hold the generated schedules

    # Calculate the start date for curing (10 days from now at 11 am)
    start_date = timezone.now().replace(hour=12, minute=45, second=0, microsecond=0) + timedelta(days=1)  # Start from tomorrow

    for _ in range(10):
        for pole in poles_to_cure:
            curing_schedule = CuringSchedule.objects.create(pole=pole, start_date=start_date)
            schedules_generated.append(curing_schedule)
        
        # Move to the next day
        start_date += timedelta(days=1)

    return render(request, 'curingApp/schedule_generated.html', {'schedules_generated': schedules_generated})
