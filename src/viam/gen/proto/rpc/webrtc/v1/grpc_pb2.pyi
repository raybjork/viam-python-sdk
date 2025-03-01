"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class PacketMessage(google.protobuf.message.Message):
    """A PacketMessage is used to packetize large messages (> 64KiB) to be able to safely
    transmit over WebRTC data channels.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int
    EOM_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    eom: builtins.bool

    def __init__(self, *, data: builtins.bytes=..., eom: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['data', b'data', 'eom', b'eom']) -> None:
        ...
global___PacketMessage = PacketMessage

class Stream(google.protobuf.message.Message):
    """A Stream represents an instance of a gRPC stream between
    a client and a server.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: builtins.int

    def __init__(self, *, id: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id']) -> None:
        ...
global___Stream = Stream

class Request(google.protobuf.message.Message):
    """A Request is a frame coming from a client. It is always
    associated with a stream where the client assigns the stream
    identifier. Servers will drop frames where the stream identifier
    has no association (if a non-header frames are sent).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STREAM_FIELD_NUMBER: builtins.int
    HEADERS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    RST_STREAM_FIELD_NUMBER: builtins.int

    @property
    def stream(self) -> global___Stream:
        ...

    @property
    def headers(self) -> global___RequestHeaders:
        ...

    @property
    def message(self) -> global___RequestMessage:
        ...
    rst_stream: builtins.bool

    def __init__(self, *, stream: global___Stream | None=..., headers: global___RequestHeaders | None=..., message: global___RequestMessage | None=..., rst_stream: builtins.bool=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['headers', b'headers', 'message', b'message', 'rst_stream', b'rst_stream', 'stream', b'stream', 'type', b'type']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['headers', b'headers', 'message', b'message', 'rst_stream', b'rst_stream', 'stream', b'stream', 'type', b'type']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['type', b'type']) -> typing_extensions.Literal['headers', 'message', 'rst_stream'] | None:
        ...
global___Request = Request

class RequestHeaders(google.protobuf.message.Message):
    """RequestHeaders describe the unary or streaming call to make."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    METHOD_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    TIMEOUT_FIELD_NUMBER: builtins.int
    method: builtins.str

    @property
    def metadata(self) -> global___Metadata:
        ...

    @property
    def timeout(self) -> google.protobuf.duration_pb2.Duration:
        ...

    def __init__(self, *, method: builtins.str=..., metadata: global___Metadata | None=..., timeout: google.protobuf.duration_pb2.Duration | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['metadata', b'metadata', 'timeout', b'timeout']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['metadata', b'metadata', 'method', b'method', 'timeout', b'timeout']) -> None:
        ...
global___RequestHeaders = RequestHeaders

class RequestMessage(google.protobuf.message.Message):
    """A RequestMessage contains individual gRPC messages and a potential
    end-of-stream (EOS) marker.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HAS_MESSAGE_FIELD_NUMBER: builtins.int
    PACKET_MESSAGE_FIELD_NUMBER: builtins.int
    EOS_FIELD_NUMBER: builtins.int
    has_message: builtins.bool

    @property
    def packet_message(self) -> global___PacketMessage:
        ...
    eos: builtins.bool

    def __init__(self, *, has_message: builtins.bool=..., packet_message: global___PacketMessage | None=..., eos: builtins.bool=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['packet_message', b'packet_message']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['eos', b'eos', 'has_message', b'has_message', 'packet_message', b'packet_message']) -> None:
        ...
global___RequestMessage = RequestMessage

class Response(google.protobuf.message.Message):
    """A Response is a frame coming from a server. It is always
    associated with a stream where the client assigns the stream
    identifier. Clients will drop frames where the stream identifier
    has no association.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STREAM_FIELD_NUMBER: builtins.int
    HEADERS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    TRAILERS_FIELD_NUMBER: builtins.int

    @property
    def stream(self) -> global___Stream:
        ...

    @property
    def headers(self) -> global___ResponseHeaders:
        ...

    @property
    def message(self) -> global___ResponseMessage:
        ...

    @property
    def trailers(self) -> global___ResponseTrailers:
        ...

    def __init__(self, *, stream: global___Stream | None=..., headers: global___ResponseHeaders | None=..., message: global___ResponseMessage | None=..., trailers: global___ResponseTrailers | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['headers', b'headers', 'message', b'message', 'stream', b'stream', 'trailers', b'trailers', 'type', b'type']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['headers', b'headers', 'message', b'message', 'stream', b'stream', 'trailers', b'trailers', 'type', b'type']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['type', b'type']) -> typing_extensions.Literal['headers', 'message', 'trailers'] | None:
        ...
global___Response = Response

class ResponseHeaders(google.protobuf.message.Message):
    """ResponseHeaders contain custom metadata that are sent to the client
    before any message or trailers (unless only trailers are sent).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    METADATA_FIELD_NUMBER: builtins.int

    @property
    def metadata(self) -> global___Metadata:
        ...

    def __init__(self, *, metadata: global___Metadata | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['metadata', b'metadata']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['metadata', b'metadata']) -> None:
        ...
global___ResponseHeaders = ResponseHeaders

class ResponseMessage(google.protobuf.message.Message):
    """ResponseMessage contains the data of a response to a call."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PACKET_MESSAGE_FIELD_NUMBER: builtins.int

    @property
    def packet_message(self) -> global___PacketMessage:
        ...

    def __init__(self, *, packet_message: global___PacketMessage | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['packet_message', b'packet_message']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['packet_message', b'packet_message']) -> None:
        ...
global___ResponseMessage = ResponseMessage

class ResponseTrailers(google.protobuf.message.Message):
    """ResponseTrailers contain the status of a response and any custom metadata."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STATUS_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> google.rpc.status_pb2.Status:
        ...

    @property
    def metadata(self) -> global___Metadata:
        ...

    def __init__(self, *, status: google.rpc.status_pb2.Status | None=..., metadata: global___Metadata | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['metadata', b'metadata', 'status', b'status']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['metadata', b'metadata', 'status', b'status']) -> None:
        ...
global___ResponseTrailers = ResponseTrailers

class Strings(google.protobuf.message.Message):
    """Strings are a series of values."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUES_FIELD_NUMBER: builtins.int

    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...

    def __init__(self, *, values: collections.abc.Iterable[builtins.str] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['values', b'values']) -> None:
        ...
global___Strings = Strings

class Metadata(google.protobuf.message.Message):
    """Metadata is for custom key values provided by a client or server
    during a stream.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class MdEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> global___Strings:
            ...

        def __init__(self, *, key: builtins.str=..., value: global___Strings | None=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    MD_FIELD_NUMBER: builtins.int

    @property
    def md(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___Strings]:
        ...

    def __init__(self, *, md: collections.abc.Mapping[builtins.str, global___Strings] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['md', b'md']) -> None:
        ...
global___Metadata = Metadata