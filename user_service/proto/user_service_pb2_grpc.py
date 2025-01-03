# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from proto import user_service_pb2 as proto_dot_user__service__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
  from grpc._utilities import first_version_is_lower
  _version_not_supported = first_version_is_lower(
      GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
  _version_not_supported = True

if _version_not_supported:
  raise RuntimeError(
      f'The grpc package installed is at version {GRPC_VERSION},'
      + f' but the generated code in proto/user_service_pb2_grpc.py depends on'
      + f' grpcio>={GRPC_GENERATED_VERSION}.'
      + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
      +
        f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
  )


class UserServiceStub(object):
  """Missing associated documentation comment in .proto file."""

  def __init__(self, channel):
    """Constructor.

    Args:
        channel: A grpc.Channel.
    """
    self.Authentication = channel.unary_unary(
        '/UserService/Authentication',
        request_serializer=proto_dot_user__service__pb2.AuthRequest.SerializeToString,
        response_deserializer=proto_dot_user__service__pb2.AuthResponse.FromString,
        _registered_method=True)
    self.CreateUser = channel.unary_unary(
        '/UserService/CreateUser',
        request_serializer=proto_dot_user__service__pb2.CreateUserRequest.SerializeToString,
        response_deserializer=proto_dot_user__service__pb2.CreateUserResponse.FromString,
        _registered_method=True)
    self.GetUserById = channel.unary_unary(
        '/UserService/GetUserById',
        request_serializer=proto_dot_user__service__pb2.GetUserByIdRequest.SerializeToString,
        response_deserializer=proto_dot_user__service__pb2.GetUserByIdResponse.FromString,
        _registered_method=True)


class UserServiceServicer(object):
  """Missing associated documentation comment in .proto file."""

  def Authentication(self, request, context):
    """Missing associated documentation comment in .proto file."""
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateUser(self, request, context):
    """Missing associated documentation comment in .proto file."""
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUserById(self, request, context):
    """Missing associated documentation comment in .proto file."""
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Authentication': grpc.unary_unary_rpc_method_handler(
          servicer.Authentication,
          request_deserializer=proto_dot_user__service__pb2.AuthRequest.FromString,
          response_serializer=proto_dot_user__service__pb2.AuthResponse.SerializeToString,
      ),
      'CreateUser': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUser,
          request_deserializer=proto_dot_user__service__pb2.CreateUserRequest.FromString,
          response_serializer=proto_dot_user__service__pb2.CreateUserResponse.SerializeToString,
      ),
      'GetUserById': grpc.unary_unary_rpc_method_handler(
          servicer.GetUserById,
          request_deserializer=proto_dot_user__service__pb2.GetUserByIdRequest.FromString,
          response_serializer=proto_dot_user__service__pb2.GetUserByIdResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'UserService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
  server.add_registered_method_handlers('UserService', rpc_method_handlers)

 # This class is part of an EXPERIMENTAL API.


class UserService(object):
  """Missing associated documentation comment in .proto file."""

  @staticmethod
  def Authentication(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
    return grpc.experimental.unary_unary(
        request,
        target,
        '/UserService/Authentication',
        proto_dot_user__service__pb2.AuthRequest.SerializeToString,
        proto_dot_user__service__pb2.AuthResponse.FromString,
        options,
        channel_credentials,
        insecure,
        call_credentials,
        compression,
        wait_for_ready,
        timeout,
        metadata,
        _registered_method=True)

  @staticmethod
  def CreateUser(request,
                 target,
                 options=(),
                 channel_credentials=None,
                 call_credentials=None,
                 insecure=False,
                 compression=None,
                 wait_for_ready=None,
                 timeout=None,
                 metadata=None):
    return grpc.experimental.unary_unary(
        request,
        target,
        '/UserService/CreateUser',
        proto_dot_user__service__pb2.CreateUserRequest.SerializeToString,
        proto_dot_user__service__pb2.CreateUserResponse.FromString,
        options,
        channel_credentials,
        insecure,
        call_credentials,
        compression,
        wait_for_ready,
        timeout,
        metadata,
        _registered_method=True)

  @staticmethod
  def GetUserById(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
    return grpc.experimental.unary_unary(
        request,
        target,
        '/UserService/GetUserById',
        proto_dot_user__service__pb2.GetUserByIdRequest.SerializeToString,
        proto_dot_user__service__pb2.GetUserByIdResponse.FromString,
        options,
        channel_credentials,
        insecure,
        call_credentials,
        compression,
        wait_for_ready,
        timeout,
        metadata,
        _registered_method=True)
