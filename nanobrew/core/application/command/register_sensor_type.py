from __future__ import annotations

from ...distributed.options import Options
from ...distributed.unit import Unit
from ...domain.sensor_type import SensorType
from ...domain.sensor_type_repository import SensorTypeRepository
from ...domain.options import Options as DomainOptions
from ..base_command import BaseCommand
from ..container import Container
from ...domain.unit_factory import UnitFactory


class RegisterSensorType(BaseCommand):
    name: str
    options: Options
    factory: callable
    unit: Unit

    def __init__(self, name: str, options: Options, factory: callable, unit: Unit):
        self.name = name
        self.options = options
        self.factory = factory
        self.unit = unit

    def get_handler(self, container: Container):
        sensor_types = container.get_service('sensor_types')

        return self.Handler(sensor_types)

    class Handler:
        _sensor_types: SensorTypeRepository
        _unit_factory: UnitFactory

        def __init__(self, sensor_types: SensorTypeRepository):
            self._sensor_types = sensor_types
            self._unit_factory = UnitFactory()

        async def handle(self, command: RegisterSensorType):
            unit = self._unit_factory.create_unit(command.unit.get_unit_type())
            options = DomainOptions.from_dict(command.options.to_dict())

            sensor_type = SensorType(
                command.name,
                options,
                command.factory,
                unit
            )

            return await self._sensor_types.register_sensor_type(command.name, sensor_type)
