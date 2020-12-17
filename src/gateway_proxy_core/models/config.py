from django.db import models


class ConfigModel(models.Model):
    config_type = models.ForeignKey("ConfigTypeModel", on_delete=models.CASCADE)
    user_config = models.JSONField()