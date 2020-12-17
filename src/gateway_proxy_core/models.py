from django.db import models

# Create your models here.


class ModelNameStrTrainMixin:
    def __str__(self):
        return f"<{self.__class__.__name__}({self.pk}):{self.name}>"

    def __repr__(self):
        return self.__str__()


class ConfigTypeModel(ModelNameStrTrainMixin, models.Model):
    name = models.CharField(max_length=254)
    tpl_table = models.ForeignKey("ConfigStructSchemaGroupModel", on_delete=models.SET_NULL, null=True)


class ConfigStructSchemaGroupModel(ModelNameStrTrainMixin, models.Model):
    ns = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    switch = models.ForeignKey("ConfigStructSchemaItemModel", null=True, blank=True, on_delete=models.SET_NULL)
    order = models.IntegerField(default=0)
    have_sub_config = models.BooleanField(default=True)

    class Meta:
        unique_together = (
            ('ns', 'name', 'switch'),
        )


class ConfigStructSchemaItemModel(ModelNameStrTrainMixin, models.Model):
    TYPE_INT = 'i'
    TYPE_FLOAT = 'f'
    TYPE_PERCENTAGE = 'p'
    TYPE_STR = 's'
    TYPE_REG = 'r'
    TYPE_IP = 'a'
    TYPE_BOOL = 'b'
    TYPE_EMAIL = 'e'
    TYPE_SWITCH = 'c'
    ns = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    order = models.IntegerField(default=0)
    table = models.ForeignKey("ConfigStructSchemaGroupModel", on_delete=models.CASCADE)
    display_name = models.CharField(max_length=254)
    required = models.BooleanField()
    type = models.CharField(max_length=1, choices=(
        (TYPE_INT, TYPE_INT),
        (TYPE_FLOAT, TYPE_FLOAT),
        (TYPE_PERCENTAGE, TYPE_PERCENTAGE),
        (TYPE_STR, TYPE_STR),
        (TYPE_BOOL, TYPE_BOOL),
        (TYPE_SWITCH, TYPE_SWITCH),
    ))
    default_value = models.CharField(max_length=254, null=True, blank=True)

    def get_default_value(self):
        if self.type == self.TYPE_INT:
            return int(self.default_value) if self.default_value else self.default_value
        elif self.type == self.TYPE_STR:
            return self.default_value
        elif self.type == self.TYPE_BOOL:
            return bool(self.default_value) if self.default_value else self.default_value
        elif self.type == self.TYPE_FLOAT:
            return float(self.default_value) if self.default_value else self.default_value
        else:
            return self.default_value

    @property
    def type_name(self):
        return dict(
            i='int',
            f='float',
            s='string',
            c='switch',
            b='bool',
        ).get(self.type, self.type)


class ConfigModel(models.Model):
    config_type = models.ForeignKey("ConfigTypeModel", on_delete=models.CASCADE)
    user_config = models.JSONField()
