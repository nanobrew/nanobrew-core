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
            sensor_type = await self._sensor_types.get_by_type_name(row['sensor_type'])

            sensors[row['sensor_id']] = Sensor(
                row['sensor_id'],
                row['name'],
                sensor_type,
                await self._get_parameters(row['sensor_id'])
            )

        return sensors

    async def persist(self, sensor: Sensor):
        connection = await self._connection.get_connection()

        await connection.execute(
            'INSERT INTO sensor (sensor_id, sensor_type, name) VALUES (?, ?, ?)',
            (sensor.get_id(), sensor.get_type_name(), sensor.get_name())
        )

        await self._persist_parameters( sensor.get_id(), sensor.get_parameters())

        await connection.commit()


    async def _persist_parameters(self, sensor_id, parameters):
        connection = await self._connection.get_connection()

        for (name, value) in parameters.items():
            await connection.execute(
                'INSERT INTO sensor_parameter (sensor_id, name, value) VALUES (?, ?, ?)',
                (sensor_id, name, value)
            )

    async def _get_parameters(self, sensor_id: str) -> dict:
        connection = await self._connection.get_connection()
        cursor = await connection.execute_fetchall(
            "SELECT name, value FROM sensor_parameter WHERE sensor_id = ?",
            [sensor_id]
        )

        parameters = {}
        for row in cursor:
            parameters[row['name']] = row['value']

        return parameters
