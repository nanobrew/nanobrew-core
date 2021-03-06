from __future__ import annotations

import logging

from ...domain.sensor import Sensor
from ...domain.sensor_repository import SensorRepository
from ...domain.sensor_type_repository import SensorTypeRepository
from ..base_command import BaseCommand
from ..container import Container
from ..error.validation_failed import ValidationFailed


class EditSensor(BaseCommand):
    def __init__(self, sensor_id, name, sensor_type, parameters):
        self._sensor_id = sensor_id
        self._name = name
        self._sensor_type = sensor_type
        self._parameters = parameters

    def get_parameters(self):
        return self._parameters

    def get_name(self):
        return self._name

    def get_sensor_id(self):
        return self._sensor_id

    def get_sensor_type(self):
        return self._sensor_type

    def get_handler(self, container: Container):
        return self.Handler(
            container.get_service('sensors'),
            container.get_service('sensor_types'),
            container.get_service('event_listener')
        )

    class Handler:
        _sensors: SensorRepository
        _sensor_types: SensorRepository

        def __init__(self, sensors: SensorRepository, sensor_types: SensorTypeRepository, event_listener):
            self._sensors = sensors
            self._sensor_types = sensor_types
            self._event_listener = event_listener

        async def handle(self, command: EditSensor):
            sensor = await self._sensors.fetch_by_id(command.get_sensor_id())

            sensor_type = await self._sensor_types.get_by_type_name(command.get_sensor_type())
            options = sensor_type.get_options()
            parameters = command.get_parameters()

            (success, errors) = options.validate(parameters)

            if success != True:
                raise ValidationFailed(errors)

            await sensor.deactivate()

            sensor.rename(command.get_name())
            sensor.update_parameters(options.filter(parameters))
            sensor.change_sensor_type(sensor_type)

            await sensor.persist(self._sensors)
            await sensor.activate(self._event_listener)

            return sensor.get_id()
