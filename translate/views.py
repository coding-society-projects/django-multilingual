import django
from django.shortcuts import render, redirect

from translate.models import Product
from .forms import *


def home(request):
    context= {}
    context['language_code'] = django.utils.translation.get_language()
    context['products'] = Product.objects.all()
    return render(request, 'translate/home.html', context)

def person_form(request):
    context = {}
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/translate/home')
    else:
        form = PersonForm()
        context['form'] = form
    return render(request, 'person_form.html', context)

def persons(request):
    context = {} 
    context['persons'] = Person.objects.all()
    return render(request, 'persons.html', context)
