from rest_framework import serializers

from vocabulator.words.models import Category, Word, Definition


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "id", "name",


class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = "title", "desc", "example", "synonyms"


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "id", "category", "name", "translation", "pronounce", "definitions",

    definitions = DefinitionSerializer(many=True, read_only=True)
