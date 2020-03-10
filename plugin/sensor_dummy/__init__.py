import logging

from nanobrew.app import App
from nanobrew.domain.config.parameter import Parameter

from .dummy import DummySensorType

async def activate(app: App):
    logging.info("Activating dummy sensor plugin")

    # Add the sensor type to the nanobrew interface.
    await app.add_sensor_type("dummy", DummySensorType)