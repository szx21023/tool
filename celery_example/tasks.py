import os
from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker=os.getenv('BROKER_URL'), backend=os.getenv('BACKEND_URL'))

# 配置定时任务
app.conf.beat_schedule = {
    'scheduled-task': {
        'task': 'tasks.scheduled_task',
        'schedule': crontab(minute='*'),  # 每分钟执行一次
    },
}

@app.task
def scheduled_task():
    print("This is a scheduled task.")

@app.task(name='task.add')
def add(x, y):
    return x + y