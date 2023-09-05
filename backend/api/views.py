from rest_framework.viewsets import ModelViewSet
from concepts.models import Concept
from api.serializers import ConceptSerializer
from rest_framework import filters


class ConceptViewSet(ModelViewSet):
    """Вьюсет для понятий"""

    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name')
