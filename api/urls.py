from django.urls import include, path
from rest_framework import routers

from .views import ConceptViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('concepts', ConceptViewSet, basename='concepts')

urlpatterns = [
    path('', include(router.urls))
    ]
