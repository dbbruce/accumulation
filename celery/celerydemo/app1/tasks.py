from celery import task
from time import sleep
from celery import shared_task

@task(name = 'add_task_dong')
def add(x):
    for i in range(x):
        print i
        # sleep(10)
        fn = '/home/ethan/workspace/demo/celeryDemo/celerydemo/log/%s.log' %str(i)
        file = open(fn, "w")
        file.write(str(i))
        file.close()
    return x

@shared_task
def add2():
    k = 'abcedf'
    fn = '/home/ethan/workspace/demo/celeryDemo/celerydemo/log/%s.log' % k
    file = open(fn, "w")
    file.write(k)
    file.close()
    return k


