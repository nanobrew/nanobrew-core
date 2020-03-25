from nanobrew.domain.brewery import Brewery
from nanobrew.domain.sensor_type import SensorType

from .application.base_command import BaseCommand
from .application.command_bus import CommandBus

class App:
    _sensor_types: dict = {}
    _command_bus: CommandBus

    def __init__(self, command_bus: CommandBus):
        self._command_bus = command_bus

    async def run_command(self, command: BaseCommand):
        return await self._command_bus.handle(command)
