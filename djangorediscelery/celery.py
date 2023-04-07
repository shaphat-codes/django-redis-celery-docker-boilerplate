import os 
from celery import Celery
from decouple import config

from celery.schedules import crontab


#set default django settings module for the celery program

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangorediscelery.settings')

app = Celery('djangorediscelery')

app.config_from_object('django.conf:settings', namespace='CELERY')


#LOAD TASK MODULES FROM ALL REGISTERED DJANGO APP CONFIGS
app.autodiscover_tasks()

# Scheduler
app.conf.beat_schedule = {
    'multiply-task-contrab': {
        'task': 'movies.tasks.mul',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },

    'multiply-every-5-seconds': {
        'task': 'movies.tasks.mul',
        'schedule': 5.0,
        'args': (16,16)
    },

    'add-every-30-seconds': {
        'task': 'movies.tasks.add',
        'schedule': 30.0,
        'args': (16,16)
    },

    'database': {
        'task': 'movies.tasks.bkup',
        'schedule': 5.0,
    },
}