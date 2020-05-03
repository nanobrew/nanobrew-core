import asyncio

from .event.sensor_value_changed import SensorValueChanged
from .event_listener import EventListener
from .parameter_list import ParameterList
from .sensor_type import SensorType


class Sensor:
    _last: float = 0
    _sensor_id: str = None
    _sensor_name: str = None
    _sensor_type: SensorType = None
    _parameters: ParameterList = None

    def __init__(self, sensor_id, sensor_name, sensor_type: SensorType, parameters: ParameterList):
        self._sensor_id = sensor_id
        self._sensor_name = sensor_name
        self._sensor_type = sensor_type
        self._parameters = parameters

    async def activate(self, listener: EventListener):
        asyncio.create_task(self._read(listener))

    async def _read(self, listener: EventListener):
        while True:
            temperature = await self._sensor_type.read(self._parameters)
            if temperature != self._last:
                await listener.raise_event(
                    SensorValueChanged(
                        self._sensor_id,
                        temperature,
                        self._sensor_type.get_unit()
                    )
                )

            self._last = temperature
            await asyncio.sleep(5)

    async def to_dict(self):
        return {
            'name': self._sensor_name,
            'value': await self._sensor_type.read(self._parameters),
            'unit': self._sensor_type.get_unit().to_dict()
        }
