from typing import cast

import pytest
from grpclib import GRPCError
from grpclib.testing import ChannelFor

from viam.components.board import Board, BoardClient
from viam.components.board.service import BoardService
from viam.components.generic.service import GenericService
from viam.components.resource_manager import ResourceManager
from viam.errors import ComponentNotFoundError
from viam.proto.common import AnalogStatus, BoardStatus, DigitalInterruptStatus
from viam.proto.component.board import (
    BoardServiceStub,
    GetDigitalInterruptValueRequest,
    GetDigitalInterruptValueResponse,
    GetGPIORequest,
    GetGPIOResponse,
    PWMFrequencyRequest,
    PWMFrequencyResponse,
    PWMRequest,
    PWMResponse,
    ReadAnalogReaderRequest,
    ReadAnalogReaderResponse,
    SetGPIORequest,
    SetPWMFrequencyRequest,
    SetPWMRequest,
    StatusRequest,
    StatusResponse,
)
from viam.utils import dict_to_struct

from . import loose_approx
from .mocks.components import (
    MockAnalogReader,
    MockBoard,
    MockDigitalInterrupt,
    MockGPIOPin,
)


@pytest.fixture(scope="function")
def board() -> MockBoard:
    return MockBoard(
        name="board",
        analog_readers={
            "reader1": MockAnalogReader("reader1", 3),
        },
        digital_interrupts={
            "interrupt1": MockDigitalInterrupt("interrupt1"),
        },
        gpio_pins={"pin1": MockGPIOPin("pin1")},
    )


@pytest.fixture(scope="function")
def service(board: MockBoard) -> BoardService:
    manager = ResourceManager([board])
    return BoardService(manager)


@pytest.fixture(scope="function")
def generic_service(board: MockBoard) -> GenericService:
    manager = ResourceManager([board])
    return GenericService(manager)


class TestBoard:
    @pytest.mark.asyncio
    async def test_analog_reader_by_name(self, board: MockBoard):
        with pytest.raises(ComponentNotFoundError):
            await board.analog_reader_by_name("does not exist")

        reader = await board.analog_reader_by_name("reader1")
        assert reader.name == "reader1"

    @pytest.mark.asyncio
    async def test_digital_interrupt_by_name(self, board: MockBoard):
        with pytest.raises(ComponentNotFoundError):
            await board.digital_interrupt_by_name("does not exist")

        interrupt = await board.digital_interrupt_by_name("interrupt1")
        assert interrupt.name == "interrupt1"

    @pytest.mark.asyncio
    async def test_gpio_pin_by_name(self, board: MockBoard):
        with pytest.raises(ComponentNotFoundError):
            await board.digital_interrupt_by_name("does not exist")

        pin = await board.gpio_pin_by_name("pin1")
        assert pin.name == "pin1"

    @pytest.mark.asyncio
    async def test_analog_reader_names(self, board: MockBoard):
        names = await board.analog_reader_names()
        assert names == ["reader1"]

    @pytest.mark.asyncio
    async def test_digital_interrupt_names(self, board: MockBoard):
        names = await board.digital_interrupt_names()
        assert names == ["interrupt1"]

    @pytest.mark.asyncio
    async def test_status(self, board: MockBoard):
        extra = {"foo": "bar", "baz": [1, 2, 3]}
        status = await board.status(extra=extra, timeout=1.82)
        assert status == BoardStatus(
            analogs={"reader1": AnalogStatus(value=3)},
            digital_interrupts={"interrupt1": DigitalInterruptStatus(value=0)},
        )
        assert board.extra == extra
        assert board.timeout == loose_approx(1.82)

    @pytest.mark.asyncio
    async def test_model_attributes(self, board: MockBoard):
        attrs = await board.model_attributes()
        assert attrs == Board.Attributes(remote=True)

    @pytest.mark.asyncio
    async def test_do(self, board: MockBoard):
        with pytest.raises(NotImplementedError):
            await board.do_command({"command": "args"})


class TestService:
    @pytest.mark.asyncio
    async def test_read_analog_reader(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            with pytest.raises(GRPCError, match=r".*Status.NOT_FOUND.*"):
                request = ReadAnalogReaderRequest(board_name=board.name, analog_reader_name="dne")
                await client.ReadAnalogReader(request)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = ReadAnalogReaderRequest(board_name=board.name, analog_reader_name="reader1", extra=dict_to_struct(extra))
            response: ReadAnalogReaderResponse = await client.ReadAnalogReader(request, timeout=4.4)
            assert response.value == 3

            reader = cast(MockAnalogReader, board.analog_readers["reader1"])
            assert reader.extra == extra
            assert reader.timeout == loose_approx(4.4)

    @pytest.mark.asyncio
    async def test_get_digital_interrupt_value(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            with pytest.raises(GRPCError, match=r".*Status.NOT_FOUND.*"):
                request = GetDigitalInterruptValueRequest(board_name=board.name, digital_interrupt_name="dne")
                await client.GetDigitalInterruptValue(request)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = GetDigitalInterruptValueRequest(
                board_name=board.name, digital_interrupt_name="interrupt1", extra=dict_to_struct(extra)
            )
            response: GetDigitalInterruptValueResponse = await client.GetDigitalInterruptValue(request, timeout=18.2)
            assert response.value == 0

            interrupt = cast(MockDigitalInterrupt, board.digital_interrupts["interrupt1"])
            assert interrupt.extra == extra
            assert interrupt.timeout == loose_approx(18.2)

    @pytest.mark.asyncio
    async def test_set_gpio(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = SetGPIORequest(name=board.name, pin="pin1", high=True, extra=dict_to_struct(extra))
            await client.SetGPIO(request, timeout=4.1)

            pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert pin.high is True
            assert pin.extra == extra
            assert pin.timeout == loose_approx(4.1)

    @pytest.mark.asyncio
    async def test_get_gpio(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            with pytest.raises(GRPCError):
                request = GetGPIORequest(name=board.name, pin="pin2")
                await client.GetGPIO(request)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = GetGPIORequest(name=board.name, pin="pin1", extra=dict_to_struct(extra))
            response: GetGPIOResponse = await client.GetGPIO(request, timeout=1.82)
            assert response.high is False

            pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert pin.extra == extra
            assert pin.timeout == loose_approx(1.82)

    @pytest.mark.asyncio
    async def test_pwm(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = PWMRequest(name=board.name, pin="pin1", extra=dict_to_struct(extra))
            response: PWMResponse = await client.PWM(request, timeout=7.86)
            assert response.duty_cycle_pct == 0.0

            pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert pin.extra == extra
            assert pin.timeout == loose_approx(7.86)

    @pytest.mark.asyncio
    async def test_set_pwm(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = SetPWMRequest(name=board.name, pin="pin1", duty_cycle_pct=12.3, extra=dict_to_struct(extra))
            await client.SetPWM(request, timeout=1.213)

            pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert pin.pwm == 12.3
            assert pin.extra == extra
            assert pin.timeout == loose_approx(1.213)

    @pytest.mark.asyncio
    async def test_pwm_frequency(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = PWMFrequencyRequest(name=board.name, pin="pin1", extra=dict_to_struct(extra))
            response: PWMFrequencyResponse = await client.PWMFrequency(request, timeout=182)
            assert response.frequency_hz == 0

            pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert pin.extra == extra
            assert pin.timeout == loose_approx(182)

    @pytest.mark.asyncio
    async def test_set_pwm_freq(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = SetPWMFrequencyRequest(name=board.name, pin="pin1", frequency_hz=123, extra=dict_to_struct(extra))
            await client.SetPWMFrequency(request)

            pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert pin.pwm_freq == 123
            assert pin.extra == extra
            assert pin.timeout is None

    @pytest.mark.asyncio
    async def test_status(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = StatusRequest(name=board.name, extra=dict_to_struct(extra))
            response: StatusResponse = await client.Status(request, timeout=5.55)

            assert response.status == BoardStatus(
                analogs={"reader1": AnalogStatus(value=3)},
                digital_interrupts={"interrupt1": DigitalInterruptStatus(value=0)},
            )
            assert board.extra == extra
            assert board.timeout == loose_approx(5.55)


class TestClient:
    @pytest.mark.asyncio
    async def test_analog_reader_by_name(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            reader = await client.analog_reader_by_name("does not exist")
            assert reader.name == "does not exist"
            with pytest.raises(GRPCError, match=r".*Status.NOT_FOUND.*"):
                await reader.read()

            reader = await client.analog_reader_by_name("reader1")
            assert reader.name == "reader1"

    @pytest.mark.asyncio
    async def test_digital_interrupt_by_name(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            interrupt = await client.digital_interrupt_by_name("dne")
            assert interrupt.name == "dne"
            with pytest.raises(GRPCError, match=r".*Status.NOT_FOUND.*"):
                await interrupt.value()

            interrupt = await client.digital_interrupt_by_name("interrupt1")
            assert interrupt.name == "interrupt1"

    @pytest.mark.asyncio
    async def test_gpio_pin_by_name(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            pin = await client.gpio_pin_by_name("dne")
            assert pin.name == "dne"
            with pytest.raises(GRPCError, match=r".*Status.NOT_FOUND.*"):
                await pin.get()

            pin = await client.gpio_pin_by_name("pin1")
            assert pin.name == "pin1"

    @pytest.mark.asyncio
    async def test_analog_reader_names(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            names = await client.analog_reader_names()
            assert names == ["reader1"]

    @pytest.mark.asyncio
    async def test_digital_interrupt_names(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            names = await client.digital_interrupt_names()
            assert names == ["interrupt1"]

    @pytest.mark.asyncio
    async def test_status(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            status = await client.status(extra=extra, timeout=1.1)
            assert status == BoardStatus(
                analogs={"reader1": AnalogStatus(value=3)},
                digital_interrupts={"interrupt1": DigitalInterruptStatus(value=0)},
            )
            assert board.extra == extra
            assert board.timeout == loose_approx(1.1)

    @pytest.mark.asyncio
    async def test_model_attributes(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            attrs = await client.model_attributes()
            assert attrs == Board.Attributes(remote=True)


class TestGPIOPinClient:
    @pytest.mark.asyncio
    async def test_set(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name("pin1")
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await pin.set(True, extra=extra, timeout=1.82)

            mock_pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert mock_pin.high is True
            assert mock_pin.extra == extra
            assert mock_pin.timeout == loose_approx(1.82)

    @pytest.mark.asyncio
    async def test_get(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name("pin1")
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            high = await pin.get(extra=extra)
            assert high is False
            mock_pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert mock_pin.extra == extra
            assert mock_pin.timeout is None

    @pytest.mark.asyncio
    async def test_set_pwm(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name("pin1")
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await pin.set_pwm(12.3, extra=extra, timeout=3.23)
            mock_pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert mock_pin.pwm == 12.3
            assert mock_pin.extra == extra
            assert mock_pin.timeout == loose_approx(3.23)

    @pytest.mark.asyncio
    async def test_get_pwm(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name("pin1")
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            pwm = await pin.get_pwm(extra=extra, timeout=1.2345)
            assert pwm == 0.0
            mock_pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert mock_pin.extra == extra
            assert mock_pin.timeout == loose_approx(1.2345)

    @pytest.mark.asyncio
    async def test_set_pwm_frequency(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name("pin1")
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await pin.set_pwm_frequency(123, extra=extra, timeout=4.341)
            mock_pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert mock_pin.pwm_freq == 123
            assert mock_pin.extra == extra
            assert mock_pin.timeout == loose_approx(4.341)

    @pytest.mark.asyncio
    async def test_get_pwm_freq(self, board: MockBoard, service: BoardService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name("pin1")
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            freq = await pin.get_pwm_frequency(extra=extra)
            assert freq == 0
            mock_pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert mock_pin.extra == extra
            assert mock_pin.timeout is None

    @pytest.mark.asyncio
    async def test_do(self, board: MockBoard, service: BoardService, generic_service: GenericService):
        async with ChannelFor([service, generic_service]) as channel:
            client = BoardClient(board.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do_command({"command": "args"})
