from celery import Celery
import os

CELERY_BROKER = os.getenv("REDIS_URL")
CELERY_BACKEND = os.getenv("REDIS_URL")

celery_app = Celery("worker", broker=CELERY_BROKER, backend=CELERY_BACKEND)

@celery_app.task
def add(x, y):
    return x + y
