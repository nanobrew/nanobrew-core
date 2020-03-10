from nanobrew.domain.brewery import Brewery
from nanobrew.domain.sensor_type import SensorType

class App:
    _sensor_types: dict = {}

    def __init__(self):
        pass

    async def getName(self):
        return "Nanobrew"

    async def set_brewery(self, brewery: Brewery):
        self._brewery = brewery

    async def add_sensor(self, sensor):
        pass

    async def add_output_type(self, name: str):
        pass

    async def add_sensor_type(self, name, sensor_type: SensorType):
        self._sensor_types[name] = sensor_type

    async def get_sensor_type(self, name):
        if name not in self._sensor_types:
            raise ValueError("Call for undefined sensor type '%s'." % name)

        return self._sensor_types[name]

