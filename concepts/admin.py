from django.contrib.admin import ModelAdmin, register

from .models import Concept


@register(Concept)
class ConceptAdmin(ModelAdmin):
    list_display = ['pk', 'name', 'definition',
                    'image']
