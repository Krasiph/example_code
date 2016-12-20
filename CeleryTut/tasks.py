import os

from celery import Celery
from celery import current_task

# tasks => The name of the current module; if I had named this file
#          "silly.py", the first argument would be 'silly'.
# broker => String Format : transport://userid:password@hostname:port/virtual_host
app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')

# This is a stupid workaround to get the backend to work on Windows.
# Hopefully a real fix will eventually be posted to the thread:
# https://github.com/celery/celery/issues/897
app.conf.update(CELERY_RESULT_BACKEND='rpc://')

@app.task
def add(x, y):
    print(current_task.backend)
    return x + y

@app.task
def tsum(numbers):
    return sum(numbers)

@app.task(bind=True, default_retry_delay=60)
def test_retry(self):
    p = 'C:\\tmp\\test.txt'
    
    if os.path.exists(p):
        with open(p, 'r') as f:
            s = f.read()
            return s
    
    else:
        self.retry(exc=RuntimeError('file does not exist'))