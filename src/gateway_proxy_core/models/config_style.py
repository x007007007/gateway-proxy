from django.db import models

from gateway_proxy_core.models._mixin import ModelNameStrTrainMixin


# class ConfigDateModel(ModelNameStrTrainMixin, models.Model):
#     name = models.CharField(max_length=254)


class ConfigComponentModel(ModelNameStrTrainMixin, models.Model):
    TYPE_NUMBER = 'n'
    TYPE_STRING = 's'
    TYPE_BOOLEAN = 'b'
    TYPE_LIST = 'l'
    TYPE_DICT = 'd'

    name = models.CharField(max_length=254)
    type = models.CharField(
        max_length=1,
        choices=(
            (TYPE_NUMBER, TYPE_NUMBER),
            (TYPE_STRING, TYPE_STRING),
            (TYPE_BOOLEAN, TYPE_BOOLEAN),
            (TYPE_LIST, TYPE_LIST),
            (TYPE_DICT, TYPE_DICT),
        )
    )

    vue_component = models.CharField(max_length=254)

