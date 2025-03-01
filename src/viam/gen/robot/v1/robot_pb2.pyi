"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
from ... import common
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PeerConnectionType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PeerConnectionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PeerConnectionType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PEER_CONNECTION_TYPE_UNSPECIFIED: _PeerConnectionType.ValueType
    PEER_CONNECTION_TYPE_GRPC: _PeerConnectionType.ValueType
    PEER_CONNECTION_TYPE_WEBRTC: _PeerConnectionType.ValueType

class PeerConnectionType(_PeerConnectionType, metaclass=_PeerConnectionTypeEnumTypeWrapper):
    ...
PEER_CONNECTION_TYPE_UNSPECIFIED: PeerConnectionType.ValueType
PEER_CONNECTION_TYPE_GRPC: PeerConnectionType.ValueType
PEER_CONNECTION_TYPE_WEBRTC: PeerConnectionType.ValueType
global___PeerConnectionType = PeerConnectionType

class FrameSystemConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    POSE_IN_PARENT_FRAME_FIELD_NUMBER: builtins.int
    MODEL_JSON_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def pose_in_parent_frame(self) -> common.v1.common_pb2.PoseInFrame:
        ...
    model_json: builtins.bytes

    def __init__(self, *, name: builtins.str=..., pose_in_parent_frame: common.v1.common_pb2.PoseInFrame | None=..., model_json: builtins.bytes=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose_in_parent_frame', b'pose_in_parent_frame']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['model_json', b'model_json', 'name', b'name', 'pose_in_parent_frame', b'pose_in_parent_frame']) -> None:
        ...
global___FrameSystemConfig = FrameSystemConfig

class FrameSystemConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUPPLEMENTAL_TRANSFORMS_FIELD_NUMBER: builtins.int

    @property
    def supplemental_transforms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.Transform]:
        """pose information on any additional reference frames that are needed
        to supplement the robot's frame system
        """

    def __init__(self, *, supplemental_transforms: collections.abc.Iterable[common.v1.common_pb2.Transform] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['supplemental_transforms', b'supplemental_transforms']) -> None:
        ...
global___FrameSystemConfigRequest = FrameSystemConfigRequest

class FrameSystemConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FRAME_SYSTEM_CONFIGS_FIELD_NUMBER: builtins.int

    @property
    def frame_system_configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FrameSystemConfig]:
        ...

    def __init__(self, *, frame_system_configs: collections.abc.Iterable[global___FrameSystemConfig] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['frame_system_configs', b'frame_system_configs']) -> None:
        ...
global___FrameSystemConfigResponse = FrameSystemConfigResponse

class TransformPoseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SOURCE_FIELD_NUMBER: builtins.int
    DESTINATION_FIELD_NUMBER: builtins.int
    SUPPLEMENTAL_TRANSFORMS_FIELD_NUMBER: builtins.int

    @property
    def source(self) -> common.v1.common_pb2.PoseInFrame:
        """the original pose to transform along with the reference frame in
        which it was observed
        """
    destination: builtins.str
    'the reference frame into which the source pose should be transformed,\n    if unset this defaults to the "world" reference frame\n    '

    @property
    def supplemental_transforms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.Transform]:
        """pose information on any additional reference frames that are needed
        to perform the transform
        """

    def __init__(self, *, source: common.v1.common_pb2.PoseInFrame | None=..., destination: builtins.str=..., supplemental_transforms: collections.abc.Iterable[common.v1.common_pb2.Transform] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['source', b'source']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['destination', b'destination', 'source', b'source', 'supplemental_transforms', b'supplemental_transforms']) -> None:
        ...
global___TransformPoseRequest = TransformPoseRequest

class TransformPoseResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSE_FIELD_NUMBER: builtins.int

    @property
    def pose(self) -> common.v1.common_pb2.PoseInFrame:
        ...

    def __init__(self, *, pose: common.v1.common_pb2.PoseInFrame | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> None:
        ...
global___TransformPoseResponse = TransformPoseResponse

class ResourceNamesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___ResourceNamesRequest = ResourceNamesRequest

class ResourceNamesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCES_FIELD_NUMBER: builtins.int

    @property
    def resources(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.ResourceName]:
        ...

    def __init__(self, *, resources: collections.abc.Iterable[common.v1.common_pb2.ResourceName] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['resources', b'resources']) -> None:
        ...
global___ResourceNamesResponse = ResourceNamesResponse

class ResourceRPCSubtype(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUBTYPE_FIELD_NUMBER: builtins.int
    PROTO_SERVICE_FIELD_NUMBER: builtins.int

    @property
    def subtype(self) -> common.v1.common_pb2.ResourceName:
        ...
    proto_service: builtins.str

    def __init__(self, *, subtype: common.v1.common_pb2.ResourceName | None=..., proto_service: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['subtype', b'subtype']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['proto_service', b'proto_service', 'subtype', b'subtype']) -> None:
        ...
global___ResourceRPCSubtype = ResourceRPCSubtype

class ResourceRPCSubtypesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___ResourceRPCSubtypesRequest = ResourceRPCSubtypesRequest

class ResourceRPCSubtypesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_RPC_SUBTYPES_FIELD_NUMBER: builtins.int

    @property
    def resource_rpc_subtypes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ResourceRPCSubtype]:
        ...

    def __init__(self, *, resource_rpc_subtypes: collections.abc.Iterable[global___ResourceRPCSubtype] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['resource_rpc_subtypes', b'resource_rpc_subtypes']) -> None:
        ...
global___ResourceRPCSubtypesResponse = ResourceRPCSubtypesResponse

class Operation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    METHOD_FIELD_NUMBER: builtins.int
    ARGUMENTS_FIELD_NUMBER: builtins.int
    STARTED_FIELD_NUMBER: builtins.int
    SESSION_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    method: builtins.str

    @property
    def arguments(self) -> google.protobuf.struct_pb2.Struct:
        ...

    @property
    def started(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...
    session_id: builtins.str

    def __init__(self, *, id: builtins.str=..., method: builtins.str=..., arguments: google.protobuf.struct_pb2.Struct | None=..., started: google.protobuf.timestamp_pb2.Timestamp | None=..., session_id: builtins.str | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_session_id', b'_session_id', 'arguments', b'arguments', 'session_id', b'session_id', 'started', b'started']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_session_id', b'_session_id', 'arguments', b'arguments', 'id', b'id', 'method', b'method', 'session_id', b'session_id', 'started', b'started']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_session_id', b'_session_id']) -> typing_extensions.Literal['session_id'] | None:
        ...
global___Operation = Operation

class GetOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___GetOperationsRequest = GetOperationsRequest

class GetOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int

    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Operation]:
        ...

    def __init__(self, *, operations: collections.abc.Iterable[global___Operation] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['operations', b'operations']) -> None:
        ...
global___GetOperationsResponse = GetOperationsResponse

class CancelOperationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: builtins.str

    def __init__(self, *, id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id']) -> None:
        ...
global___CancelOperationRequest = CancelOperationRequest

class CancelOperationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___CancelOperationResponse = CancelOperationResponse

class BlockForOperationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: builtins.str

    def __init__(self, *, id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id']) -> None:
        ...
global___BlockForOperationRequest = BlockForOperationRequest

class BlockForOperationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___BlockForOperationResponse = BlockForOperationResponse

class PeerConnectionInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    REMOTE_ADDRESS_FIELD_NUMBER: builtins.int
    LOCAL_ADDRESS_FIELD_NUMBER: builtins.int
    type: global___PeerConnectionType.ValueType
    remote_address: builtins.str
    local_address: builtins.str

    def __init__(self, *, type: global___PeerConnectionType.ValueType=..., remote_address: builtins.str | None=..., local_address: builtins.str | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_local_address', b'_local_address', '_remote_address', b'_remote_address', 'local_address', b'local_address', 'remote_address', b'remote_address']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_local_address', b'_local_address', '_remote_address', b'_remote_address', 'local_address', b'local_address', 'remote_address', b'remote_address', 'type', b'type']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_local_address', b'_local_address']) -> typing_extensions.Literal['local_address'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_remote_address', b'_remote_address']) -> typing_extensions.Literal['remote_address'] | None:
        ...
global___PeerConnectionInfo = PeerConnectionInfo

class Session(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    PEER_CONNECTION_INFO_FIELD_NUMBER: builtins.int
    id: builtins.str

    @property
    def peer_connection_info(self) -> global___PeerConnectionInfo:
        ...

    def __init__(self, *, id: builtins.str=..., peer_connection_info: global___PeerConnectionInfo | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_peer_connection_info', b'_peer_connection_info', 'peer_connection_info', b'peer_connection_info']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_peer_connection_info', b'_peer_connection_info', 'id', b'id', 'peer_connection_info', b'peer_connection_info']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_peer_connection_info', b'_peer_connection_info']) -> typing_extensions.Literal['peer_connection_info'] | None:
        ...
global___Session = Session

class GetSessionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___GetSessionsRequest = GetSessionsRequest

class GetSessionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SESSIONS_FIELD_NUMBER: builtins.int

    @property
    def sessions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Session]:
        ...

    def __init__(self, *, sessions: collections.abc.Iterable[global___Session] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['sessions', b'sessions']) -> None:
        ...
global___GetSessionsResponse = GetSessionsResponse

class DiscoveryQuery(google.protobuf.message.Message):
    """Discovery"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUBTYPE_FIELD_NUMBER: builtins.int
    MODEL_FIELD_NUMBER: builtins.int
    subtype: builtins.str
    model: builtins.str

    def __init__(self, *, subtype: builtins.str=..., model: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['model', b'model', 'subtype', b'subtype']) -> None:
        ...
global___DiscoveryQuery = DiscoveryQuery

class Discovery(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    QUERY_FIELD_NUMBER: builtins.int
    RESULTS_FIELD_NUMBER: builtins.int

    @property
    def query(self) -> global___DiscoveryQuery:
        ...

    @property
    def results(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, query: global___DiscoveryQuery | None=..., results: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['query', b'query', 'results', b'results']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['query', b'query', 'results', b'results']) -> None:
        ...
global___Discovery = Discovery

class DiscoverComponentsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    QUERIES_FIELD_NUMBER: builtins.int

    @property
    def queries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DiscoveryQuery]:
        ...

    def __init__(self, *, queries: collections.abc.Iterable[global___DiscoveryQuery] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['queries', b'queries']) -> None:
        ...
global___DiscoverComponentsRequest = DiscoverComponentsRequest

class DiscoverComponentsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISCOVERY_FIELD_NUMBER: builtins.int

    @property
    def discovery(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Discovery]:
        ...

    def __init__(self, *, discovery: collections.abc.Iterable[global___Discovery] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['discovery', b'discovery']) -> None:
        ...
global___DiscoverComponentsResponse = DiscoverComponentsResponse

class Status(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int

    @property
    def name(self) -> common.v1.common_pb2.ResourceName:
        ...

    @property
    def status(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, name: common.v1.common_pb2.ResourceName | None=..., status: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['name', b'name', 'status', b'status']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name', 'status', b'status']) -> None:
        ...
global___Status = Status

class GetStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_NAMES_FIELD_NUMBER: builtins.int

    @property
    def resource_names(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.ResourceName]:
        ...

    def __init__(self, *, resource_names: collections.abc.Iterable[common.v1.common_pb2.ResourceName] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['resource_names', b'resource_names']) -> None:
        ...
global___GetStatusRequest = GetStatusRequest

class GetStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STATUS_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Status]:
        ...

    def __init__(self, *, status: collections.abc.Iterable[global___Status] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['status', b'status']) -> None:
        ...
global___GetStatusResponse = GetStatusResponse

class StreamStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_NAMES_FIELD_NUMBER: builtins.int
    EVERY_FIELD_NUMBER: builtins.int

    @property
    def resource_names(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.ResourceName]:
        ...

    @property
    def every(self) -> google.protobuf.duration_pb2.Duration:
        """how often to send a new status."""

    def __init__(self, *, resource_names: collections.abc.Iterable[common.v1.common_pb2.ResourceName] | None=..., every: google.protobuf.duration_pb2.Duration | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['every', b'every']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['every', b'every', 'resource_names', b'resource_names']) -> None:
        ...
global___StreamStatusRequest = StreamStatusRequest

class StreamStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STATUS_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Status]:
        ...

    def __init__(self, *, status: collections.abc.Iterable[global___Status] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['status', b'status']) -> None:
        ...
global___StreamStatusResponse = StreamStatusResponse

class StopExtraParameters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int

    @property
    def name(self) -> common.v1.common_pb2.ResourceName:
        ...

    @property
    def params(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, name: common.v1.common_pb2.ResourceName | None=..., params: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['name', b'name', 'params', b'params']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name', 'params', b'params']) -> None:
        ...
global___StopExtraParameters = StopExtraParameters

class StopAllRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EXTRA_FIELD_NUMBER: builtins.int

    @property
    def extra(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StopExtraParameters]:
        ...

    def __init__(self, *, extra: collections.abc.Iterable[global___StopExtraParameters] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> None:
        ...
global___StopAllRequest = StopAllRequest

class StopAllResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___StopAllResponse = StopAllResponse

class StartSessionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESUME_FIELD_NUMBER: builtins.int
    resume: builtins.str
    'resume can be used to attempt to continue a stream after a disconnection event. If\n    a session is not found, a new one will be created and returned.\n    '

    def __init__(self, *, resume: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['resume', b'resume']) -> None:
        ...
global___StartSessionRequest = StartSessionRequest

class StartSessionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    HEARTBEAT_WINDOW_FIELD_NUMBER: builtins.int
    id: builtins.str

    @property
    def heartbeat_window(self) -> google.protobuf.duration_pb2.Duration:
        ...

    def __init__(self, *, id: builtins.str=..., heartbeat_window: google.protobuf.duration_pb2.Duration | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['heartbeat_window', b'heartbeat_window']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['heartbeat_window', b'heartbeat_window', 'id', b'id']) -> None:
        ...
global___StartSessionResponse = StartSessionResponse

class SendSessionHeartbeatRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: builtins.str

    def __init__(self, *, id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id']) -> None:
        ...
global___SendSessionHeartbeatRequest = SendSessionHeartbeatRequest

class SendSessionHeartbeatResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SendSessionHeartbeatResponse = SendSessionHeartbeatResponse