from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, db_index=True),
        description=models.TextField(blank=True)
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()


class Person(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')
