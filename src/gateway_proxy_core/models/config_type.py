from django.db import models

from gateway_proxy_core.models._mixin import ModelNameStrTrainMixin


class ConfigTypeModel(ModelNameStrTrainMixin, models.Model):
    name = models.CharField(max_length=254)
    tpl_table = models.ForeignKey("ConfigStructSchemaGroupModel", on_delete=models.SET_NULL, null=True)