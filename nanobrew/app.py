from nanobrew.domain.brewery import Brewery
from nanobrew.domain.sensor_type import SensorType

from .application.base_command import BaseCommand
from .application.command_bus import CommandBus
from .config import Config

class App:
    _sensor_types: dict = {}
    _command_bus: CommandBus
    _config: Config

    def __init__(self, command_bus: CommandBus, config: Config):
        self._command_bus = command_bus
        self._config = config

    async def run_command(self, command: BaseCommand):
        return await self._command_bus.handle(command)
    
    def get_config(self) -> Config:
        return self._config