from rest_framework.serializers import ModelSerializer
from concepts.models import Concept


class ConceptSerializer(ModelSerializer):
    """Сериализер для понятий"""

    class Meta:
        model = Concept
        fields = '__all__'
