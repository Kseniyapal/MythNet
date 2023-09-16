from django.contrib import admin

from django.contrib.admin import ModelAdmin, register
from .models import Concept


@register(Concept)
class ConceptAdmin(ModelAdmin):
    list_display = ['name', 'definition',
                    'get_synonym',
                    'get_antonym',
                    'get_association']

    def get_synonym(self, obj):
        print(obj.synonym)
        return obj.synonym.name

    def get_antonym(self, obj):
        return obj.antonym.name

    def get_association(self, obj):
        return obj.association.name
