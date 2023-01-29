import logging
from shop_site.celery import app

logger = logging.getLogger(__name__)

@app.task
def summ(x, y):
    logger.debug(x+y, extra={'user': 'user'})
