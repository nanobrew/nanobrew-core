from ...domain.sensor import Sensor
from ...domain.sensor_list import SensorList
from ...domain.sensor_repository import SensorRepository
from ...domain.sensor_type_repository import SensorTypeRepository
from ...domain.parameter_list import ParameterList

class SqliteSensorRepository(SensorRepository):
    _sensor_types: SensorTypeRepository

    def __init__(self, sensor_types: SensorTypeRepository):
        self._sensor_types = sensor_types

    async def fetch_all(self) -> dict:
        sensor_type = self._sensor_types.fetch('dummy')

        return SensorList({
            'dummy sensor #1': Sensor(sensor_type, ParameterList({}))
        })