# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: proto/api/component/v1/board.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import proto.api.common.v1.common_pb2
import proto.api.component.v1.board_pb2


class BoardServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Status(self, stream: 'grpclib.server.Stream[proto.api.component.v1.board_pb2.BoardServiceStatusRequest, proto.api.component.v1.board_pb2.BoardServiceStatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetGPIO(self, stream: 'grpclib.server.Stream[proto.api.component.v1.board_pb2.BoardServiceSetGPIORequest, proto.api.component.v1.board_pb2.BoardServiceSetGPIOResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGPIO(self, stream: 'grpclib.server.Stream[proto.api.component.v1.board_pb2.BoardServiceGetGPIORequest, proto.api.component.v1.board_pb2.BoardServiceGetGPIOResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetPWM(self, stream: 'grpclib.server.Stream[proto.api.component.v1.board_pb2.BoardServiceSetPWMRequest, proto.api.component.v1.board_pb2.BoardServiceSetPWMResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetPWMFrequency(self, stream: 'grpclib.server.Stream[proto.api.component.v1.board_pb2.BoardServiceSetPWMFrequencyRequest, proto.api.component.v1.board_pb2.BoardServiceSetPWMFrequencyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ReadAnalogReader(self, stream: 'grpclib.server.Stream[proto.api.component.v1.board_pb2.BoardServiceReadAnalogReaderRequest, proto.api.component.v1.board_pb2.BoardServiceReadAnalogReaderResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDigitalInterruptValue(self, stream: 'grpclib.server.Stream[proto.api.component.v1.board_pb2.BoardServiceGetDigitalInterruptValueRequest, proto.api.component.v1.board_pb2.BoardServiceGetDigitalInterruptValueResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/proto.api.component.v1.BoardService/Status': grpclib.const.Handler(
                self.Status,
                grpclib.const.Cardinality.UNARY_UNARY,
                proto.api.component.v1.board_pb2.BoardServiceStatusRequest,
                proto.api.component.v1.board_pb2.BoardServiceStatusResponse,
            ),
            '/proto.api.component.v1.BoardService/SetGPIO': grpclib.const.Handler(
                self.SetGPIO,
                grpclib.const.Cardinality.UNARY_UNARY,
                proto.api.component.v1.board_pb2.BoardServiceSetGPIORequest,
                proto.api.component.v1.board_pb2.BoardServiceSetGPIOResponse,
            ),
            '/proto.api.component.v1.BoardService/GetGPIO': grpclib.const.Handler(
                self.GetGPIO,
                grpclib.const.Cardinality.UNARY_UNARY,
                proto.api.component.v1.board_pb2.BoardServiceGetGPIORequest,
                proto.api.component.v1.board_pb2.BoardServiceGetGPIOResponse,
            ),
            '/proto.api.component.v1.BoardService/SetPWM': grpclib.const.Handler(
                self.SetPWM,
                grpclib.const.Cardinality.UNARY_UNARY,
                proto.api.component.v1.board_pb2.BoardServiceSetPWMRequest,
                proto.api.component.v1.board_pb2.BoardServiceSetPWMResponse,
            ),
            '/proto.api.component.v1.BoardService/SetPWMFrequency': grpclib.const.Handler(
                self.SetPWMFrequency,
                grpclib.const.Cardinality.UNARY_UNARY,
                proto.api.component.v1.board_pb2.BoardServiceSetPWMFrequencyRequest,
                proto.api.component.v1.board_pb2.BoardServiceSetPWMFrequencyResponse,
            ),
            '/proto.api.component.v1.BoardService/ReadAnalogReader': grpclib.const.Handler(
                self.ReadAnalogReader,
                grpclib.const.Cardinality.UNARY_UNARY,
                proto.api.component.v1.board_pb2.BoardServiceReadAnalogReaderRequest,
                proto.api.component.v1.board_pb2.BoardServiceReadAnalogReaderResponse,
            ),
            '/proto.api.component.v1.BoardService/GetDigitalInterruptValue': grpclib.const.Handler(
                self.GetDigitalInterruptValue,
                grpclib.const.Cardinality.UNARY_UNARY,
                proto.api.component.v1.board_pb2.BoardServiceGetDigitalInterruptValueRequest,
                proto.api.component.v1.board_pb2.BoardServiceGetDigitalInterruptValueResponse,
            ),
        }


class BoardServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Status = grpclib.client.UnaryUnaryMethod(
            channel,
            '/proto.api.component.v1.BoardService/Status',
            proto.api.component.v1.board_pb2.BoardServiceStatusRequest,
            proto.api.component.v1.board_pb2.BoardServiceStatusResponse,
        )
        self.SetGPIO = grpclib.client.UnaryUnaryMethod(
            channel,
            '/proto.api.component.v1.BoardService/SetGPIO',
            proto.api.component.v1.board_pb2.BoardServiceSetGPIORequest,
            proto.api.component.v1.board_pb2.BoardServiceSetGPIOResponse,
        )
        self.GetGPIO = grpclib.client.UnaryUnaryMethod(
            channel,
            '/proto.api.component.v1.BoardService/GetGPIO',
            proto.api.component.v1.board_pb2.BoardServiceGetGPIORequest,
            proto.api.component.v1.board_pb2.BoardServiceGetGPIOResponse,
        )
        self.SetPWM = grpclib.client.UnaryUnaryMethod(
            channel,
            '/proto.api.component.v1.BoardService/SetPWM',
            proto.api.component.v1.board_pb2.BoardServiceSetPWMRequest,
            proto.api.component.v1.board_pb2.BoardServiceSetPWMResponse,
        )
        self.SetPWMFrequency = grpclib.client.UnaryUnaryMethod(
            channel,
            '/proto.api.component.v1.BoardService/SetPWMFrequency',
            proto.api.component.v1.board_pb2.BoardServiceSetPWMFrequencyRequest,
            proto.api.component.v1.board_pb2.BoardServiceSetPWMFrequencyResponse,
        )
        self.ReadAnalogReader = grpclib.client.UnaryUnaryMethod(
            channel,
            '/proto.api.component.v1.BoardService/ReadAnalogReader',
            proto.api.component.v1.board_pb2.BoardServiceReadAnalogReaderRequest,
            proto.api.component.v1.board_pb2.BoardServiceReadAnalogReaderResponse,
        )
        self.GetDigitalInterruptValue = grpclib.client.UnaryUnaryMethod(
            channel,
            '/proto.api.component.v1.BoardService/GetDigitalInterruptValue',
            proto.api.component.v1.board_pb2.BoardServiceGetDigitalInterruptValueRequest,
            proto.api.component.v1.board_pb2.BoardServiceGetDigitalInterruptValueResponse,
        )
