from __future__ import annotations
import logging

from ..base_command import BaseCommand
from ..container import Container
from ...domain.sensor_type import SensorType
from ...domain.sensor_type_repository import SensorTypeRepository

class AddSensorType(BaseCommand):
    type_name: str
    sensor_type: SensorType

    def __init__(self, type_name: str, sensor_type: SensorType):
        self.type_name = type_name
        self.sensor_type = sensor_type

    def get_handler(self, container: Container):
        sensor_types = container.get_service('sensor_types')

        return self.Handler(sensor_types)

    class Handler:
        _sensor_types: SensorTypeRepository

        def __init__(self, sensor_types: SensorTypeRepository):
            self._sensor_types = sensor_types

        async def handle(self, command: AddSensorType):
            return await self._sensor_types.add_sensor_type(command.type_name, command.sensor_type)
