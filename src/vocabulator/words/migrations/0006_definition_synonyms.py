# Generated by Django 2.0.7 on 2018-07-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_auto_20180711_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='definition',
            name='synonyms',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]