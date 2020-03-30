import asyncio

from .sensor_type import SensorType
from .parameter_list import ParameterList

class Sensor:
    _last: float = 0
    _sensor_type: SensorType = None
    _parameters: ParameterList = None

    def __init__(self, sensor_type: SensorType, parameters: ParameterList):
        self._sensor_type = sensor_type
        self._parameters = parameters

    async def activate(self):
        asyncio.create_task(self._read())

    async def _read(self):
        while True:
            temperature = await self._sensor_type.read(self._sensor_type, self._parameters)
            if temperature != self._last:
                print("Temperature changed to %s" % temperature)

            self._last = temperature
            await asyncio.sleep(5)