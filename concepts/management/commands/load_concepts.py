import json

from django.core.management.base import BaseCommand

from concepts.models import Concept


class Command(BaseCommand):
    """Management команда для загрузки данных из json файла"""

    def handle(self):
        file_path = 'data_myth.json'

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for term in data['terms']:
            concept = Concept.objects.create(
                name=term['term'],
                definition=term['description'],
                image=term['image']
            )

            for relation in term['relations']:
                relation_type = relation['type']
                related_concepts = Concept.objects.filter(
                    id=relation['id_rel'])
                if relation_type == 'synonym':
                    concept.synonym.add(*related_concepts)
                elif relation_type == 'antonym':
                    concept.antonym.add(*related_concepts)
                elif relation_type == 'association':
                    concept.association.add(*related_concepts)

        self.stdout.write(self.style.SUCCESS('Concepts loaded successfully'))
