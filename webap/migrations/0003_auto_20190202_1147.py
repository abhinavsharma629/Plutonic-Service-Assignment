# Generated by Django 2.1.5 on 2019-02-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webap', '0002_auto_20190121_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='id_no',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='employee',
            name='occupation',
            field=models.CharField(default='SDE', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
