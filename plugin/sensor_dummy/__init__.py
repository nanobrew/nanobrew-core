import logging

from nanobrew.core.application.command.add_sensor_type import AddSensorType
from nanobrew.core.domain.parameter import Parameter

from .dummy_sensor_type import DummySensorType

async def activate(commands=None, **kwargs):
    logging.info("Activating dummy sensor plugin")

    # Add the sensor type to the nanobrew interface.
    command = AddSensorType('dummy', DummySensorType)
    await commands.run_command(command)
