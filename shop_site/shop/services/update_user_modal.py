import logging

# Create your views here.

logger = logging.getLogger(__name__)

def execute(user):
       return logger.debug("coool", extra=user) 
