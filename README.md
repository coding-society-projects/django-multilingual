# Multi-Language Django

## A. Translated labels and Language selection

1.  In HTML page add 
    ```{% load i18n %}``` 
    (must be added to child pages if this is a base template)

1.  Add texts to be translated: 
    ```
    {% translate "Welcome" %}
    ```

1.  Check settings.py that USE_I18N is set to True

1.  Create a folder **locale** in the application folder
5. Execute ```django-admin makemessages -l it```, where in place of **"it"** put 
   the language code you want. This will generate a folder 'it' and a file django.po in it. In this file it will put all the text designated as 'translate' (msgid) and will provide a msgstr attribute to set their translation in this language.
6. Once the translations are set, compile the message file: ```django-admin compilemessages```
7. In setting.py add "django.middleware.locale.LocaleMiddleware" 
right after the SessionMiddleware in the MIDDLEWARE list
8. In urls.py import the i18n_patterns: ```from django.conf.urls.i18n import i18n_patterns```
9. Add the available languages in settings.py:
```
LANGUAGES = [
    ('en', 'English'),
    ('it', 'Italian'),
]
```

10. use a language prefix in front of urls
```
urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('translate/', include('translate.urls')),
)
```

**Add language selection in web page**:
```
<form action="{% url 'set_language' %}" method="post">{% csrf_token %}
    <input type="hidden" name="next" value="{{ request.path|slice:'3:' }}">
    <select name="language" id="">
        {% get_current_language as LANGUAGE_CODE %}
        {% get_available_languages as LANGUAGES %}
        {% get_language_info_list for LANGUAGES as languages %}
        {% for lang in languages %}
            <option value="{{ lang.code }}" {% if lang.code == LANGUAGE_CODE %} selected {% endif %}>
                {{ lang.name }} ({{ lang.code }})
            </option>
        {% endfor %}
    </select>
    <input type="submit" value="Go">
    </form>
```
The ```value="{{ request.path|slice:'3:' }}``` will extract the URL without the domain and without 
the language prefix, so the controller will redirect to the changed language which will 
be set by ```set_language```.

## B. Translated data 

1. We use the ```parler``` package. This must be installed with pip and be added in the 
settings.py INSTALLED_APPS.
1. Now the model will define the translated fields:
```
class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, db_index=True),
        description=models.TextField(blank=True)
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
```
This will create a table ```product``` and a second table ```product_translation``` 
with one-to-many relationship.
3. When retrieving data from the table the rows of the selected language will be retrieved.

