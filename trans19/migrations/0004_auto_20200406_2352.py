# Generated by Django 3.0.2 on 2020-04-06 23:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans19', '0003_auto_20200404_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Case Number',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Date Case Confirmed',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Date of Birth',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Identity Document Number',
        ),
        migrations.RemoveField(
            model_name='travelhistory',
            name='Date From',
        ),
        migrations.RemoveField(
            model_name='travelhistory',
            name='Date To',
        ),
        migrations.RemoveField(
            model_name='travelhistory',
            name='Location Visited',
        ),
        migrations.RemoveField(
            model_name='travelhistory',
            name='X Coord',
        ),
        migrations.RemoveField(
            model_name='travelhistory',
            name='Y Coord',
        ),
        migrations.AddField(
            model_name='patient',
            name='DCC',
            field=models.DateField(default=datetime.date.today, verbose_name='Date Case Confirmed'),
        ),
        migrations.AddField(
            model_name='patient',
            name='DOB',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='patient',
            name='IDN',
            field=models.CharField(blank=True, help_text='Identity Document Number', max_length=10, null=True, verbose_name='Identity Document Number'),
        ),
        migrations.AddField(
            model_name='patient',
            name='caseNum',
            field=models.IntegerField(default=0, help_text='The case number of the Patient', primary_key=True, serialize=False, verbose_name='Case Number'),
        ),
        migrations.AddField(
            model_name='travelhistory',
            name='DateFrom',
            field=models.DateField(default=datetime.date.today, verbose_name='Date From'),
        ),
        migrations.AddField(
            model_name='travelhistory',
            name='DateTo',
            field=models.DateField(default=datetime.date.today, verbose_name='Date To'),
        ),
        migrations.AddField(
            model_name='travelhistory',
            name='Location_Visited',
            field=models.CharField(blank=True, help_text='Name of the Location', max_length=200, verbose_name='Location Visited'),
        ),
        migrations.AddField(
            model_name='travelhistory',
            name='XCoord',
            field=models.FloatField(default=0, help_text='X Coordiates/Longitude of the location', verbose_name='X Coord'),
        ),
        migrations.AddField(
            model_name='travelhistory',
            name='YCoord',
            field=models.FloatField(default=0, help_text='Y Coordiates/Latitude of the location', verbose_name='Y Coord'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Name',
            field=models.CharField(help_text='Name of the Patient', max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='travelhistory',
            name='Address',
            field=models.CharField(blank=True, help_text='Address of the Location', max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='travelhistory',
            name='District',
            field=models.CharField(help_text='District of the Location', max_length=200, verbose_name='District'),
        ),
    ]
