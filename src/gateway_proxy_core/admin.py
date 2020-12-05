from django.contrib import admin

# Register your models here.

from .models import ConfigTemplateTableModel, ConfigTemplateValueModel, ConfigTypeModel


@admin.register(ConfigTemplateTableModel)
class ConfigTemplateTableAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(ConfigTemplateValueModel)
class ConfigTemplateValueAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'display_name',
        'table',
        'required',
        'type',
        'default_value',
    )


@admin.register(ConfigTypeModel)
class ConfigTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'tpl_table',
    )
