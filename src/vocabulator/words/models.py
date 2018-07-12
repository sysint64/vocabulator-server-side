from django.contrib import admin
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    translation = models.CharField(max_length=255, blank=True)
    pronounce = models.CharField(max_length=255, blank=True)
    need_clarify = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def has_translation(self):
        return self.translation.strip() != ""


class Definition(models.Model):
    class Meta:
        default_related_name = "definitions"

    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    example = models.TextField(blank=True)
    synonyms = models.CharField(max_length=1000, blank=True)
