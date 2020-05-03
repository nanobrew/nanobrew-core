from ...domain.parameter_list import ParameterList
from ...domain.sensor import Sensor
from ...domain.sensor_data_mapper import SensorDataMapper
from ...domain.sensor_type_repository import SensorTypeRepository
from .connection import Connection


class SqliteSensorDataMapper(SensorDataMapper):
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
            sensor_type = await self._sensor_types.create(row['sensor_type'])

            sensors[row['sensor_id']] = Sensor(
                row['sensor_id'],
                row['name'],
                sensor_type,
                ParameterList()
            )

        return sensors

    async def persist(self, sensor: Sensor):
        connection = await self._connection.get_connection()

        await connection.execute(
            'INSERT INTO sensor (sensor_id, sensor_type, name) VALUES (?, ?, ?)',
            (
                sensor.get_id(),
                sensor.get_type_name(),
                sensor.get_name()
            )
        )

        await connection.commit()

        return connection.total_changes > 0
