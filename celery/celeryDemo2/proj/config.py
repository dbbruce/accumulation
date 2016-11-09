#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import

#CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/5'
#BROKER_URL = 'redis://127.0.0.1:6379/6'

CELERY_TIMEZONE = 'Asia/Shanghai'
#CELERY_ENABLE_UTC = True
# mysql
CELERY_RESULT_BACKEND = 'db+mysql://root:123456@127.0.0.1/celerydemo'
# mysql
#BROKER_URL = 'sqla+mysql://root:123456@127.0.0.1/celerydemo'
#BROKER_URL = 'redis://127.0.0.1:6379/0'
BROKER_URL = 'amqp://guest:guest@192.168.1.70:5672//'
#CELERY_TASK_SERIALIZER = 'json'
#CELERY_RESULT_SERIALIZER = 'json'
#CELERY_ACCEPT_CONTENT=['json']

#CELERY_TIMEZONE = 'Asia/Shanghai'
#CELERY_ENABLE_UTC = True

CELERYD_CONCURRENCY = 20

from datetime import timedelta

#CELERYBEAT_SCHEDULE = {
#    'add-every-30-seconds': {
#         'task': 'proj.tasks.add2',
#         'schedule': timedelta(seconds=30),
#         'args': ()
#    },
#}


#from celery.schedules import crontab
#
#CELERYBEAT_SCHEDULE = {
#    # Executes every Monday morning at 7:30 A.M
#    'add-every-monday-morning': {
#        'task': 'proj.tasks.add3',
#        'schedule': crontab(hour=17, minute=14),
#        #'args': (16, 16),
#    },
#    'add-every-30-seconds': {
#         'task': 'proj.tasks.add2',
#         'schedule': timedelta(seconds=10),
#         'args': ()
#    },
#
#}
