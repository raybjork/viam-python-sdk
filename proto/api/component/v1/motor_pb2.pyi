"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class MotorServiceSetPowerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    POWER_PCT_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a motor"""

    power_pct: builtins.float = ...
    """Percentage of motor's power, between -1 and 1"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        power_pct : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","power_pct",b"power_pct"]) -> None: ...
global___MotorServiceSetPowerRequest = MotorServiceSetPowerRequest

class MotorServiceSetPowerResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MotorServiceSetPowerResponse = MotorServiceSetPowerResponse

class MotorServiceGoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    POWER_PCT_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a motor"""

    power_pct: builtins.float = ...
    """Percentage of motor's power, between -1 and 1"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        power_pct : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","power_pct",b"power_pct"]) -> None: ...
global___MotorServiceGoRequest = MotorServiceGoRequest

class MotorServiceGoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MotorServiceGoResponse = MotorServiceGoResponse

class MotorServiceGoForRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    RPM_FIELD_NUMBER: builtins.int
    REVOLUTIONS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a motor"""

    rpm: builtins.float = ...
    """Speed of motor travel in rotations per minute"""

    revolutions: builtins.float = ...
    """Number of revolutions relative to motor's start position"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        rpm : builtins.float = ...,
        revolutions : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","revolutions",b"revolutions","rpm",b"rpm"]) -> None: ...
global___MotorServiceGoForRequest = MotorServiceGoForRequest

class MotorServiceGoForResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MotorServiceGoForResponse = MotorServiceGoForResponse

class MotorServiceGoToRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    RPM_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a motor"""

    rpm: builtins.float = ...
    """Speed of motor travel in rotations per minute"""

    position: builtins.float = ...
    """Number of revolutions relative to motor's home home/zero"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        rpm : builtins.float = ...,
        position : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","position",b"position","rpm",b"rpm"]) -> None: ...
global___MotorServiceGoToRequest = MotorServiceGoToRequest

class MotorServiceGoToResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MotorServiceGoToResponse = MotorServiceGoToResponse

class MotorServiceGoTillStopRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    RPM_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a motor"""

    rpm: builtins.float = ...
    """Speed of motor travel in rotations per minute"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        rpm : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","rpm",b"rpm"]) -> None: ...
global___MotorServiceGoTillStopRequest = MotorServiceGoTillStopRequest

class MotorServiceGoTillStopResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MotorServiceGoTillStopResponse = MotorServiceGoTillStopResponse

class MotorServiceResetZeroPositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a motor"""

    offset: builtins.float = ...
    """Motor position"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        offset : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","offset",b"offset"]) -> None: ...
global___MotorServiceResetZeroPositionRequest = MotorServiceResetZeroPositionRequest

class MotorServiceResetZeroPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MotorServiceResetZeroPositionResponse = MotorServiceResetZeroPositionResponse

class MotorServicePositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a motor"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___MotorServicePositionRequest = MotorServicePositionRequest

class MotorServicePositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    POSITION_FIELD_NUMBER: builtins.int
    position: builtins.float = ...
    """Current position of the motor relative to its home"""

    def __init__(self,
        *,
        position : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["position",b"position"]) -> None: ...
global___MotorServicePositionResponse = MotorServicePositionResponse

class MotorServicePositionSupportedRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a motor"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___MotorServicePositionSupportedRequest = MotorServicePositionSupportedRequest

class MotorServicePositionSupportedResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUPPORTED_FIELD_NUMBER: builtins.int
    supported: builtins.bool = ...
    """Returns true if the motor supports reporting its position"""

    def __init__(self,
        *,
        supported : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["supported",b"supported"]) -> None: ...
global___MotorServicePositionSupportedResponse = MotorServicePositionSupportedResponse

class MotorServiceStopRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a motor"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___MotorServiceStopRequest = MotorServiceStopRequest

class MotorServiceStopResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MotorServiceStopResponse = MotorServiceStopResponse

class MotorServiceIsOnRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a motor"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___MotorServiceIsOnRequest = MotorServiceIsOnRequest

class MotorServiceIsOnResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IS_ON_FIELD_NUMBER: builtins.int
    is_on: builtins.bool = ...
    def __init__(self,
        *,
        is_on : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["is_on",b"is_on"]) -> None: ...
global___MotorServiceIsOnResponse = MotorServiceIsOnResponse
