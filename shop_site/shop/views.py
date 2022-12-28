from django.shortcuts import render
# Create your views here.

def home(request):
    context = {
            'title': 'Головна',
            }
    return render(request, template_name = "shop/home.html", context = context)

def search(request):
    context = {
            'title': 'Пошук',
            }
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

