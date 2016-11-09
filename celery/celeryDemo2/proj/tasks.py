#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from proj.celery import app
from time import sleep
import time

@app.task
def add(x):
#    for i in range(x):
#        print i
#        sleep(10)
#        fn = '/home/ethan/workspace/demo/celeryDemo/celerydemo2/celeryDemo/proj/log/%s.log' %str(i)
#        file = open(fn, "w")
#        file.write(str(i))
#        file.close()
    return x

@app.task
def add2():
    sleep(10)
    i = time.time()
    fn = '/home/ethan/workspace/demo/celeryDemo/celerydemo2/celeryDemo/proj/log/%s.log' %str(i)
    file = open(fn, "w")
    file.write(str(i))
    file.close()
    return i


@app.task
def add3():
    i = 880030
    fn = '/home/ethan/workspace/demo/celeryDemo/celerydemo2/celeryDemo/proj/log/%s.log' %str(i)
    file = open(fn, "w")
    file.write(str(i))
    file.close()
    return i

