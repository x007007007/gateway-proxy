from django.db import models

from gateway_proxy_core.models._mixin import ModelNameStrTrainMixin


class ConfigTypeModel(ModelNameStrTrainMixin, models.Model):
    name = models.CharField(max_length=254)
    data_type = models.ForeignKey("ConfigStructSchemaDataTypeModel", null=True, blank=True, on_delete=models.SET_NULL)
    tpl_table = models.ForeignKey("ConfigStructSchemaGroupModel", on_delete=models.SET_NULL, null=True)