from django.contrib import admin
from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    translation = models.CharField(max_length=255, blank=True)
    pronounce = models.CharField(max_length=255, blank=True)
    need_clarify = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    association_image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    @property
    def has_translation(self):
        return self.translation.strip() != ""


class Example(models.Model):
    class Meta:
        default_related_name = "examples"

    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    content = models.TextField()
    translate = models.TextField(blank=True)


class Definition(models.Model):
    class Meta:
        default_related_name = "definitions"

    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    example = models.TextField(blank=True)
    translate = models.TextField(blank=True)
    synonyms = models.CharField(max_length=1000, blank=True)


class Kanji(models.Model):
    class Meta:
        default_related_name = "kanji"

    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    hieroglyph = models.CharField(max_length=255)
    reading = models.CharField(max_length=255)
    meaning = models.CharField(max_length=255)
