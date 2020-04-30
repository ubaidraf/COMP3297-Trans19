# Generated by Django 3.0.5 on 2020-04-30 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans19', '0010_auto_20200430_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='district',
            field=models.CharField(choices=[('Hong Kong Island', (('Central and Western', 'Central and Western'), ('Eastern', 'Eastern'), ('Southern', 'Southern'), ('Wan Chai', 'Wan Chai'))), ('Kowloon', (('Sham Shui Po', 'Sham Shui Po'), ('Kowloon City', 'Kowloon City'), ('Kwun Tong', 'Kwun Tong'), ('Wong Tai Sin', 'Wong Tai Sin'), ('Yau Tsim Mong', 'Yau Tsim Mong'))), ('New Teritories', (('Islands', 'Islands'), ('Kwai Tsing', 'Kwai Tsing'), ('North', 'North'), ('Sai Kung', 'Sai Kung'), ('Sha Tin', 'Sha Tin'), ('Tai Po', 'Tai Po'), ('Tsuen Wan', 'Tsuen Wan'), ('Tuen Mun', 'Tuen Mun'), ('Yuen Long', 'Yuen Long')))], default='Central and Western', help_text='District of the Location', max_length=200, verbose_name='District'),
        ),
    ]
