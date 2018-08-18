from django.db import transaction

from vocabulator.grpc_api.generated.sync_pb2 import SyncGrpcResponse
from vocabulator.grpc_api.generated.sync_pb2_grpc import SyncServicer
from vocabulator.grpc_api.serializers import *
from vocabulator.words.models import Category, Word, Language


class Sync(SyncServicer):
    def Sync(self, request, context):
        with transaction.atomic():
            for word_request in request.words:
                word = Word.objects.filter(id=word_request.id).first()

                if word is not None:
                    word.score = min(max(word.score + word_request.scoreDelta, 1), 100)
                    word.save()

            for new_word_request in request.newWords:
                Word.objects.create(name=new_word_request.name, translation=new_word_request.translation)

            return SyncGrpcResponse(
                languages=grpc_repeated(grpc_language, Language.objects.all()),
                categories=grpc_repeated(grpc_category, Category.objects.all()),
                words=grpc_repeated(grpc_word, Word.objects.exclude(translation="").exclude(need_clarify=True))
            )
