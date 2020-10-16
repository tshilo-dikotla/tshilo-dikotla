from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tshilo_dikotla.settings')

app = Celery('tshilo_dikotla')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    "schedule-odk-data-pull": {
        "task": "edc_odk.tasks.pull_all_data_from_odk",
        "schedule": crontab(minute="*", day_of_week='mon-fri')
    }
}
