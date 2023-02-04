import logging
from .views import error_500
from django.urls import reverse_lazy
from django.shortcuts import render

logger = logging.getLogger(__name__)

class Process500:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        return self._get_response(request)

    def process_exception(self, request, exception):
        logger.error(str(exception))
        return render(request, 'shop/500.html', context={"message" : exception})

