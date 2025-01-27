# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: org/apache/beam/model/pipeline/v1/schema.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'org/apache/beam/model/pipeline/v1/schema.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import beam_runner_api_pb2 as org_dot_apache_dot_beam_dot_model_dot_pipeline_dot_v1_dot_beam__runner__api__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.org/apache/beam/model/pipeline/v1/schema.proto\x12!org.apache.beam.model.pipeline.v1\x1a\x37org/apache/beam/model/pipeline/v1/beam_runner_api.proto\"\xaa\x01\n\x06Schema\x12\x38\n\x06\x66ields\x18\x01 \x03(\x0b\x32(.org.apache.beam.model.pipeline.v1.Field\x12\n\n\x02id\x18\x02 \x01(\t\x12:\n\x07options\x18\x03 \x03(\x0b\x32).org.apache.beam.model.pipeline.v1.Option\x12\x1e\n\x16\x65ncoding_positions_set\x18\x04 \x01(\x08\"\xc9\x01\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12:\n\x04type\x18\x03 \x01(\x0b\x32,.org.apache.beam.model.pipeline.v1.FieldType\x12\n\n\x02id\x18\x04 \x01(\x05\x12\x19\n\x11\x65ncoding_position\x18\x05 \x01(\x05\x12:\n\x07options\x18\x06 \x03(\x0b\x32).org.apache.beam.model.pipeline.v1.Option\"\xc6\x03\n\tFieldType\x12\x10\n\x08nullable\x18\x01 \x01(\x08\x12\x44\n\x0b\x61tomic_type\x18\x02 \x01(\x0e\x32-.org.apache.beam.model.pipeline.v1.AtomicTypeH\x00\x12\x42\n\narray_type\x18\x03 \x01(\x0b\x32,.org.apache.beam.model.pipeline.v1.ArrayTypeH\x00\x12H\n\riterable_type\x18\x04 \x01(\x0b\x32/.org.apache.beam.model.pipeline.v1.IterableTypeH\x00\x12>\n\x08map_type\x18\x05 \x01(\x0b\x32*.org.apache.beam.model.pipeline.v1.MapTypeH\x00\x12>\n\x08row_type\x18\x06 \x01(\x0b\x32*.org.apache.beam.model.pipeline.v1.RowTypeH\x00\x12\x46\n\x0clogical_type\x18\x07 \x01(\x0b\x32..org.apache.beam.model.pipeline.v1.LogicalTypeH\x00\x42\x0b\n\ttype_info\"O\n\tArrayType\x12\x42\n\x0c\x65lement_type\x18\x01 \x01(\x0b\x32,.org.apache.beam.model.pipeline.v1.FieldType\"R\n\x0cIterableType\x12\x42\n\x0c\x65lement_type\x18\x01 \x01(\x0b\x32,.org.apache.beam.model.pipeline.v1.FieldType\"\x8b\x01\n\x07MapType\x12>\n\x08key_type\x18\x01 \x01(\x0b\x32,.org.apache.beam.model.pipeline.v1.FieldType\x12@\n\nvalue_type\x18\x02 \x01(\x0b\x32,.org.apache.beam.model.pipeline.v1.FieldType\"D\n\x07RowType\x12\x39\n\x06schema\x18\x01 \x01(\x0b\x32).org.apache.beam.model.pipeline.v1.Schema\"\xf7\x01\n\x0bLogicalType\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x44\n\x0erepresentation\x18\x03 \x01(\x0b\x32,.org.apache.beam.model.pipeline.v1.FieldType\x12\x43\n\rargument_type\x18\x04 \x01(\x0b\x32,.org.apache.beam.model.pipeline.v1.FieldType\x12?\n\x08\x61rgument\x18\x05 \x01(\x0b\x32-.org.apache.beam.model.pipeline.v1.FieldValue\"\xdf\x03\n\x0cLogicalTypes\"\xce\x03\n\x04\x45num\x12?\n\x0fPYTHON_CALLABLE\x10\x00\x1a*\xa2\xb4\xfa\xc2\x05$beam:logical_type:python_callable:v1\x12=\n\x0eMICROS_INSTANT\x10\x01\x1a)\xa2\xb4\xfa\xc2\x05#beam:logical_type:micros_instant:v1\x12=\n\x0eMILLIS_INSTANT\x10\x02\x1a)\xa2\xb4\xfa\xc2\x05#beam:logical_type:millis_instant:v1\x12/\n\x07\x44\x45\x43IMAL\x10\x03\x1a\"\xa2\xb4\xfa\xc2\x05\x1c\x62\x65\x61m:logical_type:decimal:v1\x12\x37\n\x0b\x46IXED_BYTES\x10\x04\x1a&\xa2\xb4\xfa\xc2\x05 beam:logical_type:fixed_bytes:v1\x12\x33\n\tVAR_BYTES\x10\x05\x1a$\xa2\xb4\xfa\xc2\x05\x1e\x62\x65\x61m:logical_type:var_bytes:v1\x12\x35\n\nFIXED_CHAR\x10\x06\x1a%\xa2\xb4\xfa\xc2\x05\x1f\x62\x65\x61m:logical_type:fixed_char:v1\x12\x31\n\x08VAR_CHAR\x10\x07\x1a#\xa2\xb4\xfa\xc2\x05\x1d\x62\x65\x61m:logical_type:var_char:v1\"\x90\x01\n\x06Option\x12\x0c\n\x04name\x18\x01 \x01(\t\x12:\n\x04type\x18\x02 \x01(\x0b\x32,.org.apache.beam.model.pipeline.v1.FieldType\x12<\n\x05value\x18\x03 \x01(\x0b\x32-.org.apache.beam.model.pipeline.v1.FieldValue\"D\n\x03Row\x12=\n\x06values\x18\x01 \x03(\x0b\x32-.org.apache.beam.model.pipeline.v1.FieldValue\"\xd7\x03\n\nFieldValue\x12J\n\x0c\x61tomic_value\x18\x01 \x01(\x0b\x32\x32.org.apache.beam.model.pipeline.v1.AtomicTypeValueH\x00\x12H\n\x0b\x61rray_value\x18\x02 \x01(\x0b\x32\x31.org.apache.beam.model.pipeline.v1.ArrayTypeValueH\x00\x12N\n\x0eiterable_value\x18\x03 \x01(\x0b\x32\x34.org.apache.beam.model.pipeline.v1.IterableTypeValueH\x00\x12\x44\n\tmap_value\x18\x04 \x01(\x0b\x32/.org.apache.beam.model.pipeline.v1.MapTypeValueH\x00\x12;\n\trow_value\x18\x05 \x01(\x0b\x32&.org.apache.beam.model.pipeline.v1.RowH\x00\x12Q\n\x12logical_type_value\x18\x06 \x01(\x0b\x32\x33.org.apache.beam.model.pipeline.v1.LogicalTypeValueH\x00\x42\r\n\x0b\x66ield_value\"\xb6\x01\n\x0f\x41tomicTypeValue\x12\x0e\n\x04\x62yte\x18\x01 \x01(\x05H\x00\x12\x0f\n\x05int16\x18\x02 \x01(\x05H\x00\x12\x0f\n\x05int32\x18\x03 \x01(\x05H\x00\x12\x0f\n\x05int64\x18\x04 \x01(\x03H\x00\x12\x0f\n\x05\x66loat\x18\x05 \x01(\x02H\x00\x12\x10\n\x06\x64ouble\x18\x06 \x01(\x01H\x00\x12\x10\n\x06string\x18\x07 \x01(\tH\x00\x12\x11\n\x07\x62oolean\x18\x08 \x01(\x08H\x00\x12\x0f\n\x05\x62ytes\x18\t \x01(\x0cH\x00\x42\x07\n\x05value\"P\n\x0e\x41rrayTypeValue\x12>\n\x07\x65lement\x18\x01 \x03(\x0b\x32-.org.apache.beam.model.pipeline.v1.FieldValue\"S\n\x11IterableTypeValue\x12>\n\x07\x65lement\x18\x01 \x03(\x0b\x32-.org.apache.beam.model.pipeline.v1.FieldValue\"P\n\x0cMapTypeValue\x12@\n\x07\x65ntries\x18\x01 \x03(\x0b\x32/.org.apache.beam.model.pipeline.v1.MapTypeEntry\"\x88\x01\n\x0cMapTypeEntry\x12:\n\x03key\x18\x01 \x01(\x0b\x32-.org.apache.beam.model.pipeline.v1.FieldValue\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.org.apache.beam.model.pipeline.v1.FieldValue\"P\n\x10LogicalTypeValue\x12<\n\x05value\x18\x01 \x01(\x0b\x32-.org.apache.beam.model.pipeline.v1.FieldValue*\x83\x01\n\nAtomicType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04\x42YTE\x10\x01\x12\t\n\x05INT16\x10\x02\x12\t\n\x05INT32\x10\x03\x12\t\n\x05INT64\x10\x04\x12\t\n\x05\x46LOAT\x10\x05\x12\n\n\x06\x44OUBLE\x10\x06\x12\n\n\x06STRING\x10\x07\x12\x0b\n\x07\x42OOLEAN\x10\x08\x12\t\n\x05\x42YTES\x10\tBx\n!org.apache.beam.model.pipeline.v1B\tSchemaApiZHgithub.com/apache/beam/sdks/v2/go/pkg/beam/model/pipeline_v1;pipeline_v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'org.apache.beam.model.pipeline.v1.schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!org.apache.beam.model.pipeline.v1B\tSchemaApiZHgithub.com/apache/beam/sdks/v2/go/pkg/beam/model/pipeline_v1;pipeline_v1'
  _globals['_LOGICALTYPES_ENUM'].values_by_name["PYTHON_CALLABLE"]._loaded_options = None
  _globals['_LOGICALTYPES_ENUM'].values_by_name["PYTHON_CALLABLE"]._serialized_options = b'\242\264\372\302\005$beam:logical_type:python_callable:v1'
  _globals['_LOGICALTYPES_ENUM'].values_by_name["MICROS_INSTANT"]._loaded_options = None
  _globals['_LOGICALTYPES_ENUM'].values_by_name["MICROS_INSTANT"]._serialized_options = b'\242\264\372\302\005#beam:logical_type:micros_instant:v1'
  _globals['_LOGICALTYPES_ENUM'].values_by_name["MILLIS_INSTANT"]._loaded_options = None
  _globals['_LOGICALTYPES_ENUM'].values_by_name["MILLIS_INSTANT"]._serialized_options = b'\242\264\372\302\005#beam:logical_type:millis_instant:v1'
  _globals['_LOGICALTYPES_ENUM'].values_by_name["DECIMAL"]._loaded_options = None
  _globals['_LOGICALTYPES_ENUM'].values_by_name["DECIMAL"]._serialized_options = b'\242\264\372\302\005\034beam:logical_type:decimal:v1'
  _globals['_LOGICALTYPES_ENUM'].values_by_name["FIXED_BYTES"]._loaded_options = None
  _globals['_LOGICALTYPES_ENUM'].values_by_name["FIXED_BYTES"]._serialized_options = b'\242\264\372\302\005 beam:logical_type:fixed_bytes:v1'
  _globals['_LOGICALTYPES_ENUM'].values_by_name["VAR_BYTES"]._loaded_options = None
  _globals['_LOGICALTYPES_ENUM'].values_by_name["VAR_BYTES"]._serialized_options = b'\242\264\372\302\005\036beam:logical_type:var_bytes:v1'
  _globals['_LOGICALTYPES_ENUM'].values_by_name["FIXED_CHAR"]._loaded_options = None
  _globals['_LOGICALTYPES_ENUM'].values_by_name["FIXED_CHAR"]._serialized_options = b'\242\264\372\302\005\037beam:logical_type:fixed_char:v1'
  _globals['_LOGICALTYPES_ENUM'].values_by_name["VAR_CHAR"]._loaded_options = None
  _globals['_LOGICALTYPES_ENUM'].values_by_name["VAR_CHAR"]._serialized_options = b'\242\264\372\302\005\035beam:logical_type:var_char:v1'
  _globals['_ATOMICTYPE']._serialized_start=3432
  _globals['_ATOMICTYPE']._serialized_end=3563
  _globals['_SCHEMA']._serialized_start=143
  _globals['_SCHEMA']._serialized_end=313
  _globals['_FIELD']._serialized_start=316
  _globals['_FIELD']._serialized_end=517
  _globals['_FIELDTYPE']._serialized_start=520
  _globals['_FIELDTYPE']._serialized_end=974
  _globals['_ARRAYTYPE']._serialized_start=976
  _globals['_ARRAYTYPE']._serialized_end=1055
  _globals['_ITERABLETYPE']._serialized_start=1057
  _globals['_ITERABLETYPE']._serialized_end=1139
  _globals['_MAPTYPE']._serialized_start=1142
  _globals['_MAPTYPE']._serialized_end=1281
  _globals['_ROWTYPE']._serialized_start=1283
  _globals['_ROWTYPE']._serialized_end=1351
  _globals['_LOGICALTYPE']._serialized_start=1354
  _globals['_LOGICALTYPE']._serialized_end=1601
  _globals['_LOGICALTYPES']._serialized_start=1604
  _globals['_LOGICALTYPES']._serialized_end=2083
  _globals['_LOGICALTYPES_ENUM']._serialized_start=1621
  _globals['_LOGICALTYPES_ENUM']._serialized_end=2083
  _globals['_OPTION']._serialized_start=2086
  _globals['_OPTION']._serialized_end=2230
  _globals['_ROW']._serialized_start=2232
  _globals['_ROW']._serialized_end=2300
  _globals['_FIELDVALUE']._serialized_start=2303
  _globals['_FIELDVALUE']._serialized_end=2774
  _globals['_ATOMICTYPEVALUE']._serialized_start=2777
  _globals['_ATOMICTYPEVALUE']._serialized_end=2959
  _globals['_ARRAYTYPEVALUE']._serialized_start=2961
  _globals['_ARRAYTYPEVALUE']._serialized_end=3041
  _globals['_ITERABLETYPEVALUE']._serialized_start=3043
  _globals['_ITERABLETYPEVALUE']._serialized_end=3126
  _globals['_MAPTYPEVALUE']._serialized_start=3128
  _globals['_MAPTYPEVALUE']._serialized_end=3208
  _globals['_MAPTYPEENTRY']._serialized_start=3211
  _globals['_MAPTYPEENTRY']._serialized_end=3347
  _globals['_LOGICALTYPEVALUE']._serialized_start=3349
  _globals['_LOGICALTYPEVALUE']._serialized_end=3429
# @@protoc_insertion_point(module_scope)
