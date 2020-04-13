from .sensor_type import SensorType

class SensorTypeRepository:
    _sensor_types: dict
 
    def __init__(self):
        self._sensor_types = {}

    async def add_sensor_type(self, type_name: str, sensor_type: SensorType):
        self._sensor_types[type_name] = sensor_type
        return

    def fetch(self, type_name) -> SensorType:
        if type_name not in self._sensor_types:
            raise KeyError('Undefined sensor type "%s"' % type_name)

        return self._sensor_types[type_name]()
