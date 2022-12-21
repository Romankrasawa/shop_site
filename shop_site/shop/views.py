from django.shortcuts import render
# Create your views here.
def home(request):
    context = {
            'title': 'Homy',
            }
    return render(request, template_name = "shop/home.html", context = context)
