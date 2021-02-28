import django
from django.shortcuts import render

from translate.models import Product


def home(request):
    context= {}
    context['language_code'] = django.utils.translation.get_language()
    context['products'] = Product.objects.all()
    return render(request, 'translate/home.html', context)
