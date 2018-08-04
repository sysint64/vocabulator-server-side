from django.db import transaction

from vocabulator.grpc_api.generated.sync_pb2 import SyncGrpcResponse
from vocabulator.grpc_api.generated.sync_pb2_grpc import SyncServicer
from vocabulator.grpc_api.serializers import *
from vocabulator.words.models import Category, Word


class Sync(SyncServicer):
    def Sync(self, request, context):
        with transaction.atomic():
            for word_request in request.words:
                word = Word.objects.get(id=word_request.id)
                word.score = min(max(word.score + word_request.scoreDelta, 1), 100)
                word.save()

        return SyncGrpcResponse(
            categories=grpc_repeated(grpc_category, Category.objects.all()),
            words=grpc_repeated(grpc_word, Word.objects.all())
        )
