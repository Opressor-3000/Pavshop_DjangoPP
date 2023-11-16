import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pavshop.settings")

app = Celery("pavshop")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

#celery -A django-celery-worker
#celery -A pavshop worker --beat --scheduler django --loglevel=info