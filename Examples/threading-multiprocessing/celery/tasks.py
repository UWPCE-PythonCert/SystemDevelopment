from celery import Celery

celery = Celery('tasks', backend="amqp", broker='amqp://guest@localhost//')

@celery.task
def add(x, y):
    return x + y
