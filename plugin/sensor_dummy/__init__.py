import logging

from nanobrew.core.app import App
from nanobrew.core.application.command.add_sensor_type import AddSensorType
from nanobrew.core.domain.parameter import Parameter

from .dummy import DummySensorType

async def activate(app: App):
    logging.info("Activating dummy sensor plugin")

    # Add the sensor type to the nanobrew interface.
    command = AddSensorType('dummy', DummySensorType)
    await app.run_command(command)
