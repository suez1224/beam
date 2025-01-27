# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: org/apache/beam/model/job_management/v1/beam_job_api.proto
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
    'org/apache/beam/model/job_management/v1/beam_job_api.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...pipeline.v1 import beam_runner_api_pb2 as org_dot_apache_dot_beam_dot_model_dot_pipeline_dot_v1_dot_beam__runner__api__pb2
from ...pipeline.v1 import endpoints_pb2 as org_dot_apache_dot_beam_dot_model_dot_pipeline_dot_v1_dot_endpoints__pb2
from ...pipeline.v1 import metrics_pb2 as org_dot_apache_dot_beam_dot_model_dot_pipeline_dot_v1_dot_metrics__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:org/apache/beam/model/job_management/v1/beam_job_api.proto\x12\'org.apache.beam.model.job_management.v1\x1a\x37org/apache/beam/model/pipeline/v1/beam_runner_api.proto\x1a\x31org/apache/beam/model/pipeline/v1/endpoints.proto\x1a/org/apache/beam/model/pipeline/v1/metrics.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x97\x01\n\x11PrepareJobRequest\x12=\n\x08pipeline\x18\x01 \x01(\x0b\x32+.org.apache.beam.model.pipeline.v1.Pipeline\x12\x31\n\x10pipeline_options\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08job_name\x18\x03 \x01(\t\"\xa7\x01\n\x12PrepareJobResponse\x12\x16\n\x0epreparation_id\x18\x01 \x01(\t\x12Z\n\x19\x61rtifact_staging_endpoint\x18\x02 \x01(\x0b\x32\x37.org.apache.beam.model.pipeline.v1.ApiServiceDescriptor\x12\x1d\n\x15staging_session_token\x18\x03 \x01(\t\"@\n\rRunJobRequest\x12\x16\n\x0epreparation_id\x18\x01 \x01(\t\x12\x17\n\x0fretrieval_token\x18\x02 \x01(\t\" \n\x0eRunJobResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"\"\n\x10\x43\x61ncelJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"Z\n\x11\x43\x61ncelJobResponse\x12\x45\n\x05state\x18\x01 \x01(\x0e\x32\x36.org.apache.beam.model.job_management.v1.JobState.Enum\"\xa5\x01\n\x07JobInfo\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x10\n\x08job_name\x18\x02 \x01(\t\x12\x31\n\x10pipeline_options\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x45\n\x05state\x18\x04 \x01(\x0e\x32\x36.org.apache.beam.model.job_management.v1.JobState.Enum\"\x10\n\x0eGetJobsRequest\"U\n\x0fGetJobsResponse\x12\x42\n\x08job_info\x18\x01 \x03(\x0b\x32\x30.org.apache.beam.model.job_management.v1.JobInfo\"$\n\x12GetJobStateRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"\x85\x01\n\rJobStateEvent\x12\x45\n\x05state\x18\x01 \x01(\x0e\x32\x36.org.apache.beam.model.job_management.v1.JobState.Enum\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\'\n\x15GetJobPipelineRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"W\n\x16GetJobPipelineResponse\x12=\n\x08pipeline\x18\x01 \x01(\x0b\x32+.org.apache.beam.model.pipeline.v1.Pipeline\"$\n\x12JobMessagesRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"\xd1\x02\n\nJobMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\t\x12Y\n\nimportance\x18\x03 \x01(\x0e\x32\x45.org.apache.beam.model.job_management.v1.JobMessage.MessageImportance\x12\x14\n\x0cmessage_text\x18\x04 \x01(\t\"\xaf\x01\n\x11MessageImportance\x12\"\n\x1eMESSAGE_IMPORTANCE_UNSPECIFIED\x10\x00\x12\x15\n\x11JOB_MESSAGE_DEBUG\x10\x01\x12\x18\n\x14JOB_MESSAGE_DETAILED\x10\x02\x12\x15\n\x11JOB_MESSAGE_BASIC\x10\x03\x12\x17\n\x13JOB_MESSAGE_WARNING\x10\x04\x12\x15\n\x11JOB_MESSAGE_ERROR\x10\x05\"\xc4\x01\n\x13JobMessagesResponse\x12O\n\x10message_response\x18\x01 \x01(\x0b\x32\x33.org.apache.beam.model.job_management.v1.JobMessageH\x00\x12P\n\x0estate_response\x18\x02 \x01(\x0b\x32\x36.org.apache.beam.model.job_management.v1.JobStateEventH\x00\x42\n\n\x08response\"\xb7\x01\n\x08JobState\"\xaa\x01\n\x04\x45num\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07STOPPED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x08\n\x04\x44ONE\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\r\n\tCANCELLED\x10\x05\x12\x0b\n\x07UPDATED\x10\x06\x12\x0c\n\x08\x44RAINING\x10\x07\x12\x0b\n\x07\x44RAINED\x10\x08\x12\x0c\n\x08STARTING\x10\t\x12\x0e\n\nCANCELLING\x10\n\x12\x0c\n\x08UPDATING\x10\x0b\"&\n\x14GetJobMetricsRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"`\n\x15GetJobMetricsResponse\x12G\n\x07metrics\x18\x01 \x01(\x0b\x32\x36.org.apache.beam.model.job_management.v1.MetricResults\"\x9b\x01\n\rMetricResults\x12\x44\n\tattempted\x18\x01 \x03(\x0b\x32\x31.org.apache.beam.model.pipeline.v1.MonitoringInfo\x12\x44\n\tcommitted\x18\x02 \x03(\x0b\x32\x31.org.apache.beam.model.pipeline.v1.MonitoringInfo\" \n\x1e\x44\x65scribePipelineOptionsRequest\"e\n\x12PipelineOptionType\"O\n\x04\x45num\x12\n\n\x06STRING\x10\x00\x12\x0b\n\x07\x42OOLEAN\x10\x01\x12\x0b\n\x07INTEGER\x10\x02\x12\n\n\x06NUMBER\x10\x03\x12\t\n\x05\x41RRAY\x10\x04\x12\n\n\x06OBJECT\x10\x05\"\xb3\x01\n\x18PipelineOptionDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12N\n\x04type\x18\x02 \x01(\x0e\x32@.org.apache.beam.model.job_management.v1.PipelineOptionType.Enum\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x15\n\rdefault_value\x18\x04 \x01(\t\x12\r\n\x05group\x18\x05 \x01(\t\"u\n\x1f\x44\x65scribePipelineOptionsResponse\x12R\n\x07options\x18\x01 \x03(\x0b\x32\x41.org.apache.beam.model.job_management.v1.PipelineOptionDescriptor2\xf6\n\n\nJobService\x12\x82\x01\n\x07Prepare\x12:.org.apache.beam.model.job_management.v1.PrepareJobRequest\x1a;.org.apache.beam.model.job_management.v1.PrepareJobResponse\x12v\n\x03Run\x12\x36.org.apache.beam.model.job_management.v1.RunJobRequest\x1a\x37.org.apache.beam.model.job_management.v1.RunJobResponse\x12|\n\x07GetJobs\x12\x37.org.apache.beam.model.job_management.v1.GetJobsRequest\x1a\x38.org.apache.beam.model.job_management.v1.GetJobsResponse\x12\x7f\n\x08GetState\x12;.org.apache.beam.model.job_management.v1.GetJobStateRequest\x1a\x36.org.apache.beam.model.job_management.v1.JobStateEvent\x12\x8e\x01\n\x0bGetPipeline\x12>.org.apache.beam.model.job_management.v1.GetJobPipelineRequest\x1a?.org.apache.beam.model.job_management.v1.GetJobPipelineResponse\x12\x7f\n\x06\x43\x61ncel\x12\x39.org.apache.beam.model.job_management.v1.CancelJobRequest\x1a:.org.apache.beam.model.job_management.v1.CancelJobResponse\x12\x87\x01\n\x0eGetStateStream\x12;.org.apache.beam.model.job_management.v1.GetJobStateRequest\x1a\x36.org.apache.beam.model.job_management.v1.JobStateEvent0\x01\x12\x8f\x01\n\x10GetMessageStream\x12;.org.apache.beam.model.job_management.v1.JobMessagesRequest\x1a<.org.apache.beam.model.job_management.v1.JobMessagesResponse0\x01\x12\x8e\x01\n\rGetJobMetrics\x12=.org.apache.beam.model.job_management.v1.GetJobMetricsRequest\x1a>.org.apache.beam.model.job_management.v1.GetJobMetricsResponse\x12\xac\x01\n\x17\x44\x65scribePipelineOptions\x12G.org.apache.beam.model.job_management.v1.DescribePipelineOptionsRequest\x1aH.org.apache.beam.model.job_management.v1.DescribePipelineOptionsResponseB\x84\x01\n&org.apache.beam.model.jobmanagement.v1B\x06JobApiZRgithub.com/apache/beam/sdks/v2/go/pkg/beam/model/jobmanagement_v1;jobmanagement_v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'org.apache.beam.model.job_management.v1.beam_job_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&org.apache.beam.model.jobmanagement.v1B\006JobApiZRgithub.com/apache/beam/sdks/v2/go/pkg/beam/model/jobmanagement_v1;jobmanagement_v1'
  _globals['_PREPAREJOBREQUEST']._serialized_start=324
  _globals['_PREPAREJOBREQUEST']._serialized_end=475
  _globals['_PREPAREJOBRESPONSE']._serialized_start=478
  _globals['_PREPAREJOBRESPONSE']._serialized_end=645
  _globals['_RUNJOBREQUEST']._serialized_start=647
  _globals['_RUNJOBREQUEST']._serialized_end=711
  _globals['_RUNJOBRESPONSE']._serialized_start=713
  _globals['_RUNJOBRESPONSE']._serialized_end=745
  _globals['_CANCELJOBREQUEST']._serialized_start=747
  _globals['_CANCELJOBREQUEST']._serialized_end=781
  _globals['_CANCELJOBRESPONSE']._serialized_start=783
  _globals['_CANCELJOBRESPONSE']._serialized_end=873
  _globals['_JOBINFO']._serialized_start=876
  _globals['_JOBINFO']._serialized_end=1041
  _globals['_GETJOBSREQUEST']._serialized_start=1043
  _globals['_GETJOBSREQUEST']._serialized_end=1059
  _globals['_GETJOBSRESPONSE']._serialized_start=1061
  _globals['_GETJOBSRESPONSE']._serialized_end=1146
  _globals['_GETJOBSTATEREQUEST']._serialized_start=1148
  _globals['_GETJOBSTATEREQUEST']._serialized_end=1184
  _globals['_JOBSTATEEVENT']._serialized_start=1187
  _globals['_JOBSTATEEVENT']._serialized_end=1320
  _globals['_GETJOBPIPELINEREQUEST']._serialized_start=1322
  _globals['_GETJOBPIPELINEREQUEST']._serialized_end=1361
  _globals['_GETJOBPIPELINERESPONSE']._serialized_start=1363
  _globals['_GETJOBPIPELINERESPONSE']._serialized_end=1450
  _globals['_JOBMESSAGESREQUEST']._serialized_start=1452
  _globals['_JOBMESSAGESREQUEST']._serialized_end=1488
  _globals['_JOBMESSAGE']._serialized_start=1491
  _globals['_JOBMESSAGE']._serialized_end=1828
  _globals['_JOBMESSAGE_MESSAGEIMPORTANCE']._serialized_start=1653
  _globals['_JOBMESSAGE_MESSAGEIMPORTANCE']._serialized_end=1828
  _globals['_JOBMESSAGESRESPONSE']._serialized_start=1831
  _globals['_JOBMESSAGESRESPONSE']._serialized_end=2027
  _globals['_JOBSTATE']._serialized_start=2030
  _globals['_JOBSTATE']._serialized_end=2213
  _globals['_JOBSTATE_ENUM']._serialized_start=2043
  _globals['_JOBSTATE_ENUM']._serialized_end=2213
  _globals['_GETJOBMETRICSREQUEST']._serialized_start=2215
  _globals['_GETJOBMETRICSREQUEST']._serialized_end=2253
  _globals['_GETJOBMETRICSRESPONSE']._serialized_start=2255
  _globals['_GETJOBMETRICSRESPONSE']._serialized_end=2351
  _globals['_METRICRESULTS']._serialized_start=2354
  _globals['_METRICRESULTS']._serialized_end=2509
  _globals['_DESCRIBEPIPELINEOPTIONSREQUEST']._serialized_start=2511
  _globals['_DESCRIBEPIPELINEOPTIONSREQUEST']._serialized_end=2543
  _globals['_PIPELINEOPTIONTYPE']._serialized_start=2545
  _globals['_PIPELINEOPTIONTYPE']._serialized_end=2646
  _globals['_PIPELINEOPTIONTYPE_ENUM']._serialized_start=2567
  _globals['_PIPELINEOPTIONTYPE_ENUM']._serialized_end=2646
  _globals['_PIPELINEOPTIONDESCRIPTOR']._serialized_start=2649
  _globals['_PIPELINEOPTIONDESCRIPTOR']._serialized_end=2828
  _globals['_DESCRIBEPIPELINEOPTIONSRESPONSE']._serialized_start=2830
  _globals['_DESCRIBEPIPELINEOPTIONSRESPONSE']._serialized_end=2947
  _globals['_JOBSERVICE']._serialized_start=2950
  _globals['_JOBSERVICE']._serialized_end=4348
# @@protoc_insertion_point(module_scope)
