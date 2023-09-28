from django.contrib.admin import ModelAdmin, register

from .models import Concept


@register(Concept)
class ConceptAdmin(ModelAdmin):
    """Регистрация модели в админке"""
    list_display = ['pk', 'name', 'definition',
                    'image']
