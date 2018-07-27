import time
from concurrent import futures

import grpc

import time_pb2
import time_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Timer(time_pb2_grpc.TimeServicer):
    def GetTime(self, request, context):
        return time_pb2.TimeReply(message=time.ctime())


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    time_pb2_grpc.add_TimeServicer_to_server(Timer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
