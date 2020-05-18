from .sensor_type import SensorType

class SensorTypeRepository:
    _sensor_types: dict

    def __init__(self):
        self._sensor_types = {}

    async def register_sensor_type(self, type_name: str, sensor_type: SensorType):
        self._sensor_types[type_name] = sensor_type

    async def fetch_all(self):
        return self._sensor_types

    async def create(self, type_name: str, parameters: dict):
        if type_name not in self._sensor_types:
            raise KeyError('Undefined sensor type "%s"' % type_name)

        return self._sensor_types[type_name].create_reader(parameters)

    async def get_by_type_name(self, type_name) -> SensorType:
        if type_name not in self._sensor_types:
            raise KeyError('Undefined sensor type "%s"' % type_name)

        return self._sensor_types[type_name]
