# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: anyvalue.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'anyvalue.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61nyvalue.proto\x12\x0bopamp.proto\"\xe8\x01\n\x08\x41nyValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x02 \x01(\x08H\x00\x12\x13\n\tint_value\x18\x03 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x04 \x01(\x01H\x00\x12.\n\x0b\x61rray_value\x18\x05 \x01(\x0b\x32\x17.opamp.proto.ArrayValueH\x00\x12\x31\n\x0ckvlist_value\x18\x06 \x01(\x0b\x32\x19.opamp.proto.KeyValueListH\x00\x12\x15\n\x0b\x62ytes_value\x18\x07 \x01(\x0cH\x00\x42\x07\n\x05value\"3\n\nArrayValue\x12%\n\x06values\x18\x01 \x03(\x0b\x32\x15.opamp.proto.AnyValue\"5\n\x0cKeyValueList\x12%\n\x06values\x18\x01 \x03(\x0b\x32\x15.opamp.proto.KeyValue\"=\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.opamp.proto.AnyValueB.Z,github.com/open-telemetry/opamp-go/protobufsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'anyvalue_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z,github.com/open-telemetry/opamp-go/protobufs'
  _globals['_ANYVALUE']._serialized_start=32
  _globals['_ANYVALUE']._serialized_end=264
  _globals['_ARRAYVALUE']._serialized_start=266
  _globals['_ARRAYVALUE']._serialized_end=317
  _globals['_KEYVALUELIST']._serialized_start=319
  _globals['_KEYVALUELIST']._serialized_end=372
  _globals['_KEYVALUE']._serialized_start=374
  _globals['_KEYVALUE']._serialized_end=435
# @@protoc_insertion_point(module_scope)
