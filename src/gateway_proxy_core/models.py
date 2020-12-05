from django.db import models

# Create your models here.


class ConfigTypeModel(models.Model):
    name = models.CharField(max_length=254)
    tpl_table = models.ForeignKey("ConfigTemplateTableModel", on_delete=models.SET_NULL, null=True)


class ConfigTemplateTableModel(models.Model):
    name = models.CharField(max_length=254)
    switch = models.ForeignKey("ConfigTemplateValueModel", null=True, blank=True, on_delete=models.SET_NULL)
    order = models.IntegerField(default=0)
    have_sub_config = models.BooleanField(default=True)


class ConfigTemplateValueModel(models.Model):
    TYPE_INT = 'i'
    TYPE_FLOAT = 'f'
    TYPE_PERCENTAGE = 'p'
    TYPE_STR = 's'
    TYPE_REG = 'r'
    TYPE_IP = 'a'
    TYPE_BOOL = 'b'
    TYPE_EMAIL = 'e'
    TYPE_SWITCH = 'c'
    name = models.CharField(max_length=254)
    order = models.IntegerField(default=0)
    table = models.ForeignKey("ConfigTemplateTableModel", on_delete=models.CASCADE)
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
            bool='bool',
        ).get(self.type, self.type)

class ConfigModel(models.Model):
    config_type = models.ForeignKey("ConfigTypeModel", on_delete=models.CASCADE)
    user_config = models.JSONField()
