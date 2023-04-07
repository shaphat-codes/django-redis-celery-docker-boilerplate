#this imports the app to be used 

from .celery import app as celery_app

__all__ = ('celery_app',)