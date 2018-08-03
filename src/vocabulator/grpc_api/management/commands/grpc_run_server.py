from contextlib import contextmanager

from concurrent import futures
import grpc
import time

from django.core.management.base import BaseCommand

from vocabulator.grpc import helloworld_pb2, helloworld_pb2_grpc
from vocabulator.words.models import Word


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, %s!' % Word.objects.all().first().name)


@contextmanager
def serve_forever():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    yield
    server.stop(0)


class Command(BaseCommand):
    help = 'Run th gRPC server'

    def handle(self, *args, **options):
        with serve_forever():
            self.stdout.write(self.style.SUCCESS('Successfully started grpc server '))
            try:
                while True:
                    time.sleep(_ONE_DAY_IN_SECONDS)
            except KeyboardInterrupt:
                pass
