from django.contrib import admin

# Register your models here.

from .models import (
    ConfigStructSchemaGroupModel,
    ConfigStructSchemaItemModel,
    ConfigTypeModel,
    ConfigStructSchemaNamespaceModel,
    ConfigComponentModel,
    ConfigValidatorModel,
)


@admin.register(ConfigComponentModel)
class ConfigComponentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


@admin.register(ConfigValidatorModel)
class ConfigValidatorAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )

@admin.register(ConfigStructSchemaNamespaceModel)
class ConfigStructSchemaNamespaceAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'path'
    )


@admin.register(ConfigStructSchemaGroupModel)
class ConfigStructSchemaGroupAdmin(admin.ModelAdmin):
    search_fields = (
        'item__name',
    )
    list_display = (
        'pk',
        'ns',
        'name',
        'item',
        'order',
        'have_sub_config'
    )


@admin.register(ConfigStructSchemaItemModel)
class ConfigStructSchemaItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'ns',
        'name',
        'display_name',
        'group',
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
