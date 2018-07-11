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
    definition = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @property
    def has_translation(self):
        return self.translation.strip() != ""
