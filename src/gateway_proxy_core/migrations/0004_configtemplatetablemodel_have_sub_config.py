# Generated by Django 3.1.4 on 2020-12-05 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway_proxy_core', '0003_configtemplatetablemodel_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='configtemplatetablemodel',
            name='have_sub_config',
            field=models.BooleanField(default=True),
        ),
    ]
