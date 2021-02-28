from django.contrib import admin

from translate.models import Product
from parler.admin import TranslatableAdmin


class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'description']


admin.site.register(Product, ProductAdmin)
