# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: checkin-generator.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x63heckin-generator.proto\x12\x08tutorial\"\x94\x02\n\x11\x41ndroidBuildProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07product\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61rrier\x18\x03 \x01(\t\x12\r\n\x05radio\x18\x04 \x01(\t\x12\x12\n\nbootloader\x18\x05 \x01(\t\x12\x0e\n\x06\x63lient\x18\x06 \x01(\t\x12\x11\n\ttimestamp\x18\x07 \x01(\x03\x12\x16\n\x0egoogleServices\x18\x08 \x01(\x05\x12\x0e\n\x06\x64\x65vice\x18\t \x01(\t\x12\x12\n\nsdkVersion\x18\n \x01(\x05\x12\r\n\x05model\x18\x0b \x01(\t\x12\x14\n\x0cmanufacturer\x18\x0c \x01(\t\x12\x14\n\x0c\x62uildProduct\x18\r \x01(\t\x12\x14\n\x0cotaInstalled\x18\x0e \x01(\x08\"\x9d\x02\n\x13\x41ndroidCheckinProto\x12*\n\x05\x62uild\x18\x01 \x01(\x0b\x32\x1b.tutorial.AndroidBuildProto\x12\x17\n\x0flastCheckinMsec\x18\x02 \x01(\x03\x12*\n\x05\x65vent\x18\x03 \x03(\x0b\x32\x1b.tutorial.AndroidEventProto\x12-\n\x04stat\x18\x04 \x03(\x0b\x32\x1f.tutorial.AndroidStatisticProto\x12\x16\n\x0erequestedGroup\x18\x05 \x03(\t\x12\x14\n\x0c\x63\x65llOperator\x18\x06 \x01(\t\x12\x13\n\x0bsimOperator\x18\x07 \x01(\t\x12\x0f\n\x07roaming\x18\x08 \x01(\t\x12\x12\n\nuserNumber\x18\t \x01(\x05\"A\n\x11\x41ndroidEventProto\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x10\n\x08timeMsec\x18\x03 \x01(\x03\"@\n\x15\x41ndroidStatisticProto\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x0b\n\x03sum\x18\x03 \x01(\x02\"\x91\x05\n\x18\x44\x65viceConfigurationProto\x12\x13\n\x0btouchScreen\x18\x01 \x01(\x05\x12\x10\n\x08keyboard\x18\x02 \x01(\x05\x12\x12\n\nnavigation\x18\x03 \x01(\x05\x12\x14\n\x0cscreenLayout\x18\x04 \x01(\x05\x12\x17\n\x0fhasHardKeyboard\x18\x05 \x01(\x08\x12\x1c\n\x14hasFiveWayNavigation\x18\x06 \x01(\x08\x12\x15\n\rscreenDensity\x18\x07 \x01(\x05\x12\x13\n\x0bglEsVersion\x18\x08 \x01(\x05\x12\x1b\n\x13systemSharedLibrary\x18\t \x03(\t\x12\x1e\n\x16systemAvailableFeature\x18\n \x03(\t\x12\x16\n\x0enativePlatform\x18\x0b \x03(\t\x12\x13\n\x0bscreenWidth\x18\x0c \x01(\x05\x12\x14\n\x0cscreenHeight\x18\r \x01(\x05\x12\x1d\n\x15systemSupportedLocale\x18\x0e \x03(\t\x12\x13\n\x0bglExtension\x18\x0f \x03(\t\x12\x13\n\x0b\x64\x65viceClass\x18\x10 \x01(\x05\x12 \n\x14maxApkDownloadSizeMb\x18\x11 \x01(\x05:\x02\x35\x30\x12\x1d\n\x15smallestScreenWidthDP\x18\x12 \x01(\x05\x12\x17\n\x0clowRamDevice\x18\x13 \x01(\x05:\x01\x30\x12$\n\x10totalMemoryBytes\x18\x14 \x01(\x03:\n8354971648\x12\x1c\n\x11maxNumOf_CPUCores\x18\x15 \x01(\x05:\x01\x38\x12.\n\rdeviceFeature\x18\x1a \x03(\x0b\x32\x17.tutorial.DeviceFeature\x12\x14\n\tunknown28\x18\x1c \x01(\x05:\x01\x30\x12\x14\n\tunknown30\x18\x1e \x01(\x05:\x01\x34\",\n\rDeviceFeature\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\"\xfc\x03\n\x15\x41ndroidCheckinRequest\x12\x0c\n\x04imei\x18\x01 \x01(\t\x12\r\n\x02id\x18\x02 \x01(\x03:\x01\x30\x12\x0e\n\x06\x64igest\x18\x03 \x01(\t\x12.\n\x07\x63heckin\x18\x04 \x01(\x0b\x32\x1d.tutorial.AndroidCheckinProto\x12\x14\n\x0c\x64\x65siredBuild\x18\x05 \x01(\t\x12\x0e\n\x06locale\x18\x06 \x01(\t\x12\x11\n\tloggingId\x18\x07 \x01(\x03\x12\x15\n\rmarketCheckin\x18\x08 \x01(\t\x12\x0f\n\x07macAddr\x18\t \x03(\t\x12\x0c\n\x04meid\x18\n \x01(\t\x12\x15\n\raccountCookie\x18\x0b \x03(\t\x12\x10\n\x08timeZone\x18\x0c \x01(\t\x12\x15\n\rsecurityToken\x18\r \x01(\x06\x12\x0f\n\x07version\x18\x0e \x01(\x05\x12\x0f\n\x07otaCert\x18\x0f \x03(\t\x12\x14\n\x0cserialNumber\x18\x10 \x01(\t\x12\x0b\n\x03\x65sn\x18\x11 \x01(\t\x12?\n\x13\x64\x65viceConfiguration\x18\x12 \x01(\x0b\x32\".tutorial.DeviceConfigurationProto\x12\x13\n\x0bmacAddrType\x18\x13 \x03(\t\x12\x10\n\x08\x66ragment\x18\x14 \x01(\x05\x12\x10\n\x08userName\x18\x15 \x01(\t\x12\x18\n\x10userSerialNumber\x18\x16 \x01(\x05')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'checkin_generator_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ANDROIDBUILDPROTO._serialized_start=38
  _ANDROIDBUILDPROTO._serialized_end=314
  _ANDROIDCHECKINPROTO._serialized_start=317
  _ANDROIDCHECKINPROTO._serialized_end=602
  _ANDROIDEVENTPROTO._serialized_start=604
  _ANDROIDEVENTPROTO._serialized_end=669
  _ANDROIDSTATISTICPROTO._serialized_start=671
  _ANDROIDSTATISTICPROTO._serialized_end=735
  _DEVICECONFIGURATIONPROTO._serialized_start=738
  _DEVICECONFIGURATIONPROTO._serialized_end=1395
  _DEVICEFEATURE._serialized_start=1397
  _DEVICEFEATURE._serialized_end=1441
  _ANDROIDCHECKINREQUEST._serialized_start=1444
  _ANDROIDCHECKINREQUEST._serialized_end=1952
# @@protoc_insertion_point(module_scope)
