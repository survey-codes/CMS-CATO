from celery import shared_task

@shared_task
def power(n):
    """Return 2 to the n'th power"""
    return 2 ** n
