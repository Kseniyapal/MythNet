from rest_framework.viewsets import ModelViewSet
from concepts.models import Concept
from api.serializers import ConceptSerializer
from rest_framework import filters
from django.shortcuts import render


class ConceptViewSet(ModelViewSet):
    """Вьюсет для понятий"""

    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return render(request,  'pages/list_concepts.html', {'objects': serializer.data})
        else:
            return render(request, 'pages/index.html')

