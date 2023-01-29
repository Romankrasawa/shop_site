import os
import shop_site
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_site.settings')

app = Celery('shop_site')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
