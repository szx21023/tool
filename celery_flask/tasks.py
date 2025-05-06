from celery_app import celery
import time

@celery.task(name="add")
def add(x, y):
    time.sleep(5)
    return x + y
