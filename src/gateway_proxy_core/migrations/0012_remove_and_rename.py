# Generated by Django 3.1.4 on 2020-12-17 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gateway_proxy_core', '0011_new_ns'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configstructschemaitemmodel',
            old_name='table',
            new_name='group',
        ),
        migrations.RemoveField(
            model_name='configstructschemaitemmodel',
            name='ns_old',
        ),
        migrations.AlterUniqueTogether(
            name='configstructschemagroupmodel',
            unique_together={('ns', 'name', 'switch')},
        ),
        migrations.RemoveField(
            model_name='configstructschemagroupmodel',
            name='ns_old',
        ),
        migrations.RenameField(
            model_name='configstructschemagroupmodel',
            old_name='switch',
            new_name='item',
        ),
        migrations.AlterUniqueTogether(
            name='configstructschemagroupmodel',
            unique_together={('ns', 'name', 'item')},
        ),
        migrations.AlterUniqueTogether(
            name='configstructschemaitemmodel',
            unique_together={('ns', 'name', 'group')},
        ),
    ]