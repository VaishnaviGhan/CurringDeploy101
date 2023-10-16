# schedule_runserver.py

from apscheduler.schedulers.background import BackgroundScheduler
import subprocess

def start_server():
    subprocess.run(["python", "manage.py", "runserver"])

scheduler = BackgroundScheduler()
scheduler.add_job(start_server, 'cron', hour=11)
scheduler.start()

try:
    print("Server scheduler is running. Press Ctrl+C to exit.")
    scheduler.await_termination()
except KeyboardInterrupt:
    print("Server scheduler terminated manually.")
