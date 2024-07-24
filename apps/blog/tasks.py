from celery import shared_task
from .forms import PostForm
import logging


@shared_task
def save_post(form_data, files, instance=None):
    logger = logging.getLogger("django")
    logger.info("Start saving post")
    if not instance:
        form = PostForm(form_data, files)
        logger.info("Get data from request and save into form")
        if form.is_valid():
            logger.info("Form is valid")
            form.save()
            logger.info("Form saved")
    else:
        form = PostForm(form_data, files, instance=instance)
        logger.info("Get data from request and save into form")
        if form.is_valid():
            logger.info("Form is valid")
            form.save()
            logger.info("Form saved")
