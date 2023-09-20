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
    synonym = models.ManyToManyField('self',
                                     blank=True,)
    antonym = models.ManyToManyField('self',
                                     blank=True,)
    association = models.ManyToManyField('self', blank=True)

    def get_id(self):
        return self.pk
