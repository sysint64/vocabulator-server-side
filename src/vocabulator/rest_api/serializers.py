from rest_framework import serializers

from vocabulator.words.models import Category, Word


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "id", "name",


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "id", "category", "name", "translation", "pronounce", "definition",
