# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/user_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'proto/user_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proto/user_service.proto\"B\n\x11\x43reateUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"I\n\x12\x43reateUserResponse\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12\x0e\n\x06userId\x18\x02 \x01(\x05\x12\x10\n\x08\x65rrorMsg\x18\x03 \x01(\t\".\n\x0b\x41uthRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"^\n\x0c\x41uthResponse\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12\x10\n\x08\x65rrorMsg\x18\x02 \x01(\t\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x03 \x01(\t\x12\x14\n\x0crefreshToken\x18\x04 \x01(\t2s\n\x0bUserService\x12-\n\x0e\x41uthentication\x12\x0c.AuthRequest\x1a\r.AuthResponse\x12\x35\n\nCreateUser\x12\x12.CreateUserRequest\x1a\x13.CreateUserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.user_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CREATEUSERREQUEST']._serialized_start=28
  _globals['_CREATEUSERREQUEST']._serialized_end=94
  _globals['_CREATEUSERRESPONSE']._serialized_start=96
  _globals['_CREATEUSERRESPONSE']._serialized_end=169
  _globals['_AUTHREQUEST']._serialized_start=171
  _globals['_AUTHREQUEST']._serialized_end=217
  _globals['_AUTHRESPONSE']._serialized_start=219
  _globals['_AUTHRESPONSE']._serialized_end=313
  _globals['_USERSERVICE']._serialized_start=315
  _globals['_USERSERVICE']._serialized_end=430
# @@protoc_insertion_point(module_scope)
