from .sensor_type import SensorType

class SensorTypeRepository:
    _sensor_types: dict
 
    def __init__(self):
        self._sensor_types = {}

    async def add_sensor_type(self, type_name: str, sensor_class: SensorType):
        self._sensor_types[type_name] = sensor_class
        return

    def create(self, type_name) -> SensorType:
        '''Creates a new SensorType instance and returns it.'''
        if type_name not in self._sensor_types:
            raise KeyError('Undefined sensor type "%s"' % type_name)

        class_name = self._sensor_types[type_name]
        return class_name()
