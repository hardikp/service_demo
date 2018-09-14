# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import market_data_pb2 as market__data__pb2


class MarketDataStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetOHLC = channel.unary_unary(
        '/market_data.MarketData/GetOHLC',
        request_serializer=market__data__pb2.OHLCRequest.SerializeToString,
        response_deserializer=market__data__pb2.OHLCReply.FromString,
        )


class MarketDataServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetOHLC(self, request, context):
    """Get the [Open, High, Low, Close] for the given list of stocks
    and start/end dates
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MarketDataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetOHLC': grpc.unary_unary_rpc_method_handler(
          servicer.GetOHLC,
          request_deserializer=market__data__pb2.OHLCRequest.FromString,
          response_serializer=market__data__pb2.OHLCReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'market_data.MarketData', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
