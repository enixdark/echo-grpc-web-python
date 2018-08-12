# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import echo_pb2 as echo__pb2


class EchoServiceStub(object):
  """A simple echo service.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Echo = channel.unary_unary(
        '/grpc.gateway.testing.EchoService/Echo',
        request_serializer=echo__pb2.EchoRequest.SerializeToString,
        response_deserializer=echo__pb2.EchoResponse.FromString,
        )
    self.EchoAbort = channel.unary_unary(
        '/grpc.gateway.testing.EchoService/EchoAbort',
        request_serializer=echo__pb2.EchoRequest.SerializeToString,
        response_deserializer=echo__pb2.EchoResponse.FromString,
        )
    self.NoOp = channel.unary_unary(
        '/grpc.gateway.testing.EchoService/NoOp',
        request_serializer=echo__pb2.Empty.SerializeToString,
        response_deserializer=echo__pb2.Empty.FromString,
        )
    self.ServerStreamingEcho = channel.unary_stream(
        '/grpc.gateway.testing.EchoService/ServerStreamingEcho',
        request_serializer=echo__pb2.ServerStreamingEchoRequest.SerializeToString,
        response_deserializer=echo__pb2.ServerStreamingEchoResponse.FromString,
        )
    self.ServerStreamingEchoAbort = channel.unary_stream(
        '/grpc.gateway.testing.EchoService/ServerStreamingEchoAbort',
        request_serializer=echo__pb2.ServerStreamingEchoRequest.SerializeToString,
        response_deserializer=echo__pb2.ServerStreamingEchoResponse.FromString,
        )
    self.ClientStreamingEcho = channel.stream_unary(
        '/grpc.gateway.testing.EchoService/ClientStreamingEcho',
        request_serializer=echo__pb2.ClientStreamingEchoRequest.SerializeToString,
        response_deserializer=echo__pb2.ClientStreamingEchoResponse.FromString,
        )
    self.FullDuplexEcho = channel.stream_stream(
        '/grpc.gateway.testing.EchoService/FullDuplexEcho',
        request_serializer=echo__pb2.EchoRequest.SerializeToString,
        response_deserializer=echo__pb2.EchoResponse.FromString,
        )
    self.HalfDuplexEcho = channel.stream_stream(
        '/grpc.gateway.testing.EchoService/HalfDuplexEcho',
        request_serializer=echo__pb2.EchoRequest.SerializeToString,
        response_deserializer=echo__pb2.EchoResponse.FromString,
        )


class EchoServiceServicer(object):
  """A simple echo service.
  """

  def Echo(self, request, context):
    """One request followed by one response
    The server returns the client message as-is.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EchoAbort(self, request, context):
    """Sends back abort status.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NoOp(self, request, context):
    """One empty request, ZERO processing, followed by one empty response
    (minimum effort to do message serialization).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ServerStreamingEcho(self, request, context):
    """One request followed by a sequence of responses (streamed download).
    The server will return the same client message repeatedly.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ServerStreamingEchoAbort(self, request, context):
    """One request followed by a sequence of responses (streamed download).
    The server abort directly.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClientStreamingEcho(self, request_iterator, context):
    """A sequence of requests followed by one response (streamed upload).
    The server returns the total number of messages as the result.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FullDuplexEcho(self, request_iterator, context):
    """A sequence of requests with each message echoed by the server immediately.
    The server returns the same client messages in order.
    E.g. this is how the speech API works.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HalfDuplexEcho(self, request_iterator, context):
    """A sequence of requests followed by a sequence of responses.
    The server buffers all the client messages and then returns the same
    client messages one by one after the client half-closes the stream.
    This is how an image recognition API may work.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EchoServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Echo': grpc.unary_unary_rpc_method_handler(
          servicer.Echo,
          request_deserializer=echo__pb2.EchoRequest.FromString,
          response_serializer=echo__pb2.EchoResponse.SerializeToString,
      ),
      'EchoAbort': grpc.unary_unary_rpc_method_handler(
          servicer.EchoAbort,
          request_deserializer=echo__pb2.EchoRequest.FromString,
          response_serializer=echo__pb2.EchoResponse.SerializeToString,
      ),
      'NoOp': grpc.unary_unary_rpc_method_handler(
          servicer.NoOp,
          request_deserializer=echo__pb2.Empty.FromString,
          response_serializer=echo__pb2.Empty.SerializeToString,
      ),
      'ServerStreamingEcho': grpc.unary_stream_rpc_method_handler(
          servicer.ServerStreamingEcho,
          request_deserializer=echo__pb2.ServerStreamingEchoRequest.FromString,
          response_serializer=echo__pb2.ServerStreamingEchoResponse.SerializeToString,
      ),
      'ServerStreamingEchoAbort': grpc.unary_stream_rpc_method_handler(
          servicer.ServerStreamingEchoAbort,
          request_deserializer=echo__pb2.ServerStreamingEchoRequest.FromString,
          response_serializer=echo__pb2.ServerStreamingEchoResponse.SerializeToString,
      ),
      'ClientStreamingEcho': grpc.stream_unary_rpc_method_handler(
          servicer.ClientStreamingEcho,
          request_deserializer=echo__pb2.ClientStreamingEchoRequest.FromString,
          response_serializer=echo__pb2.ClientStreamingEchoResponse.SerializeToString,
      ),
      'FullDuplexEcho': grpc.stream_stream_rpc_method_handler(
          servicer.FullDuplexEcho,
          request_deserializer=echo__pb2.EchoRequest.FromString,
          response_serializer=echo__pb2.EchoResponse.SerializeToString,
      ),
      'HalfDuplexEcho': grpc.stream_stream_rpc_method_handler(
          servicer.HalfDuplexEcho,
          request_deserializer=echo__pb2.EchoRequest.FromString,
          response_serializer=echo__pb2.EchoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.gateway.testing.EchoService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))