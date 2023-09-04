from django.db import models


class Concept(models.Model):

    name = models.CharField(
        'Название',
        max_length=255
    )

    definition = models.CharField(
        'Определение',
        max_length=255
    )
    synonym = models.ManyToManyField('self')
    antonym = models.ManyToManyField('self')
    association = models.ManyToManyField('self')
