# Generated by Django 2.0.7 on 2018-07-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='pronounce',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='word',
            name='translate',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
