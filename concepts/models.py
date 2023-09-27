from django.db import models


class Concept(models.Model):
    """Модель понятие"""

    name = models.CharField(
        'Название',
        max_length=255
    )

    definition = models.CharField(
        'Определение',
        max_length=255
    )
    image = models.ImageField(
        'Картинка',
        upload_to='images/')

    synonym = models.ManyToManyField('self',
                                     blank=True,)
    antonym = models.ManyToManyField('self',
                                     blank=True,)
    association = models.ManyToManyField('self', blank=True)
