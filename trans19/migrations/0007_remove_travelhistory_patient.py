# Generated by Django 3.0.2 on 2020-04-28 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans19', '0006_auto_20200407_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelhistory',
            name='Patient',
        ),
    ]
