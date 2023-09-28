from django.core.paginator import Paginator
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api.serializers import ConceptSerializer
from concepts.models import Concept


def get_list_by_id(concepts, ids):
    """Получение списка по Id"""
    res = []
    for id in ids:
        object = next((item for item in concepts if item['id'] == id),
                      None)
        res.append(object)
    return res


class ConceptViewSet(ModelViewSet):
    """Вьюсет для понятий"""

    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('name',)
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        """Метод для вывода списка"""
        queryset = self.filter_queryset(self.get_queryset())
        paginator = Paginator(queryset, self.pagination_class.page_size)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = self.get_serializer(page_obj, many=True)
        return render(request, 'pages/list_concepts.html',
                      {'objects': serializer.data, 'page_obj': page_obj})

    def retrieve(self, request, *args, **kwargs):
        """Метод для рендера страницы конкретного понятия"""
        queryset = self.filter_queryset(self.get_queryset())
        serializer_concepts = self.get_serializer(queryset, many=True)
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        list_synonym = get_list_by_id(
            serializer_concepts.data, serializer.data['synonym']
            )
        list_antonym = get_list_by_id(
            serializer_concepts.data, serializer.data['antonym']
            )
        list_association = get_list_by_id(
            serializer_concepts.data, serializer.data['association']
            )
        return render(request,  'pages/concept.html',
                      {'object': serializer.data,
                       'synonyms': list_synonym,
                       'antonyms': list_antonym,
                       'associations': list_association})
