# Generated by Django 2.1.5 on 2019-03-12 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webap', '0006_auto_20190312_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='currentRequst',
            new_name='currentRequest',
        ),
    ]