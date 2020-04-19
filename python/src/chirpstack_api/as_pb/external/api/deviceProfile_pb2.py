# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/deviceProfile.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.as_pb.external.api import profiles_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_profiles__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chirpstack-api/as_pb/external/api/deviceProfile.proto',
  package='api',
  syntax='proto3',
  serialized_options=b'Z7github.com/iBrick/chirpstack-api/go/v3/as/external/api',
  serialized_pb=b'\n5chirpstack-api/as_pb/external/api/deviceProfile.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x30\x63hirpstack-api/as_pb/external/api/profiles.proto\"H\n\x1a\x43reateDeviceProfileRequest\x12*\n\x0e\x64\x65vice_profile\x18\x01 \x01(\x0b\x32\x12.api.DeviceProfile\")\n\x1b\x43reateDeviceProfileResponse\x12\n\n\x02id\x18\x01 \x01(\t\"%\n\x17GetDeviceProfileRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xa6\x01\n\x18GetDeviceProfileResponse\x12*\n\x0e\x64\x65vice_profile\x18\x01 \x01(\x0b\x32\x12.api.DeviceProfile\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"H\n\x1aUpdateDeviceProfileRequest\x12*\n\x0e\x64\x65vice_profile\x18\x01 \x01(\x0b\x32\x12.api.DeviceProfile\"(\n\x1a\x44\x65leteDeviceProfileRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xe6\x01\n\x15\x44\x65viceProfileListItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\'\n\x0forganization_id\x18\x03 \x01(\x03R\x0eorganizationID\x12*\n\x11network_server_id\x18\x04 \x01(\x03R\x0fnetworkServerID\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x89\x01\n\x18ListDeviceProfileRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\'\n\x0forganization_id\x18\x03 \x01(\x03R\x0eorganizationID\x12%\n\x0e\x61pplication_id\x18\x04 \x01(\x03R\rapplicationID\"\\\n\x19ListDeviceProfileResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12*\n\x06result\x18\x02 \x03(\x0b\x32\x1a.api.DeviceProfileListItem2\xae\x04\n\x14\x44\x65viceProfileService\x12l\n\x06\x43reate\x12\x1f.api.CreateDeviceProfileRequest\x1a .api.CreateDeviceProfileResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/api/device-profiles:\x01*\x12\x65\n\x03Get\x12\x1c.api.GetDeviceProfileRequest\x1a\x1d.api.GetDeviceProfileResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/api/device-profiles/{id}\x12v\n\x06Update\x12\x1f.api.UpdateDeviceProfileRequest\x1a\x16.google.protobuf.Empty\"3\x82\xd3\xe4\x93\x02-\x1a(/api/device-profiles/{device_profile.id}:\x01*\x12\x64\n\x06\x44\x65lete\x12\x1f.api.DeleteDeviceProfileRequest\x1a\x16.google.protobuf.Empty\"!\x82\xd3\xe4\x93\x02\x1b*\x19/api/device-profiles/{id}\x12\x63\n\x04List\x12\x1d.api.ListDeviceProfileRequest\x1a\x1e.api.ListDeviceProfileResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/api/device-profilesB9Z7github.com/iBrick/chirpstack-api/go/v3/as/external/apib\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,chirpstack__api_dot_as__pb_dot_external_dot_api_dot_profiles__pb2.DESCRIPTOR,])




_CREATEDEVICEPROFILEREQUEST = _descriptor.Descriptor(
  name='CreateDeviceProfileRequest',
  full_name='api.CreateDeviceProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_profile', full_name='api.CreateDeviceProfileRequest.device_profile', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=276,
)


_CREATEDEVICEPROFILERESPONSE = _descriptor.Descriptor(
  name='CreateDeviceProfileResponse',
  full_name='api.CreateDeviceProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.CreateDeviceProfileResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=319,
)


_GETDEVICEPROFILEREQUEST = _descriptor.Descriptor(
  name='GetDeviceProfileRequest',
  full_name='api.GetDeviceProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.GetDeviceProfileRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=358,
)


_GETDEVICEPROFILERESPONSE = _descriptor.Descriptor(
  name='GetDeviceProfileResponse',
  full_name='api.GetDeviceProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_profile', full_name='api.GetDeviceProfileResponse.device_profile', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='api.GetDeviceProfileResponse.created_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='api.GetDeviceProfileResponse.updated_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=527,
)


_UPDATEDEVICEPROFILEREQUEST = _descriptor.Descriptor(
  name='UpdateDeviceProfileRequest',
  full_name='api.UpdateDeviceProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_profile', full_name='api.UpdateDeviceProfileRequest.device_profile', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=601,
)


_DELETEDEVICEPROFILEREQUEST = _descriptor.Descriptor(
  name='DeleteDeviceProfileRequest',
  full_name='api.DeleteDeviceProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.DeleteDeviceProfileRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=643,
)


_DEVICEPROFILELISTITEM = _descriptor.Descriptor(
  name='DeviceProfileListItem',
  full_name='api.DeviceProfileListItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.DeviceProfileListItem.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.DeviceProfileListItem.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='api.DeviceProfileListItem.organization_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='organizationID', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_server_id', full_name='api.DeviceProfileListItem.network_server_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='networkServerID', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='api.DeviceProfileListItem.created_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='api.DeviceProfileListItem.updated_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=646,
  serialized_end=876,
)


_LISTDEVICEPROFILEREQUEST = _descriptor.Descriptor(
  name='ListDeviceProfileRequest',
  full_name='api.ListDeviceProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='api.ListDeviceProfileRequest.limit', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='api.ListDeviceProfileRequest.offset', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='api.ListDeviceProfileRequest.organization_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='organizationID', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_id', full_name='api.ListDeviceProfileRequest.application_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='applicationID', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=879,
  serialized_end=1016,
)


_LISTDEVICEPROFILERESPONSE = _descriptor.Descriptor(
  name='ListDeviceProfileResponse',
  full_name='api.ListDeviceProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_count', full_name='api.ListDeviceProfileResponse.total_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='api.ListDeviceProfileResponse.result', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1018,
  serialized_end=1110,
)

_CREATEDEVICEPROFILEREQUEST.fields_by_name['device_profile'].message_type = chirpstack__api_dot_as__pb_dot_external_dot_api_dot_profiles__pb2._DEVICEPROFILE
_GETDEVICEPROFILERESPONSE.fields_by_name['device_profile'].message_type = chirpstack__api_dot_as__pb_dot_external_dot_api_dot_profiles__pb2._DEVICEPROFILE
_GETDEVICEPROFILERESPONSE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETDEVICEPROFILERESPONSE.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_UPDATEDEVICEPROFILEREQUEST.fields_by_name['device_profile'].message_type = chirpstack__api_dot_as__pb_dot_external_dot_api_dot_profiles__pb2._DEVICEPROFILE
_DEVICEPROFILELISTITEM.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DEVICEPROFILELISTITEM.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTDEVICEPROFILERESPONSE.fields_by_name['result'].message_type = _DEVICEPROFILELISTITEM
DESCRIPTOR.message_types_by_name['CreateDeviceProfileRequest'] = _CREATEDEVICEPROFILEREQUEST
DESCRIPTOR.message_types_by_name['CreateDeviceProfileResponse'] = _CREATEDEVICEPROFILERESPONSE
DESCRIPTOR.message_types_by_name['GetDeviceProfileRequest'] = _GETDEVICEPROFILEREQUEST
DESCRIPTOR.message_types_by_name['GetDeviceProfileResponse'] = _GETDEVICEPROFILERESPONSE
DESCRIPTOR.message_types_by_name['UpdateDeviceProfileRequest'] = _UPDATEDEVICEPROFILEREQUEST
DESCRIPTOR.message_types_by_name['DeleteDeviceProfileRequest'] = _DELETEDEVICEPROFILEREQUEST
DESCRIPTOR.message_types_by_name['DeviceProfileListItem'] = _DEVICEPROFILELISTITEM
DESCRIPTOR.message_types_by_name['ListDeviceProfileRequest'] = _LISTDEVICEPROFILEREQUEST
DESCRIPTOR.message_types_by_name['ListDeviceProfileResponse'] = _LISTDEVICEPROFILERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateDeviceProfileRequest = _reflection.GeneratedProtocolMessageType('CreateDeviceProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDEVICEPROFILEREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.deviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateDeviceProfileRequest)
  })
_sym_db.RegisterMessage(CreateDeviceProfileRequest)

CreateDeviceProfileResponse = _reflection.GeneratedProtocolMessageType('CreateDeviceProfileResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDEVICEPROFILERESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.deviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateDeviceProfileResponse)
  })
_sym_db.RegisterMessage(CreateDeviceProfileResponse)

GetDeviceProfileRequest = _reflection.GeneratedProtocolMessageType('GetDeviceProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDEVICEPROFILEREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.deviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.GetDeviceProfileRequest)
  })
_sym_db.RegisterMessage(GetDeviceProfileRequest)

GetDeviceProfileResponse = _reflection.GeneratedProtocolMessageType('GetDeviceProfileResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDEVICEPROFILERESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.deviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.GetDeviceProfileResponse)
  })
_sym_db.RegisterMessage(GetDeviceProfileResponse)

UpdateDeviceProfileRequest = _reflection.GeneratedProtocolMessageType('UpdateDeviceProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDEVICEPROFILEREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.deviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdateDeviceProfileRequest)
  })
_sym_db.RegisterMessage(UpdateDeviceProfileRequest)

DeleteDeviceProfileRequest = _reflection.GeneratedProtocolMessageType('DeleteDeviceProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDEVICEPROFILEREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.deviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.DeleteDeviceProfileRequest)
  })
_sym_db.RegisterMessage(DeleteDeviceProfileRequest)

DeviceProfileListItem = _reflection.GeneratedProtocolMessageType('DeviceProfileListItem', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEPROFILELISTITEM,
  '__module__' : 'chirpstack_api.as_pb.external.api.deviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.DeviceProfileListItem)
  })
_sym_db.RegisterMessage(DeviceProfileListItem)

ListDeviceProfileRequest = _reflection.GeneratedProtocolMessageType('ListDeviceProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICEPROFILEREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.deviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.ListDeviceProfileRequest)
  })
_sym_db.RegisterMessage(ListDeviceProfileRequest)

ListDeviceProfileResponse = _reflection.GeneratedProtocolMessageType('ListDeviceProfileResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICEPROFILERESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.deviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.ListDeviceProfileResponse)
  })
_sym_db.RegisterMessage(ListDeviceProfileResponse)


DESCRIPTOR._options = None

_DEVICEPROFILESERVICE = _descriptor.ServiceDescriptor(
  name='DeviceProfileService',
  full_name='api.DeviceProfileService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1113,
  serialized_end=1671,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='api.DeviceProfileService.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEDEVICEPROFILEREQUEST,
    output_type=_CREATEDEVICEPROFILERESPONSE,
    serialized_options=b'\202\323\344\223\002\031\"\024/api/device-profiles:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='api.DeviceProfileService.Get',
    index=1,
    containing_service=None,
    input_type=_GETDEVICEPROFILEREQUEST,
    output_type=_GETDEVICEPROFILERESPONSE,
    serialized_options=b'\202\323\344\223\002\033\022\031/api/device-profiles/{id}',
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='api.DeviceProfileService.Update',
    index=2,
    containing_service=None,
    input_type=_UPDATEDEVICEPROFILEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002-\032(/api/device-profiles/{device_profile.id}:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='api.DeviceProfileService.Delete',
    index=3,
    containing_service=None,
    input_type=_DELETEDEVICEPROFILEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\033*\031/api/device-profiles/{id}',
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='api.DeviceProfileService.List',
    index=4,
    containing_service=None,
    input_type=_LISTDEVICEPROFILEREQUEST,
    output_type=_LISTDEVICEPROFILERESPONSE,
    serialized_options=b'\202\323\344\223\002\026\022\024/api/device-profiles',
  ),
])
_sym_db.RegisterServiceDescriptor(_DEVICEPROFILESERVICE)

DESCRIPTOR.services_by_name['DeviceProfileService'] = _DEVICEPROFILESERVICE

# @@protoc_insertion_point(module_scope)
