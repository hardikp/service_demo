# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: market_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='market_data.proto',
  package='market_data',
  syntax='proto3',
  serialized_pb=_b('\n\x11market_data.proto\x12\x0bmarket_data\"C\n\x0bOHLCRequest\x12\x0e\n\x06ticker\x18\x03 \x03(\t\x12\x12\n\nstart_date\x18\x01 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x02 \x01(\t\"\xa8\x04\n\tOHLCReply\x12\r\n\x05\x64\x61tes\x18\x01 \x03(\t\x12.\n\x04open\x18\x02 \x03(\x0b\x32 .market_data.OHLCReply.OpenEntry\x12.\n\x04high\x18\x03 \x03(\x0b\x32 .market_data.OHLCReply.HighEntry\x12,\n\x03low\x18\x04 \x03(\x0b\x32\x1f.market_data.OHLCReply.LowEntry\x12\x30\n\x05\x63lose\x18\x05 \x03(\x0b\x32!.market_data.OHLCReply.CloseEntry\x1a\x18\n\x07OHLCRet\x12\r\n\x05price\x18\x01 \x03(\x01\x1aK\n\tOpenEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.market_data.OHLCReply.OHLCRet:\x02\x38\x01\x1aK\n\tHighEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.market_data.OHLCReply.OHLCRet:\x02\x38\x01\x1aJ\n\x08LowEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.market_data.OHLCReply.OHLCRet:\x02\x38\x01\x1aL\n\nCloseEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.market_data.OHLCReply.OHLCRet:\x02\x38\x01\x32I\n\nMarketData\x12;\n\x07GetOHLC\x12\x18.market_data.OHLCRequest\x1a\x16.market_data.OHLCReplyb\x06proto3')
)




_OHLCREQUEST = _descriptor.Descriptor(
  name='OHLCRequest',
  full_name='market_data.OHLCRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ticker', full_name='market_data.OHLCRequest.ticker', index=0,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='market_data.OHLCRequest.start_date', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='market_data.OHLCRequest.end_date', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=101,
)


_OHLCREPLY_OHLCRET = _descriptor.Descriptor(
  name='OHLCRet',
  full_name='market_data.OHLCReply.OHLCRet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='market_data.OHLCReply.OHLCRet.price', index=0,
      number=1, type=1, cpp_type=5, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=348,
)

_OHLCREPLY_OPENENTRY = _descriptor.Descriptor(
  name='OpenEntry',
  full_name='market_data.OHLCReply.OpenEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='market_data.OHLCReply.OpenEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='market_data.OHLCReply.OpenEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=425,
)

_OHLCREPLY_HIGHENTRY = _descriptor.Descriptor(
  name='HighEntry',
  full_name='market_data.OHLCReply.HighEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='market_data.OHLCReply.HighEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='market_data.OHLCReply.HighEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=427,
  serialized_end=502,
)

_OHLCREPLY_LOWENTRY = _descriptor.Descriptor(
  name='LowEntry',
  full_name='market_data.OHLCReply.LowEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='market_data.OHLCReply.LowEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='market_data.OHLCReply.LowEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=504,
  serialized_end=578,
)

_OHLCREPLY_CLOSEENTRY = _descriptor.Descriptor(
  name='CloseEntry',
  full_name='market_data.OHLCReply.CloseEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='market_data.OHLCReply.CloseEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='market_data.OHLCReply.CloseEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=580,
  serialized_end=656,
)

_OHLCREPLY = _descriptor.Descriptor(
  name='OHLCReply',
  full_name='market_data.OHLCReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dates', full_name='market_data.OHLCReply.dates', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open', full_name='market_data.OHLCReply.open', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='market_data.OHLCReply.high', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low', full_name='market_data.OHLCReply.low', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close', full_name='market_data.OHLCReply.close', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OHLCREPLY_OHLCRET, _OHLCREPLY_OPENENTRY, _OHLCREPLY_HIGHENTRY, _OHLCREPLY_LOWENTRY, _OHLCREPLY_CLOSEENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=656,
)

_OHLCREPLY_OHLCRET.containing_type = _OHLCREPLY
_OHLCREPLY_OPENENTRY.fields_by_name['value'].message_type = _OHLCREPLY_OHLCRET
_OHLCREPLY_OPENENTRY.containing_type = _OHLCREPLY
_OHLCREPLY_HIGHENTRY.fields_by_name['value'].message_type = _OHLCREPLY_OHLCRET
_OHLCREPLY_HIGHENTRY.containing_type = _OHLCREPLY
_OHLCREPLY_LOWENTRY.fields_by_name['value'].message_type = _OHLCREPLY_OHLCRET
_OHLCREPLY_LOWENTRY.containing_type = _OHLCREPLY
_OHLCREPLY_CLOSEENTRY.fields_by_name['value'].message_type = _OHLCREPLY_OHLCRET
_OHLCREPLY_CLOSEENTRY.containing_type = _OHLCREPLY
_OHLCREPLY.fields_by_name['open'].message_type = _OHLCREPLY_OPENENTRY
_OHLCREPLY.fields_by_name['high'].message_type = _OHLCREPLY_HIGHENTRY
_OHLCREPLY.fields_by_name['low'].message_type = _OHLCREPLY_LOWENTRY
_OHLCREPLY.fields_by_name['close'].message_type = _OHLCREPLY_CLOSEENTRY
DESCRIPTOR.message_types_by_name['OHLCRequest'] = _OHLCREQUEST
DESCRIPTOR.message_types_by_name['OHLCReply'] = _OHLCREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OHLCRequest = _reflection.GeneratedProtocolMessageType('OHLCRequest', (_message.Message,), dict(
  DESCRIPTOR = _OHLCREQUEST,
  __module__ = 'market_data_pb2'
  # @@protoc_insertion_point(class_scope:market_data.OHLCRequest)
  ))
_sym_db.RegisterMessage(OHLCRequest)

OHLCReply = _reflection.GeneratedProtocolMessageType('OHLCReply', (_message.Message,), dict(

  OHLCRet = _reflection.GeneratedProtocolMessageType('OHLCRet', (_message.Message,), dict(
    DESCRIPTOR = _OHLCREPLY_OHLCRET,
    __module__ = 'market_data_pb2'
    # @@protoc_insertion_point(class_scope:market_data.OHLCReply.OHLCRet)
    ))
  ,

  OpenEntry = _reflection.GeneratedProtocolMessageType('OpenEntry', (_message.Message,), dict(
    DESCRIPTOR = _OHLCREPLY_OPENENTRY,
    __module__ = 'market_data_pb2'
    # @@protoc_insertion_point(class_scope:market_data.OHLCReply.OpenEntry)
    ))
  ,

  HighEntry = _reflection.GeneratedProtocolMessageType('HighEntry', (_message.Message,), dict(
    DESCRIPTOR = _OHLCREPLY_HIGHENTRY,
    __module__ = 'market_data_pb2'
    # @@protoc_insertion_point(class_scope:market_data.OHLCReply.HighEntry)
    ))
  ,

  LowEntry = _reflection.GeneratedProtocolMessageType('LowEntry', (_message.Message,), dict(
    DESCRIPTOR = _OHLCREPLY_LOWENTRY,
    __module__ = 'market_data_pb2'
    # @@protoc_insertion_point(class_scope:market_data.OHLCReply.LowEntry)
    ))
  ,

  CloseEntry = _reflection.GeneratedProtocolMessageType('CloseEntry', (_message.Message,), dict(
    DESCRIPTOR = _OHLCREPLY_CLOSEENTRY,
    __module__ = 'market_data_pb2'
    # @@protoc_insertion_point(class_scope:market_data.OHLCReply.CloseEntry)
    ))
  ,
  DESCRIPTOR = _OHLCREPLY,
  __module__ = 'market_data_pb2'
  # @@protoc_insertion_point(class_scope:market_data.OHLCReply)
  ))
_sym_db.RegisterMessage(OHLCReply)
_sym_db.RegisterMessage(OHLCReply.OHLCRet)
_sym_db.RegisterMessage(OHLCReply.OpenEntry)
_sym_db.RegisterMessage(OHLCReply.HighEntry)
_sym_db.RegisterMessage(OHLCReply.LowEntry)
_sym_db.RegisterMessage(OHLCReply.CloseEntry)


_OHLCREPLY_OPENENTRY.has_options = True
_OHLCREPLY_OPENENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_OHLCREPLY_HIGHENTRY.has_options = True
_OHLCREPLY_HIGHENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_OHLCREPLY_LOWENTRY.has_options = True
_OHLCREPLY_LOWENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_OHLCREPLY_CLOSEENTRY.has_options = True
_OHLCREPLY_CLOSEENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_MARKETDATA = _descriptor.ServiceDescriptor(
  name='MarketData',
  full_name='market_data.MarketData',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=658,
  serialized_end=731,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOHLC',
    full_name='market_data.MarketData.GetOHLC',
    index=0,
    containing_service=None,
    input_type=_OHLCREQUEST,
    output_type=_OHLCREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MARKETDATA)

DESCRIPTOR.services_by_name['MarketData'] = _MARKETDATA

# @@protoc_insertion_point(module_scope)
