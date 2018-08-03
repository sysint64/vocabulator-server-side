from __future__ import print_function

import grpc

from vocabulator.grpc_api.generated import sync_pb2, sync_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = sync_pb2_grpc.SyncStub(channel)
        response = stub.Sync(sync_pb2.SyncGrpcRequest())
    print("Greeter client received: " + str(response))


if __name__ == '__main__':
    run()
