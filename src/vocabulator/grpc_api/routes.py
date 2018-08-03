from vocabulator.grpc_api.generated.sync_pb2_grpc import add_SyncServicer_to_server
from vocabulator.grpc_api.views import Sync


def add_services(server):
    add_SyncServicer_to_server(Sync(), server)
