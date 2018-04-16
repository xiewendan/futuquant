# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Qot_ReqSubInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Qot_Common_pb2 as Qot__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Qot_ReqSubInfo.proto',
  package='Qot_ReqSubInfo',
  syntax='proto2',
  serialized_pb=_b('\n\x14Qot_ReqSubInfo.proto\x12\x0eQot_ReqSubInfo\x1a\x10Qot_Common.proto\"\x1b\n\x03\x43\x32S\x12\x14\n\x0cisReqAllConn\x18\x01 \x01(\x08\"<\n\x07SubInfo\x12\x0f\n\x07subType\x18\x01 \x02(\x05\x12 \n\x05stock\x18\x02 \x03(\x0b\x32\x11.Qot_Common.Stock\"a\n\x0b\x43onnSubInfo\x12(\n\x07subInfo\x18\x01 \x03(\x0b\x32\x17.Qot_ReqSubInfo.SubInfo\x12\x11\n\tusedQuota\x18\x02 \x02(\x05\x12\x15\n\risOwnConnData\x18\x03 \x02(\x08\"d\n\x03S2C\x12\x30\n\x0b\x63onnSubInfo\x18\x01 \x03(\x0b\x32\x1b.Qot_ReqSubInfo.ConnSubInfo\x12\x16\n\x0etotalUsedQuota\x18\x02 \x02(\x05\x12\x13\n\x0bremainQuota\x18\x03 \x02(\x05\"+\n\x07Request\x12 \n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x13.Qot_ReqSubInfo.C2S\"^\n\x08Response\x12\x0f\n\x07retType\x18\x01 \x02(\x05\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12 \n\x03s2c\x18\x04 \x01(\x0b\x32\x13.Qot_ReqSubInfo.S2C')
  ,
  dependencies=[Qot__Common__pb2.DESCRIPTOR,])




_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Qot_ReqSubInfo.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isReqAllConn', full_name='Qot_ReqSubInfo.C2S.isReqAllConn', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=85,
)


_SUBINFO = _descriptor.Descriptor(
  name='SubInfo',
  full_name='Qot_ReqSubInfo.SubInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subType', full_name='Qot_ReqSubInfo.SubInfo.subType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stock', full_name='Qot_ReqSubInfo.SubInfo.stock', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=147,
)


_CONNSUBINFO = _descriptor.Descriptor(
  name='ConnSubInfo',
  full_name='Qot_ReqSubInfo.ConnSubInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subInfo', full_name='Qot_ReqSubInfo.ConnSubInfo.subInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usedQuota', full_name='Qot_ReqSubInfo.ConnSubInfo.usedQuota', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isOwnConnData', full_name='Qot_ReqSubInfo.ConnSubInfo.isOwnConnData', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=246,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Qot_ReqSubInfo.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connSubInfo', full_name='Qot_ReqSubInfo.S2C.connSubInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalUsedQuota', full_name='Qot_ReqSubInfo.S2C.totalUsedQuota', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remainQuota', full_name='Qot_ReqSubInfo.S2C.remainQuota', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=348,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Qot_ReqSubInfo.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Qot_ReqSubInfo.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=393,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Qot_ReqSubInfo.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Qot_ReqSubInfo.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Qot_ReqSubInfo.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Qot_ReqSubInfo.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Qot_ReqSubInfo.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=489,
)

_SUBINFO.fields_by_name['stock'].message_type = Qot__Common__pb2._STOCK
_CONNSUBINFO.fields_by_name['subInfo'].message_type = _SUBINFO
_S2C.fields_by_name['connSubInfo'].message_type = _CONNSUBINFO
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['SubInfo'] = _SUBINFO
DESCRIPTOR.message_types_by_name['ConnSubInfo'] = _CONNSUBINFO
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Qot_ReqSubInfo_pb2'
  # @@protoc_insertion_point(class_scope:Qot_ReqSubInfo.C2S)
  ))
_sym_db.RegisterMessage(C2S)

SubInfo = _reflection.GeneratedProtocolMessageType('SubInfo', (_message.Message,), dict(
  DESCRIPTOR = _SUBINFO,
  __module__ = 'Qot_ReqSubInfo_pb2'
  # @@protoc_insertion_point(class_scope:Qot_ReqSubInfo.SubInfo)
  ))
_sym_db.RegisterMessage(SubInfo)

ConnSubInfo = _reflection.GeneratedProtocolMessageType('ConnSubInfo', (_message.Message,), dict(
  DESCRIPTOR = _CONNSUBINFO,
  __module__ = 'Qot_ReqSubInfo_pb2'
  # @@protoc_insertion_point(class_scope:Qot_ReqSubInfo.ConnSubInfo)
  ))
_sym_db.RegisterMessage(ConnSubInfo)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Qot_ReqSubInfo_pb2'
  # @@protoc_insertion_point(class_scope:Qot_ReqSubInfo.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Qot_ReqSubInfo_pb2'
  # @@protoc_insertion_point(class_scope:Qot_ReqSubInfo.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Qot_ReqSubInfo_pb2'
  # @@protoc_insertion_point(class_scope:Qot_ReqSubInfo.Response)
  ))
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
