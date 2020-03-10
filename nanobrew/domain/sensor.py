import asyncio

from nanobrew.domain.kettle import Kettle
from nanobrew.domain.sensor_type import SensorType
from nanobrew.domain.parameter_list import ParameterList

class Sensor:
    _last: float
    _sensor_type: SensorType
    _parameters: ParameterList
    _kettle: Kettle

    def __init__(self, sensor_type: SensorType, parameters: ParameterList):
        self._sensor_type = sensor_type
        self._parameters = parameters

    async def start(self):
        asyncio.create_task(self._read())

    async def _read(self):
        while True:
            temperature = await self._sensor_type.read()
            if temperature != self._last:

                print("Temperature changed to %s" % temperature)

                if self._kettle is not None:
                    await self._kettle.set_temperature(temperature)

            self.last = temperature
            await asyncio.sleep(0.1)