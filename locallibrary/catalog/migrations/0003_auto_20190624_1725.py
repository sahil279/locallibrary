# Generated by Django 2.2.2 on 2019-06-24 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190624_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='NAME',
            new_name='name',
        ),
    ]
