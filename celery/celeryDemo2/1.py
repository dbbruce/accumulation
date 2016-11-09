# coding:utf-8
from proj.tasks import add
for i in range(1000000):
    r= add.delay(6)
