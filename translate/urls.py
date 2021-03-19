from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('persons', views.persons),
    path('person/form', views.person_form),
]