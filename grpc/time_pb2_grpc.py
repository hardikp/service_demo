# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import time_pb2 as time__pb2


class TimeStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetTime = channel.unary_unary(
        '/time.Time/GetTime',
        request_serializer=time__pb2.TimeRequest.SerializeToString,
        response_deserializer=time__pb2.TimeReply.FromString,
        )


class TimeServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetTime(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TimeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetTime': grpc.unary_unary_rpc_method_handler(
          servicer.GetTime,
          request_deserializer=time__pb2.TimeRequest.FromString,
          response_serializer=time__pb2.TimeReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'time.Time', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
