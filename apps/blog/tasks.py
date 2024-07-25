from celery import shared_task
import logging


@shared_task
def save_post(form):
    logger = logging.getLogger("django")
    logger.info("Start saving post")
    form.save()
    logger.info("Form saved")
