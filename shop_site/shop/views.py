import logging
from django.shortcuts import render
from .models import *
# Create your views here.

logger = logging.getLogger(__name__)

def home(request):
    context = {
            'title': 'Головна',
            }
    request.session["category"] = {29474883 : 1,}
    logger.debug("okey", extra={'user': request.user})
    return render(request, template_name = "shop/home.html", context = context)

def search(request):
    context = {
            'title': 'Пошук',
            }
    cat = request.session["category"]["29474883"] = request.session["category"].get('29474883', 0) + 1
    request.session.modified = True
    logger.debug(cat , extra={'user': request.user})
    return render(request, template_name = "shop/search.html", context = context)

def product(request):
    context = {
            'title': 'Товар',
            }
    return render(request, template_name = "shop/product.html", context = context)

def catalog(request):
    context = {
            'title': 'Каталог',
            }
    return render(request, template_name = "shop/catalog.html", context = context)

def category(request):
    context = {
            'title': 'Категорія',
            }
    return render(request, template_name = "shop/categories.html", context = context)

def about_us(request):
    context = {
            'title': 'Про нас',
            }
    return render(request, template_name = "shop/about_us.html", context = context)

def feedback(request):
    context = {
            'title': 'Відгук',
            }
    return render(request, template_name = "shop/feedback.html", context = context)

def purcache_confirm(request):
    context = {
            'title': 'Підтвердження замовлення',
            }
    return render(request, template_name = "shop/purcache_confirm.html", context = context)

def purcache_result(request):
    context = {
            'title': 'Квитансія вашого замовлення',
            }
    return render(request, template_name = "shop/purcache_result.html", context = context)

