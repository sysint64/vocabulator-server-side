# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sync.proto

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
  name='sync.proto',
  package='sync',
  syntax='proto3',
  serialized_pb=_b('\n\nsync.proto\x12\x04sync\"7\n\x0fSyncGrpcRequest\x12$\n\x05words\x18\x01 \x03(\x0b\x32\x15.sync.WordGrpcRequest\"1\n\x0fWordGrpcRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x12\n\nscoreDelta\x18\x02 \x01(\x05\"m\n\x10SyncGrpcResponse\x12\x32\n\ncategories\x18\x01 \x03(\x0b\x32\x1e.sync.WordCategoryGrpcResponse\x12%\n\x05words\x18\x02 \x03(\x0b\x32\x16.sync.WordGrpcResponse\"4\n\x18WordCategoryGrpcResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xab\x01\n\x10WordGrpcResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x12\n\ncategoryId\x18\x02 \x01(\x03\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0ctranslations\x18\x04 \x01(\t\x12\x11\n\tpronounce\x18\x05 \x01(\t\x12\x31\n\x0b\x64\x65\x66initions\x18\x06 \x03(\x0b\x32\x1c.sync.DefinitionGrpcResponse\x12\r\n\x05score\x18\x07 \x01(\x03\"X\n\x16\x44\x65\x66initionGrpcResponse\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x0f\n\x07\x65xample\x18\x03 \x01(\t\x12\x10\n\x08synonyms\x18\x04 \x01(\t2=\n\x04Sync\x12\x35\n\x04Sync\x12\x15.sync.SyncGrpcRequest\x1a\x16.sync.SyncGrpcResponseB*\n\x16ru.kabylin.andrey.syncB\tSyncProtoP\x01\xa2\x02\x02SPb\x06proto3')
)




_SYNCGRPCREQUEST = _descriptor.Descriptor(
  name='SyncGrpcRequest',
  full_name='sync.SyncGrpcRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='words', full_name='sync.SyncGrpcRequest.words', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=20,
  serialized_end=75,
)


_WORDGRPCREQUEST = _descriptor.Descriptor(
  name='WordGrpcRequest',
  full_name='sync.WordGrpcRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sync.WordGrpcRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scoreDelta', full_name='sync.WordGrpcRequest.scoreDelta', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=126,
)


_SYNCGRPCRESPONSE = _descriptor.Descriptor(
  name='SyncGrpcResponse',
  full_name='sync.SyncGrpcResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='categories', full_name='sync.SyncGrpcResponse.categories', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='words', full_name='sync.SyncGrpcResponse.words', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=237,
)


_WORDCATEGORYGRPCRESPONSE = _descriptor.Descriptor(
  name='WordCategoryGrpcResponse',
  full_name='sync.WordCategoryGrpcResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sync.WordCategoryGrpcResponse.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='sync.WordCategoryGrpcResponse.name', index=1,
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
  serialized_start=239,
  serialized_end=291,
)


_WORDGRPCRESPONSE = _descriptor.Descriptor(
  name='WordGrpcResponse',
  full_name='sync.WordGrpcResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sync.WordGrpcResponse.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categoryId', full_name='sync.WordGrpcResponse.categoryId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='sync.WordGrpcResponse.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='translations', full_name='sync.WordGrpcResponse.translations', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pronounce', full_name='sync.WordGrpcResponse.pronounce', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='definitions', full_name='sync.WordGrpcResponse.definitions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='sync.WordGrpcResponse.score', index=6,
      number=7, type=3, cpp_type=2, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=465,
)


_DEFINITIONGRPCRESPONSE = _descriptor.Descriptor(
  name='DefinitionGrpcResponse',
  full_name='sync.DefinitionGrpcResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='sync.DefinitionGrpcResponse.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='sync.DefinitionGrpcResponse.desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='example', full_name='sync.DefinitionGrpcResponse.example', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='synonyms', full_name='sync.DefinitionGrpcResponse.synonyms', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=467,
  serialized_end=555,
)

_SYNCGRPCREQUEST.fields_by_name['words'].message_type = _WORDGRPCREQUEST
_SYNCGRPCRESPONSE.fields_by_name['categories'].message_type = _WORDCATEGORYGRPCRESPONSE
_SYNCGRPCRESPONSE.fields_by_name['words'].message_type = _WORDGRPCRESPONSE
_WORDGRPCRESPONSE.fields_by_name['definitions'].message_type = _DEFINITIONGRPCRESPONSE
DESCRIPTOR.message_types_by_name['SyncGrpcRequest'] = _SYNCGRPCREQUEST
DESCRIPTOR.message_types_by_name['WordGrpcRequest'] = _WORDGRPCREQUEST
DESCRIPTOR.message_types_by_name['SyncGrpcResponse'] = _SYNCGRPCRESPONSE
DESCRIPTOR.message_types_by_name['WordCategoryGrpcResponse'] = _WORDCATEGORYGRPCRESPONSE
DESCRIPTOR.message_types_by_name['WordGrpcResponse'] = _WORDGRPCRESPONSE
DESCRIPTOR.message_types_by_name['DefinitionGrpcResponse'] = _DEFINITIONGRPCRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SyncGrpcRequest = _reflection.GeneratedProtocolMessageType('SyncGrpcRequest', (_message.Message,), dict(
  DESCRIPTOR = _SYNCGRPCREQUEST,
  __module__ = 'sync_pb2'
  # @@protoc_insertion_point(class_scope:sync.SyncGrpcRequest)
  ))
_sym_db.RegisterMessage(SyncGrpcRequest)

WordGrpcRequest = _reflection.GeneratedProtocolMessageType('WordGrpcRequest', (_message.Message,), dict(
  DESCRIPTOR = _WORDGRPCREQUEST,
  __module__ = 'sync_pb2'
  # @@protoc_insertion_point(class_scope:sync.WordGrpcRequest)
  ))
_sym_db.RegisterMessage(WordGrpcRequest)

SyncGrpcResponse = _reflection.GeneratedProtocolMessageType('SyncGrpcResponse', (_message.Message,), dict(
  DESCRIPTOR = _SYNCGRPCRESPONSE,
  __module__ = 'sync_pb2'
  # @@protoc_insertion_point(class_scope:sync.SyncGrpcResponse)
  ))
_sym_db.RegisterMessage(SyncGrpcResponse)

WordCategoryGrpcResponse = _reflection.GeneratedProtocolMessageType('WordCategoryGrpcResponse', (_message.Message,), dict(
  DESCRIPTOR = _WORDCATEGORYGRPCRESPONSE,
  __module__ = 'sync_pb2'
  # @@protoc_insertion_point(class_scope:sync.WordCategoryGrpcResponse)
  ))
_sym_db.RegisterMessage(WordCategoryGrpcResponse)

WordGrpcResponse = _reflection.GeneratedProtocolMessageType('WordGrpcResponse', (_message.Message,), dict(
  DESCRIPTOR = _WORDGRPCRESPONSE,
  __module__ = 'sync_pb2'
  # @@protoc_insertion_point(class_scope:sync.WordGrpcResponse)
  ))
_sym_db.RegisterMessage(WordGrpcResponse)

DefinitionGrpcResponse = _reflection.GeneratedProtocolMessageType('DefinitionGrpcResponse', (_message.Message,), dict(
  DESCRIPTOR = _DEFINITIONGRPCRESPONSE,
  __module__ = 'sync_pb2'
  # @@protoc_insertion_point(class_scope:sync.DefinitionGrpcResponse)
  ))
_sym_db.RegisterMessage(DefinitionGrpcResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026ru.kabylin.andrey.syncB\tSyncProtoP\001\242\002\002SP'))

_SYNC = _descriptor.ServiceDescriptor(
  name='Sync',
  full_name='sync.Sync',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=557,
  serialized_end=618,
  methods=[
  _descriptor.MethodDescriptor(
    name='Sync',
    full_name='sync.Sync.Sync',
    index=0,
    containing_service=None,
    input_type=_SYNCGRPCREQUEST,
    output_type=_SYNCGRPCRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SYNC)

DESCRIPTOR.services_by_name['Sync'] = _SYNC

# @@protoc_insertion_point(module_scope)
