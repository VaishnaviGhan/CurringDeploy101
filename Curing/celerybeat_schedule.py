# celerybeat_schedule

from Curing.celery_config import Celery
from celery.schedules import crontab

app = Celery('Curing')

app.conf.beat_schedule = {
    'generate-curing-schedules-every-day': {
        'task': 'curingApp.tasks.generate_curing_schedules',
        'schedule': crontab(hour=11, minute=0),  # Run the task every day at 11:00 AM
    },
}
