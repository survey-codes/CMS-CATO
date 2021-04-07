from celery import shared_task

@shared_task
def hello():
    """Return Hello"""
    return 'Hello Daniel'
