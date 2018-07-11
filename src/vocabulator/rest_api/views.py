from rest_framework.decorators import api_view
from rest_framework.response import Response

from vocabulator.rest_api.serializers import CategorySerializer, WordSerializer
from vocabulator.words.models import Category, Word


@api_view(["GET"])
def sync(request):
    return Response(
        {
            "categories": CategorySerializer(Category.objects.all(), many=True).data,
            "words": WordSerializer(Word.objects.all(), many=True).data
        }
    )
