from ...domain.parameter_list import ParameterList
from ...domain.sensor import Sensor
from ...domain.sensor_repository import SensorRepository
from ...domain.sensor_type_repository import SensorTypeRepository
from .connection import Connection


class SqliteSensorRepository(SensorRepository):
    _sensor_types: SensorTypeRepository
    _connection: Connection

    def __init__(self, connection: Connection, sensor_types: SensorTypeRepository):
        self._sensor_types = sensor_types
        self._connection = connection

    async def fetch_all(self):
        connection = await self._connection.get_connection()
        cursor = await connection.execute_fetchall(
            "SELECT sensor_id, sensor_type, name FROM sensor"
        )

        sensors = {}
        for row in cursor:
            sensor_type = self._sensor_types.fetch(row['sensor_type'])

            sensors[row['sensor_id']] = Sensor(sensor_type, ParameterList({
                'name': row['name'],
                'sensor_id': row['sensor_id'],
                'sensor_type': row['sensor_type'],
            }))

        return sensors
