from contextlib import contextmanager

from concurrent import futures
import grpc
import time

from django.conf import settings
from django.core.management.base import BaseCommand


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


@contextmanager
def serve_forever():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    for service in settings.GRPC_SERVICES:
        service_init = __import__(service + ".routes", fromlist=[""])
        service_init.add_services(server)

    # TODO: rm hardcode
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
