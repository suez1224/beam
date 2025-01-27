# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: org/apache/beam/model/fn_execution/v1/beam_fn_api.proto
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
    'org/apache/beam/model/fn_execution/v1/beam_fn_api.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...pipeline.v1 import beam_runner_api_pb2 as org_dot_apache_dot_beam_dot_model_dot_pipeline_dot_v1_dot_beam__runner__api__pb2
from ...pipeline.v1 import endpoints_pb2 as org_dot_apache_dot_beam_dot_model_dot_pipeline_dot_v1_dot_endpoints__pb2
from ...pipeline.v1 import metrics_pb2 as org_dot_apache_dot_beam_dot_model_dot_pipeline_dot_v1_dot_metrics__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7org/apache/beam/model/fn_execution/v1/beam_fn_api.proto\x12%org.apache.beam.model.fn_execution.v1\x1a\x37org/apache/beam/model/pipeline/v1/beam_runner_api.proto\x1a\x31org/apache/beam/model/pipeline/v1/endpoints.proto\x1a/org/apache/beam/model/pipeline/v1/metrics.proto\x1a google/protobuf/descriptor.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"{\n\x0eRemoteGrpcPort\x12W\n\x16\x61pi_service_descriptor\x18\x01 \x01(\x0b\x32\x37.org.apache.beam.model.pipeline.v1.ApiServiceDescriptor\x12\x10\n\x08\x63oder_id\x18\x02 \x01(\t\"I\n!GetProcessBundleDescriptorRequest\x12$\n\x1cprocess_bundle_descriptor_id\x18\x01 \x01(\t\"\xa3\x06\n\x12InstructionRequest\x12\x16\n\x0einstruction_id\x18\x01 \x01(\t\x12V\n\x0eprocess_bundle\x18\xe9\x07 \x01(\x0b\x32;.org.apache.beam.model.fn_execution.v1.ProcessBundleRequestH\x00\x12g\n\x17process_bundle_progress\x18\xea\x07 \x01(\x0b\x32\x43.org.apache.beam.model.fn_execution.v1.ProcessBundleProgressRequestH\x00\x12\x61\n\x14process_bundle_split\x18\xeb\x07 \x01(\x0b\x32@.org.apache.beam.model.fn_execution.v1.ProcessBundleSplitRequestH\x00\x12X\n\x0f\x66inalize_bundle\x18\xec\x07 \x01(\x0b\x32<.org.apache.beam.model.fn_execution.v1.FinalizeBundleRequestH\x00\x12\x62\n\x10monitoring_infos\x18\xed\x07 \x01(\x0b\x32\x45.org.apache.beam.model.fn_execution.v1.MonitoringInfosMetadataRequestH\x00\x12i\n\x18harness_monitoring_infos\x18\xee\x07 \x01(\x0b\x32\x44.org.apache.beam.model.fn_execution.v1.HarnessMonitoringInfosRequestH\x00\x12P\n\x0bsample_data\x18\xef\x07 \x01(\x0b\x32\x38.org.apache.beam.model.fn_execution.v1.SampleDataRequestH\x00\x12K\n\x08register\x18\xe8\x07 \x01(\x0b\x32\x36.org.apache.beam.model.fn_execution.v1.RegisterRequestH\x00\x42\t\n\x07request\"\xbc\x06\n\x13InstructionResponse\x12\x16\n\x0einstruction_id\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12W\n\x0eprocess_bundle\x18\xe9\x07 \x01(\x0b\x32<.org.apache.beam.model.fn_execution.v1.ProcessBundleResponseH\x00\x12h\n\x17process_bundle_progress\x18\xea\x07 \x01(\x0b\x32\x44.org.apache.beam.model.fn_execution.v1.ProcessBundleProgressResponseH\x00\x12\x62\n\x14process_bundle_split\x18\xeb\x07 \x01(\x0b\x32\x41.org.apache.beam.model.fn_execution.v1.ProcessBundleSplitResponseH\x00\x12Y\n\x0f\x66inalize_bundle\x18\xec\x07 \x01(\x0b\x32=.org.apache.beam.model.fn_execution.v1.FinalizeBundleResponseH\x00\x12\x63\n\x10monitoring_infos\x18\xed\x07 \x01(\x0b\x32\x46.org.apache.beam.model.fn_execution.v1.MonitoringInfosMetadataResponseH\x00\x12j\n\x18harness_monitoring_infos\x18\xee\x07 \x01(\x0b\x32\x45.org.apache.beam.model.fn_execution.v1.HarnessMonitoringInfosResponseH\x00\x12Q\n\x0bsample_data\x18\xef\x07 \x01(\x0b\x32\x39.org.apache.beam.model.fn_execution.v1.SampleDataResponseH\x00\x12L\n\x08register\x18\xe8\x07 \x01(\x0b\x32\x37.org.apache.beam.model.fn_execution.v1.RegisterResponseH\x00\x42\n\n\x08response\",\n\x11SampleDataRequest\x12\x17\n\x0fpcollection_ids\x18\x01 \x03(\t\"!\n\x0eSampledElement\x12\x0f\n\x07\x65lement\x18\x01 \x01(\x0c\"\xd2\x02\n\x12SampleDataResponse\x12\x66\n\x0f\x65lement_samples\x18\x01 \x03(\x0b\x32M.org.apache.beam.model.fn_execution.v1.SampleDataResponse.ElementSamplesEntry\x1aV\n\x0b\x45lementList\x12G\n\x08\x65lements\x18\x01 \x03(\x0b\x32\x35.org.apache.beam.model.fn_execution.v1.SampledElement\x1a|\n\x13\x45lementSamplesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12T\n\x05value\x18\x02 \x01(\x0b\x32\x45.org.apache.beam.model.fn_execution.v1.SampleDataResponse.ElementList:\x02\x38\x01\"\x1f\n\x1dHarnessMonitoringInfosRequest\"\xcb\x01\n\x1eHarnessMonitoringInfosResponse\x12r\n\x0fmonitoring_data\x18\x01 \x03(\x0b\x32Y.org.apache.beam.model.fn_execution.v1.HarnessMonitoringInfosResponse.MonitoringDataEntry\x1a\x35\n\x13MonitoringDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"t\n\x0fRegisterRequest\x12\x61\n\x19process_bundle_descriptor\x18\x01 \x03(\x0b\x32>.org.apache.beam.model.fn_execution.v1.ProcessBundleDescriptor\"\x12\n\x10RegisterResponse\"\xe1\t\n\x17ProcessBundleDescriptor\x12\n\n\x02id\x18\x01 \x01(\t\x12\x62\n\ntransforms\x18\x02 \x03(\x0b\x32N.org.apache.beam.model.fn_execution.v1.ProcessBundleDescriptor.TransformsEntry\x12\x66\n\x0cpcollections\x18\x03 \x03(\x0b\x32P.org.apache.beam.model.fn_execution.v1.ProcessBundleDescriptor.PcollectionsEntry\x12u\n\x14windowing_strategies\x18\x04 \x03(\x0b\x32W.org.apache.beam.model.fn_execution.v1.ProcessBundleDescriptor.WindowingStrategiesEntry\x12Z\n\x06\x63oders\x18\x05 \x03(\x0b\x32J.org.apache.beam.model.fn_execution.v1.ProcessBundleDescriptor.CodersEntry\x12\x66\n\x0c\x65nvironments\x18\x06 \x03(\x0b\x32P.org.apache.beam.model.fn_execution.v1.ProcessBundleDescriptor.EnvironmentsEntry\x12]\n\x1cstate_api_service_descriptor\x18\x07 \x01(\x0b\x32\x37.org.apache.beam.model.pipeline.v1.ApiServiceDescriptor\x12]\n\x1ctimer_api_service_descriptor\x18\x08 \x01(\x0b\x32\x37.org.apache.beam.model.pipeline.v1.ApiServiceDescriptor\x1a`\n\x0fTransformsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.org.apache.beam.model.pipeline.v1.PTransform:\x02\x38\x01\x1a\x63\n\x11PcollectionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b\x32..org.apache.beam.model.pipeline.v1.PCollection:\x02\x38\x01\x1ap\n\x18WindowingStrategiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0b\x32\x34.org.apache.beam.model.pipeline.v1.WindowingStrategy:\x02\x38\x01\x1aW\n\x0b\x43odersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.org.apache.beam.model.pipeline.v1.Coder:\x02\x38\x01\x1a\x63\n\x11\x45nvironmentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b\x32..org.apache.beam.model.pipeline.v1.Environment:\x02\x38\x01\"\xd3\x02\n\x11\x42undleApplication\x12\x14\n\x0ctransform_id\x18\x01 \x01(\t\x12\x10\n\x08input_id\x18\x02 \x01(\t\x12\x0f\n\x07\x65lement\x18\x03 \x01(\x0c\x12i\n\x11output_watermarks\x18\x04 \x03(\x0b\x32N.org.apache.beam.model.fn_execution.v1.BundleApplication.OutputWatermarksEntry\x12\x45\n\nis_bounded\x18\x05 \x01(\x0e\x32\x31.org.apache.beam.model.pipeline.v1.IsBounded.Enum\x1aS\n\x15OutputWatermarksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp:\x02\x38\x01\"\xa2\x01\n\x18\x44\x65layedBundleApplication\x12M\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32\x38.org.apache.beam.model.fn_execution.v1.BundleApplication\x12\x37\n\x14requested_time_delay\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x9a\x04\n\x14ProcessBundleRequest\x12$\n\x1cprocess_bundle_descriptor_id\x18\x01 \x01(\t\x12\\\n\x0c\x63\x61\x63he_tokens\x18\x02 \x03(\x0b\x32\x46.org.apache.beam.model.fn_execution.v1.ProcessBundleRequest.CacheToken\x12\x41\n\x08\x65lements\x18\x03 \x01(\x0b\x32/.org.apache.beam.model.fn_execution.v1.Elements\x1a\xba\x02\n\nCacheToken\x12\x66\n\nuser_state\x18\x01 \x01(\x0b\x32P.org.apache.beam.model.fn_execution.v1.ProcessBundleRequest.CacheToken.UserStateH\x00\x12\x66\n\nside_input\x18\x02 \x01(\x0b\x32P.org.apache.beam.model.fn_execution.v1.ProcessBundleRequest.CacheToken.SideInputH\x00\x12\r\n\x05token\x18\n \x01(\x0c\x1a\x0b\n\tUserState\x1a\x38\n\tSideInput\x12\x14\n\x0ctransform_id\x18\x01 \x01(\t\x12\x15\n\rside_input_id\x18\x02 \x01(\tB\x06\n\x04type\"\xc7\x03\n\x15ProcessBundleResponse\x12W\n\x0eresidual_roots\x18\x02 \x03(\x0b\x32?.org.apache.beam.model.fn_execution.v1.DelayedBundleApplication\x12K\n\x10monitoring_infos\x18\x03 \x03(\x0b\x32\x31.org.apache.beam.model.pipeline.v1.MonitoringInfo\x12\x1d\n\x15requires_finalization\x18\x04 \x01(\x08\x12i\n\x0fmonitoring_data\x18\x05 \x03(\x0b\x32P.org.apache.beam.model.fn_execution.v1.ProcessBundleResponse.MonitoringDataEntry\x12\x41\n\x08\x65lements\x18\x06 \x01(\x0b\x32/.org.apache.beam.model.fn_execution.v1.Elements\x1a\x35\n\x13MonitoringDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01J\x04\x08\x01\x10\x02\"6\n\x1cProcessBundleProgressRequest\x12\x16\n\x0einstruction_id\x18\x01 \x01(\t\"<\n\x1eMonitoringInfosMetadataRequest\x12\x1a\n\x12monitoring_info_id\x18\x01 \x03(\t\"\xa8\x02\n\x1dProcessBundleProgressResponse\x12K\n\x10monitoring_infos\x18\x03 \x03(\x0b\x32\x31.org.apache.beam.model.pipeline.v1.MonitoringInfo\x12q\n\x0fmonitoring_data\x18\x05 \x03(\x0b\x32X.org.apache.beam.model.fn_execution.v1.ProcessBundleProgressResponse.MonitoringDataEntry\x1a\x35\n\x13MonitoringDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01J\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x04\x10\x05\"\x80\x02\n\x1fMonitoringInfosMetadataResponse\x12s\n\x0fmonitoring_info\x18\x01 \x03(\x0b\x32Z.org.apache.beam.model.fn_execution.v1.MonitoringInfosMetadataResponse.MonitoringInfoEntry\x1ah\n\x13MonitoringInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b\x32\x31.org.apache.beam.model.pipeline.v1.MonitoringInfo:\x02\x38\x01\"\x95\x03\n\x19ProcessBundleSplitRequest\x12\x16\n\x0einstruction_id\x18\x01 \x01(\t\x12k\n\x0e\x64\x65sired_splits\x18\x03 \x03(\x0b\x32S.org.apache.beam.model.fn_execution.v1.ProcessBundleSplitRequest.DesiredSplitsEntry\x1am\n\x0c\x44\x65siredSplit\x12\x1d\n\x15\x66raction_of_remainder\x18\x01 \x01(\x01\x12\x1c\n\x14\x61llowed_split_points\x18\x03 \x03(\x03\x12 \n\x18\x65stimated_input_elements\x18\x02 \x01(\x03\x1a\x83\x01\n\x12\x44\x65siredSplitsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\\\n\x05value\x18\x02 \x01(\x0b\x32M.org.apache.beam.model.fn_execution.v1.ProcessBundleSplitRequest.DesiredSplit:\x02\x38\x01\"\x92\x03\n\x1aProcessBundleSplitResponse\x12O\n\rprimary_roots\x18\x01 \x03(\x0b\x32\x38.org.apache.beam.model.fn_execution.v1.BundleApplication\x12W\n\x0eresidual_roots\x18\x02 \x03(\x0b\x32?.org.apache.beam.model.fn_execution.v1.DelayedBundleApplication\x12\x66\n\x0e\x63hannel_splits\x18\x03 \x03(\x0b\x32N.org.apache.beam.model.fn_execution.v1.ProcessBundleSplitResponse.ChannelSplit\x1a\x62\n\x0c\x43hannelSplit\x12\x14\n\x0ctransform_id\x18\x01 \x01(\t\x12\x1c\n\x14last_primary_element\x18\x02 \x01(\x03\x12\x1e\n\x16\x66irst_residual_element\x18\x03 \x01(\x03\"/\n\x15\x46inalizeBundleRequest\x12\x16\n\x0einstruction_id\x18\x01 \x01(\t\"\x18\n\x16\x46inalizeBundleResponse\"\xe1\x02\n\x08\x45lements\x12\x42\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x34.org.apache.beam.model.fn_execution.v1.Elements.Data\x12\x46\n\x06timers\x18\x02 \x03(\x0b\x32\x36.org.apache.beam.model.fn_execution.v1.Elements.Timers\x1aW\n\x04\x44\x61ta\x12\x16\n\x0einstruction_id\x18\x01 \x01(\t\x12\x14\n\x0ctransform_id\x18\x02 \x01(\t\x12\x10\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x42\x02\x08\x01\x12\x0f\n\x07is_last\x18\x04 \x01(\x08\x1ap\n\x06Timers\x12\x16\n\x0einstruction_id\x18\x01 \x01(\t\x12\x14\n\x0ctransform_id\x18\x02 \x01(\t\x12\x17\n\x0ftimer_family_id\x18\x03 \x01(\t\x12\x0e\n\x06timers\x18\x04 \x01(\x0c\x12\x0f\n\x07is_last\x18\x05 \x01(\x08\"\xe3\x02\n\x0cStateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0einstruction_id\x18\x02 \x01(\t\x12\x42\n\tstate_key\x18\x03 \x01(\x0b\x32/.org.apache.beam.model.fn_execution.v1.StateKey\x12\x46\n\x03get\x18\xe8\x07 \x01(\x0b\x32\x36.org.apache.beam.model.fn_execution.v1.StateGetRequestH\x00\x12L\n\x06\x61ppend\x18\xe9\x07 \x01(\x0b\x32\x39.org.apache.beam.model.fn_execution.v1.StateAppendRequestH\x00\x12J\n\x05\x63lear\x18\xea\x07 \x01(\x0b\x32\x38.org.apache.beam.model.fn_execution.v1.StateClearRequestH\x00\x42\t\n\x07request\"\x9b\x02\n\rStateResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12G\n\x03get\x18\xe8\x07 \x01(\x0b\x32\x37.org.apache.beam.model.fn_execution.v1.StateGetResponseH\x00\x12M\n\x06\x61ppend\x18\xe9\x07 \x01(\x0b\x32:.org.apache.beam.model.fn_execution.v1.StateAppendResponseH\x00\x12K\n\x05\x63lear\x18\xea\x07 \x01(\x0b\x32\x39.org.apache.beam.model.fn_execution.v1.StateClearResponseH\x00\x42\n\n\x08response\"\xfb\t\n\x08StateKey\x12H\n\x06runner\x18\x01 \x01(\x0b\x32\x36.org.apache.beam.model.fn_execution.v1.StateKey.RunnerH\x00\x12`\n\x13multimap_side_input\x18\x02 \x01(\x0b\x32\x41.org.apache.beam.model.fn_execution.v1.StateKey.MultimapSideInputH\x00\x12V\n\x0e\x62\x61g_user_state\x18\x03 \x01(\x0b\x32<.org.apache.beam.model.fn_execution.v1.StateKey.BagUserStateH\x00\x12`\n\x13iterable_side_input\x18\x04 \x01(\x0b\x32\x41.org.apache.beam.model.fn_execution.v1.StateKey.IterableSideInputH\x00\x12i\n\x18multimap_keys_side_input\x18\x05 \x01(\x0b\x32\x45.org.apache.beam.model.fn_execution.v1.StateKey.MultimapKeysSideInputH\x00\x12i\n\x18multimap_keys_user_state\x18\x06 \x01(\x0b\x32\x45.org.apache.beam.model.fn_execution.v1.StateKey.MultimapKeysUserStateH\x00\x12`\n\x13multimap_user_state\x18\x07 \x01(\x0b\x32\x41.org.apache.beam.model.fn_execution.v1.StateKey.MultimapUserStateH\x00\x1a\x15\n\x06Runner\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x1aP\n\x11IterableSideInput\x12\x14\n\x0ctransform_id\x18\x01 \x01(\t\x12\x15\n\rside_input_id\x18\x02 \x01(\t\x12\x0e\n\x06window\x18\x03 \x01(\x0c\x1a]\n\x11MultimapSideInput\x12\x14\n\x0ctransform_id\x18\x01 \x01(\t\x12\x15\n\rside_input_id\x18\x02 \x01(\t\x12\x0e\n\x06window\x18\x03 \x01(\x0c\x12\x0b\n\x03key\x18\x04 \x01(\x0c\x1aT\n\x15MultimapKeysSideInput\x12\x14\n\x0ctransform_id\x18\x01 \x01(\t\x12\x15\n\rside_input_id\x18\x02 \x01(\t\x12\x0e\n\x06window\x18\x03 \x01(\x0c\x1aX\n\x0c\x42\x61gUserState\x12\x14\n\x0ctransform_id\x18\x01 \x01(\t\x12\x15\n\ruser_state_id\x18\x02 \x01(\t\x12\x0e\n\x06window\x18\x03 \x01(\x0c\x12\x0b\n\x03key\x18\x04 \x01(\x0c\x1a\x61\n\x15MultimapKeysUserState\x12\x14\n\x0ctransform_id\x18\x01 \x01(\t\x12\x15\n\ruser_state_id\x18\x02 \x01(\t\x12\x0e\n\x06window\x18\x03 \x01(\x0c\x12\x0b\n\x03key\x18\x04 \x01(\x0c\x1an\n\x11MultimapUserState\x12\x14\n\x0ctransform_id\x18\x01 \x01(\t\x12\x15\n\ruser_state_id\x18\x02 \x01(\t\x12\x0e\n\x06window\x18\x03 \x01(\x0c\x12\x0b\n\x03key\x18\x04 \x01(\x0c\x12\x0f\n\x07map_key\x18\x05 \x01(\x0c\x42\x06\n\x04type\"-\n\x0fStateGetRequest\x12\x1a\n\x12\x63ontinuation_token\x18\x01 \x01(\x0c\"<\n\x10StateGetResponse\x12\x1a\n\x12\x63ontinuation_token\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\"\n\x12StateAppendRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x15\n\x13StateAppendResponse\"\x13\n\x11StateClearRequest\"\x14\n\x12StateClearResponse\"\xee\x03\n\x08LogEntry\x12O\n\x08severity\x18\x01 \x01(\x0e\x32=.org.apache.beam.model.fn_execution.v1.LogEntry.Severity.Enum\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\r\n\x05trace\x18\x04 \x01(\t\x12\x16\n\x0einstruction_id\x18\x05 \x01(\t\x12\x14\n\x0ctransform_id\x18\x06 \x01(\t\x12\x14\n\x0clog_location\x18\x07 \x01(\t\x12\x0e\n\x06thread\x18\x08 \x01(\t\x12,\n\x0b\x63ustom_data\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\x1aL\n\x04List\x12\x44\n\x0blog_entries\x18\x01 \x03(\x0b\x32/.org.apache.beam.model.fn_execution.v1.LogEntry\x1ar\n\x08Severity\"f\n\x04\x45num\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\t\n\x05TRACE\x10\x01\x12\t\n\x05\x44\x45\x42UG\x10\x02\x12\x08\n\x04INFO\x10\x03\x12\n\n\x06NOTICE\x10\x04\x12\x08\n\x04WARN\x10\x05\x12\t\n\x05\x45RROR\x10\x06\x12\x0c\n\x08\x43RITICAL\x10\x07\"\x0c\n\nLogControl\"\xfc\x03\n\x12StartWorkerRequest\x12\x11\n\tworker_id\x18\x01 \x01(\t\x12Q\n\x10\x63ontrol_endpoint\x18\x02 \x01(\x0b\x32\x37.org.apache.beam.model.pipeline.v1.ApiServiceDescriptor\x12Q\n\x10logging_endpoint\x18\x03 \x01(\x0b\x32\x37.org.apache.beam.model.pipeline.v1.ApiServiceDescriptor\x12R\n\x11\x61rtifact_endpoint\x18\x04 \x01(\x0b\x32\x37.org.apache.beam.model.pipeline.v1.ApiServiceDescriptor\x12S\n\x12provision_endpoint\x18\x05 \x01(\x0b\x32\x37.org.apache.beam.model.pipeline.v1.ApiServiceDescriptor\x12U\n\x06params\x18\n \x03(\x0b\x32\x45.org.apache.beam.model.fn_execution.v1.StartWorkerRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"$\n\x13StartWorkerResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\"&\n\x11StopWorkerRequest\x12\x11\n\tworker_id\x18\x01 \x01(\t\"#\n\x12StopWorkerResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\"!\n\x13WorkerStatusRequest\x12\n\n\x02id\x18\x01 \x01(\t\"F\n\x14WorkerStatusResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x13\n\x0bstatus_info\x18\x03 \x01(\t2\xc3\x02\n\rBeamFnControl\x12\x86\x01\n\x07\x43ontrol\x12:.org.apache.beam.model.fn_execution.v1.InstructionResponse\x1a\x39.org.apache.beam.model.fn_execution.v1.InstructionRequest\"\x00(\x01\x30\x01\x12\xa8\x01\n\x1aGetProcessBundleDescriptor\x12H.org.apache.beam.model.fn_execution.v1.GetProcessBundleDescriptorRequest\x1a>.org.apache.beam.model.fn_execution.v1.ProcessBundleDescriptor\"\x00\x32|\n\nBeamFnData\x12n\n\x04\x44\x61ta\x12/.org.apache.beam.model.fn_execution.v1.Elements\x1a/.org.apache.beam.model.fn_execution.v1.Elements\"\x00(\x01\x30\x01\x32\x87\x01\n\x0b\x42\x65\x61mFnState\x12x\n\x05State\x12\x33.org.apache.beam.model.fn_execution.v1.StateRequest\x1a\x34.org.apache.beam.model.fn_execution.v1.StateResponse\"\x00(\x01\x30\x01\x32\x89\x01\n\rBeamFnLogging\x12x\n\x07Logging\x12\x34.org.apache.beam.model.fn_execution.v1.LogEntry.List\x1a\x31.org.apache.beam.model.fn_execution.v1.LogControl\"\x00(\x01\x30\x01\x32\xa9\x02\n\x18\x42\x65\x61mFnExternalWorkerPool\x12\x86\x01\n\x0bStartWorker\x12\x39.org.apache.beam.model.fn_execution.v1.StartWorkerRequest\x1a:.org.apache.beam.model.fn_execution.v1.StartWorkerResponse\"\x00\x12\x83\x01\n\nStopWorker\x12\x38.org.apache.beam.model.fn_execution.v1.StopWorkerRequest\x1a\x39.org.apache.beam.model.fn_execution.v1.StopWorkerResponse\"\x00\x32\xa4\x01\n\x12\x42\x65\x61mFnWorkerStatus\x12\x8d\x01\n\x0cWorkerStatus\x12;.org.apache.beam.model.fn_execution.v1.WorkerStatusResponse\x1a:.org.apache.beam.model.fn_execution.v1.WorkerStatusRequest\"\x00(\x01\x30\x01\x42\x81\x01\n$org.apache.beam.model.fnexecution.v1B\tBeamFnApiZNgithub.com/apache/beam/sdks/v2/go/pkg/beam/model/fnexecution_v1;fnexecution_v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'org.apache.beam.model.fn_execution.v1.beam_fn_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$org.apache.beam.model.fnexecution.v1B\tBeamFnApiZNgithub.com/apache/beam/sdks/v2/go/pkg/beam/model/fnexecution_v1;fnexecution_v1'
  _globals['_SAMPLEDATARESPONSE_ELEMENTSAMPLESENTRY']._loaded_options = None
  _globals['_SAMPLEDATARESPONSE_ELEMENTSAMPLESENTRY']._serialized_options = b'8\001'
  _globals['_HARNESSMONITORINGINFOSRESPONSE_MONITORINGDATAENTRY']._loaded_options = None
  _globals['_HARNESSMONITORINGINFOSRESPONSE_MONITORINGDATAENTRY']._serialized_options = b'8\001'
  _globals['_PROCESSBUNDLEDESCRIPTOR_TRANSFORMSENTRY']._loaded_options = None
  _globals['_PROCESSBUNDLEDESCRIPTOR_TRANSFORMSENTRY']._serialized_options = b'8\001'
  _globals['_PROCESSBUNDLEDESCRIPTOR_PCOLLECTIONSENTRY']._loaded_options = None
  _globals['_PROCESSBUNDLEDESCRIPTOR_PCOLLECTIONSENTRY']._serialized_options = b'8\001'
  _globals['_PROCESSBUNDLEDESCRIPTOR_WINDOWINGSTRATEGIESENTRY']._loaded_options = None
  _globals['_PROCESSBUNDLEDESCRIPTOR_WINDOWINGSTRATEGIESENTRY']._serialized_options = b'8\001'
  _globals['_PROCESSBUNDLEDESCRIPTOR_CODERSENTRY']._loaded_options = None
  _globals['_PROCESSBUNDLEDESCRIPTOR_CODERSENTRY']._serialized_options = b'8\001'
  _globals['_PROCESSBUNDLEDESCRIPTOR_ENVIRONMENTSENTRY']._loaded_options = None
  _globals['_PROCESSBUNDLEDESCRIPTOR_ENVIRONMENTSENTRY']._serialized_options = b'8\001'
  _globals['_BUNDLEAPPLICATION_OUTPUTWATERMARKSENTRY']._loaded_options = None
  _globals['_BUNDLEAPPLICATION_OUTPUTWATERMARKSENTRY']._serialized_options = b'8\001'
  _globals['_PROCESSBUNDLERESPONSE_MONITORINGDATAENTRY']._loaded_options = None
  _globals['_PROCESSBUNDLERESPONSE_MONITORINGDATAENTRY']._serialized_options = b'8\001'
  _globals['_PROCESSBUNDLEPROGRESSRESPONSE_MONITORINGDATAENTRY']._loaded_options = None
  _globals['_PROCESSBUNDLEPROGRESSRESPONSE_MONITORINGDATAENTRY']._serialized_options = b'8\001'
  _globals['_MONITORINGINFOSMETADATARESPONSE_MONITORINGINFOENTRY']._loaded_options = None
  _globals['_MONITORINGINFOSMETADATARESPONSE_MONITORINGINFOENTRY']._serialized_options = b'8\001'
  _globals['_PROCESSBUNDLESPLITREQUEST_DESIREDSPLITSENTRY']._loaded_options = None
  _globals['_PROCESSBUNDLESPLITREQUEST_DESIREDSPLITSENTRY']._serialized_options = b'8\001'
  _globals['_ELEMENTS_DATA'].fields_by_name['data']._loaded_options = None
  _globals['_ELEMENTS_DATA'].fields_by_name['data']._serialized_options = b'\010\001'
  _globals['_STARTWORKERREQUEST_PARAMSENTRY']._loaded_options = None
  _globals['_STARTWORKERREQUEST_PARAMSENTRY']._serialized_options = b'8\001'
  _globals['_REMOTEGRPCPORT']._serialized_start=384
  _globals['_REMOTEGRPCPORT']._serialized_end=507
  _globals['_GETPROCESSBUNDLEDESCRIPTORREQUEST']._serialized_start=509
  _globals['_GETPROCESSBUNDLEDESCRIPTORREQUEST']._serialized_end=582
  _globals['_INSTRUCTIONREQUEST']._serialized_start=585
  _globals['_INSTRUCTIONREQUEST']._serialized_end=1388
  _globals['_INSTRUCTIONRESPONSE']._serialized_start=1391
  _globals['_INSTRUCTIONRESPONSE']._serialized_end=2219
  _globals['_SAMPLEDATAREQUEST']._serialized_start=2221
  _globals['_SAMPLEDATAREQUEST']._serialized_end=2265
  _globals['_SAMPLEDELEMENT']._serialized_start=2267
  _globals['_SAMPLEDELEMENT']._serialized_end=2300
  _globals['_SAMPLEDATARESPONSE']._serialized_start=2303
  _globals['_SAMPLEDATARESPONSE']._serialized_end=2641
  _globals['_SAMPLEDATARESPONSE_ELEMENTLIST']._serialized_start=2429
  _globals['_SAMPLEDATARESPONSE_ELEMENTLIST']._serialized_end=2515
  _globals['_SAMPLEDATARESPONSE_ELEMENTSAMPLESENTRY']._serialized_start=2517
  _globals['_SAMPLEDATARESPONSE_ELEMENTSAMPLESENTRY']._serialized_end=2641
  _globals['_HARNESSMONITORINGINFOSREQUEST']._serialized_start=2643
  _globals['_HARNESSMONITORINGINFOSREQUEST']._serialized_end=2674
  _globals['_HARNESSMONITORINGINFOSRESPONSE']._serialized_start=2677
  _globals['_HARNESSMONITORINGINFOSRESPONSE']._serialized_end=2880
  _globals['_HARNESSMONITORINGINFOSRESPONSE_MONITORINGDATAENTRY']._serialized_start=2827
  _globals['_HARNESSMONITORINGINFOSRESPONSE_MONITORINGDATAENTRY']._serialized_end=2880
  _globals['_REGISTERREQUEST']._serialized_start=2882
  _globals['_REGISTERREQUEST']._serialized_end=2998
  _globals['_REGISTERRESPONSE']._serialized_start=3000
  _globals['_REGISTERRESPONSE']._serialized_end=3018
  _globals['_PROCESSBUNDLEDESCRIPTOR']._serialized_start=3021
  _globals['_PROCESSBUNDLEDESCRIPTOR']._serialized_end=4270
  _globals['_PROCESSBUNDLEDESCRIPTOR_TRANSFORMSENTRY']._serialized_start=3769
  _globals['_PROCESSBUNDLEDESCRIPTOR_TRANSFORMSENTRY']._serialized_end=3865
  _globals['_PROCESSBUNDLEDESCRIPTOR_PCOLLECTIONSENTRY']._serialized_start=3867
  _globals['_PROCESSBUNDLEDESCRIPTOR_PCOLLECTIONSENTRY']._serialized_end=3966
  _globals['_PROCESSBUNDLEDESCRIPTOR_WINDOWINGSTRATEGIESENTRY']._serialized_start=3968
  _globals['_PROCESSBUNDLEDESCRIPTOR_WINDOWINGSTRATEGIESENTRY']._serialized_end=4080
  _globals['_PROCESSBUNDLEDESCRIPTOR_CODERSENTRY']._serialized_start=4082
  _globals['_PROCESSBUNDLEDESCRIPTOR_CODERSENTRY']._serialized_end=4169
  _globals['_PROCESSBUNDLEDESCRIPTOR_ENVIRONMENTSENTRY']._serialized_start=4171
  _globals['_PROCESSBUNDLEDESCRIPTOR_ENVIRONMENTSENTRY']._serialized_end=4270
  _globals['_BUNDLEAPPLICATION']._serialized_start=4273
  _globals['_BUNDLEAPPLICATION']._serialized_end=4612
  _globals['_BUNDLEAPPLICATION_OUTPUTWATERMARKSENTRY']._serialized_start=4529
  _globals['_BUNDLEAPPLICATION_OUTPUTWATERMARKSENTRY']._serialized_end=4612
  _globals['_DELAYEDBUNDLEAPPLICATION']._serialized_start=4615
  _globals['_DELAYEDBUNDLEAPPLICATION']._serialized_end=4777
  _globals['_PROCESSBUNDLEREQUEST']._serialized_start=4780
  _globals['_PROCESSBUNDLEREQUEST']._serialized_end=5318
  _globals['_PROCESSBUNDLEREQUEST_CACHETOKEN']._serialized_start=5004
  _globals['_PROCESSBUNDLEREQUEST_CACHETOKEN']._serialized_end=5318
  _globals['_PROCESSBUNDLEREQUEST_CACHETOKEN_USERSTATE']._serialized_start=5241
  _globals['_PROCESSBUNDLEREQUEST_CACHETOKEN_USERSTATE']._serialized_end=5252
  _globals['_PROCESSBUNDLEREQUEST_CACHETOKEN_SIDEINPUT']._serialized_start=5254
  _globals['_PROCESSBUNDLEREQUEST_CACHETOKEN_SIDEINPUT']._serialized_end=5310
  _globals['_PROCESSBUNDLERESPONSE']._serialized_start=5321
  _globals['_PROCESSBUNDLERESPONSE']._serialized_end=5776
  _globals['_PROCESSBUNDLERESPONSE_MONITORINGDATAENTRY']._serialized_start=2827
  _globals['_PROCESSBUNDLERESPONSE_MONITORINGDATAENTRY']._serialized_end=2880
  _globals['_PROCESSBUNDLEPROGRESSREQUEST']._serialized_start=5778
  _globals['_PROCESSBUNDLEPROGRESSREQUEST']._serialized_end=5832
  _globals['_MONITORINGINFOSMETADATAREQUEST']._serialized_start=5834
  _globals['_MONITORINGINFOSMETADATAREQUEST']._serialized_end=5894
  _globals['_PROCESSBUNDLEPROGRESSRESPONSE']._serialized_start=5897
  _globals['_PROCESSBUNDLEPROGRESSRESPONSE']._serialized_end=6193
  _globals['_PROCESSBUNDLEPROGRESSRESPONSE_MONITORINGDATAENTRY']._serialized_start=2827
  _globals['_PROCESSBUNDLEPROGRESSRESPONSE_MONITORINGDATAENTRY']._serialized_end=2880
  _globals['_MONITORINGINFOSMETADATARESPONSE']._serialized_start=6196
  _globals['_MONITORINGINFOSMETADATARESPONSE']._serialized_end=6452
  _globals['_MONITORINGINFOSMETADATARESPONSE_MONITORINGINFOENTRY']._serialized_start=6348
  _globals['_MONITORINGINFOSMETADATARESPONSE_MONITORINGINFOENTRY']._serialized_end=6452
  _globals['_PROCESSBUNDLESPLITREQUEST']._serialized_start=6455
  _globals['_PROCESSBUNDLESPLITREQUEST']._serialized_end=6860
  _globals['_PROCESSBUNDLESPLITREQUEST_DESIREDSPLIT']._serialized_start=6617
  _globals['_PROCESSBUNDLESPLITREQUEST_DESIREDSPLIT']._serialized_end=6726
  _globals['_PROCESSBUNDLESPLITREQUEST_DESIREDSPLITSENTRY']._serialized_start=6729
  _globals['_PROCESSBUNDLESPLITREQUEST_DESIREDSPLITSENTRY']._serialized_end=6860
  _globals['_PROCESSBUNDLESPLITRESPONSE']._serialized_start=6863
  _globals['_PROCESSBUNDLESPLITRESPONSE']._serialized_end=7265
  _globals['_PROCESSBUNDLESPLITRESPONSE_CHANNELSPLIT']._serialized_start=7167
  _globals['_PROCESSBUNDLESPLITRESPONSE_CHANNELSPLIT']._serialized_end=7265
  _globals['_FINALIZEBUNDLEREQUEST']._serialized_start=7267
  _globals['_FINALIZEBUNDLEREQUEST']._serialized_end=7314
  _globals['_FINALIZEBUNDLERESPONSE']._serialized_start=7316
  _globals['_FINALIZEBUNDLERESPONSE']._serialized_end=7340
  _globals['_ELEMENTS']._serialized_start=7343
  _globals['_ELEMENTS']._serialized_end=7696
  _globals['_ELEMENTS_DATA']._serialized_start=7495
  _globals['_ELEMENTS_DATA']._serialized_end=7582
  _globals['_ELEMENTS_TIMERS']._serialized_start=7584
  _globals['_ELEMENTS_TIMERS']._serialized_end=7696
  _globals['_STATEREQUEST']._serialized_start=7699
  _globals['_STATEREQUEST']._serialized_end=8054
  _globals['_STATERESPONSE']._serialized_start=8057
  _globals['_STATERESPONSE']._serialized_end=8340
  _globals['_STATEKEY']._serialized_start=8343
  _globals['_STATEKEY']._serialized_end=9618
  _globals['_STATEKEY_RUNNER']._serialized_start=9025
  _globals['_STATEKEY_RUNNER']._serialized_end=9046
  _globals['_STATEKEY_ITERABLESIDEINPUT']._serialized_start=9048
  _globals['_STATEKEY_ITERABLESIDEINPUT']._serialized_end=9128
  _globals['_STATEKEY_MULTIMAPSIDEINPUT']._serialized_start=9130
  _globals['_STATEKEY_MULTIMAPSIDEINPUT']._serialized_end=9223
  _globals['_STATEKEY_MULTIMAPKEYSSIDEINPUT']._serialized_start=9225
  _globals['_STATEKEY_MULTIMAPKEYSSIDEINPUT']._serialized_end=9309
  _globals['_STATEKEY_BAGUSERSTATE']._serialized_start=9311
  _globals['_STATEKEY_BAGUSERSTATE']._serialized_end=9399
  _globals['_STATEKEY_MULTIMAPKEYSUSERSTATE']._serialized_start=9401
  _globals['_STATEKEY_MULTIMAPKEYSUSERSTATE']._serialized_end=9498
  _globals['_STATEKEY_MULTIMAPUSERSTATE']._serialized_start=9500
  _globals['_STATEKEY_MULTIMAPUSERSTATE']._serialized_end=9610
  _globals['_STATEGETREQUEST']._serialized_start=9620
  _globals['_STATEGETREQUEST']._serialized_end=9665
  _globals['_STATEGETRESPONSE']._serialized_start=9667
  _globals['_STATEGETRESPONSE']._serialized_end=9727
  _globals['_STATEAPPENDREQUEST']._serialized_start=9729
  _globals['_STATEAPPENDREQUEST']._serialized_end=9763
  _globals['_STATEAPPENDRESPONSE']._serialized_start=9765
  _globals['_STATEAPPENDRESPONSE']._serialized_end=9786
  _globals['_STATECLEARREQUEST']._serialized_start=9788
  _globals['_STATECLEARREQUEST']._serialized_end=9807
  _globals['_STATECLEARRESPONSE']._serialized_start=9809
  _globals['_STATECLEARRESPONSE']._serialized_end=9829
  _globals['_LOGENTRY']._serialized_start=9832
  _globals['_LOGENTRY']._serialized_end=10326
  _globals['_LOGENTRY_LIST']._serialized_start=10134
  _globals['_LOGENTRY_LIST']._serialized_end=10210
  _globals['_LOGENTRY_SEVERITY']._serialized_start=10212
  _globals['_LOGENTRY_SEVERITY']._serialized_end=10326
  _globals['_LOGENTRY_SEVERITY_ENUM']._serialized_start=10224
  _globals['_LOGENTRY_SEVERITY_ENUM']._serialized_end=10326
  _globals['_LOGCONTROL']._serialized_start=10328
  _globals['_LOGCONTROL']._serialized_end=10340
  _globals['_STARTWORKERREQUEST']._serialized_start=10343
  _globals['_STARTWORKERREQUEST']._serialized_end=10851
  _globals['_STARTWORKERREQUEST_PARAMSENTRY']._serialized_start=10806
  _globals['_STARTWORKERREQUEST_PARAMSENTRY']._serialized_end=10851
  _globals['_STARTWORKERRESPONSE']._serialized_start=10853
  _globals['_STARTWORKERRESPONSE']._serialized_end=10889
  _globals['_STOPWORKERREQUEST']._serialized_start=10891
  _globals['_STOPWORKERREQUEST']._serialized_end=10929
  _globals['_STOPWORKERRESPONSE']._serialized_start=10931
  _globals['_STOPWORKERRESPONSE']._serialized_end=10966
  _globals['_WORKERSTATUSREQUEST']._serialized_start=10968
  _globals['_WORKERSTATUSREQUEST']._serialized_end=11001
  _globals['_WORKERSTATUSRESPONSE']._serialized_start=11003
  _globals['_WORKERSTATUSRESPONSE']._serialized_end=11073
  _globals['_BEAMFNCONTROL']._serialized_start=11076
  _globals['_BEAMFNCONTROL']._serialized_end=11399
  _globals['_BEAMFNDATA']._serialized_start=11401
  _globals['_BEAMFNDATA']._serialized_end=11525
  _globals['_BEAMFNSTATE']._serialized_start=11528
  _globals['_BEAMFNSTATE']._serialized_end=11663
  _globals['_BEAMFNLOGGING']._serialized_start=11666
  _globals['_BEAMFNLOGGING']._serialized_end=11803
  _globals['_BEAMFNEXTERNALWORKERPOOL']._serialized_start=11806
  _globals['_BEAMFNEXTERNALWORKERPOOL']._serialized_end=12103
  _globals['_BEAMFNWORKERSTATUS']._serialized_start=12106
  _globals['_BEAMFNWORKERSTATUS']._serialized_end=12270
# @@protoc_insertion_point(module_scope)
