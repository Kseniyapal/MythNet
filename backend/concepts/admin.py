from django.contrib import admin

from django.contrib.admin import ModelAdmin, register
from .models import Concept


@register(Concept)
class ConceptAdmin(ModelAdmin):
    list_display = ['name', 'definition']
