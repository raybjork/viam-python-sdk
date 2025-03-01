"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ShellRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DATA_IN_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    data_in: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., data_in: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['data_in', b'data_in', 'extra', b'extra', 'name', b'name']) -> None:
        ...
global___ShellRequest = ShellRequest

class ShellResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_OUT_FIELD_NUMBER: builtins.int
    DATA_ERR_FIELD_NUMBER: builtins.int
    EOF_FIELD_NUMBER: builtins.int
    data_out: builtins.str
    data_err: builtins.str
    eof: builtins.bool

    def __init__(self, *, data_out: builtins.str=..., data_err: builtins.str=..., eof: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['data_err', b'data_err', 'data_out', b'data_out', 'eof', b'eof']) -> None:
        ...
global___ShellResponse = ShellResponse