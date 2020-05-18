from nanobrew.core.application.command import RegisterSensorType
from nanobrew.core.distributed.options import Options
from nanobrew.core.distributed.temperature import Temperature

from .dummy_sensor_reader import DummySensorReader


async def create_reader(parameters) -> DummySensorReader:
    return DummySensorReader(
        parameters['start'],
        parameters['step']
    )

async def activate(commands=None, **kwargs):
    options = Options()
    options.add_enum_option(
        True,
        'start',
        'Start',
        'the number to start the dummy sensor with',
        {'1.0': '1.0', '5.0': '5.0', '10.0': '10.0', '25.0': '25.0'}
    )

    options.add_decimal_option(
        True,
        'step',
        'Step',
        'the number the sensor should increase with on each tick'
    )

    await commands.run_command(
        RegisterSensorType("dummy", options, create_reader, Temperature())
    )
