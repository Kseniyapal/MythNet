import json
from pathlib import Path
from django.core.files import File
from concepts.models import Concept


json_file_path = 'data_myth.json'


with open(json_file_path) as file:
    data = json.load(file)


for term_data in data['terms']:

    concept = Concept.objects.create(
        name=term_data['term'],
        definition=term_data['description']
    )
    
    image_path = Path(term_data['image'])
    with open(image_path, 'rb') as image_file:
        concept.image.save(image_path.name, File(image_file))
    
    for relation in term_data['relations']:
        relation_type = relation['type']
        related_term_id = relation['id_rel']
        
        related_term = Concept.objects.get(id=related_term_id)
        
        if relation_type == 'synonym':
            concept.synonym.add(related_term)
        elif relation_type == 'antonym':
            concept.antonym.add(related_term)
        elif relation_type == 'association':
            concept.association.add(related_term)