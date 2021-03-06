# Generated by Django 2.0.7 on 2018-08-12 10:33

from django.db import migrations


def replace_comma_to_semicolon(apps, schema_editor):
    Word = apps.get_model('words', 'Word')

    for post in Word.objects.all():
        post.translation = post.translation.replace(",", ";")
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0012_auto_20180812_1031'),
    ]

    operations = [
        migrations.RunPython(replace_comma_to_semicolon),
    ]
