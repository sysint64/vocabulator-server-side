from vocabulator.grpc_api.generated.sync_pb2 import SyncGrpcResponse
from vocabulator.grpc_api.generated.sync_pb2_grpc import SyncServicer
from vocabulator.grpc_api.serializers import *
from vocabulator.words.models import Category, Word


class Sync(SyncServicer):
    def Sync(self, request, context):
        return SyncGrpcResponse(
            categories=grpc_repeated(grpc_category, Category.objects.all()),
            words=grpc_repeated(grpc_word, Word.objects.all())
        )
