from django.contrib import admin

# Register your models here.

from .models import ConfigStructSchemaGroupModel, ConfigStructSchemaItemModel, ConfigTypeModel


@admin.register(ConfigStructSchemaGroupModel)
class ConfigTemplateTableAdmin(admin.ModelAdmin):
    search_fields = (
        'switch__name',
    )
    list_display = (
        'name',
        'switch',
        'order',
        'have_sub_config'
    )


@admin.register(ConfigStructSchemaItemModel)
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
