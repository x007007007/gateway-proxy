# Generated by Django 3.1.4 on 2020-12-17 14:31

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('gateway_proxy_core', '0009_configstructschemanamespace'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConfigStructSchemaNamespace',
            new_name='ConfigStructSchemaNamespaceModel',
        ),
    ]
