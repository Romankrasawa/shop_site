import logging
from config.celery import app

logger = logging.getLogger(__name__)

@app.task
def summ(x, y):
    logger.debug(x+y, extra={'user': 'user'})
