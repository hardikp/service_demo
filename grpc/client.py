import grpc

import time_pb2
import time_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = time_pb2_grpc.TimeStub(channel)
    response = stub.GetTime(time_pb2.TimeRequest())
    print('Client received: {}'.format(response.message))


if __name__ == '__main__':
    run()
