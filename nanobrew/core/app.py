from .application.base_command import BaseCommand
from .application.container import Container
from .application.command_bus import CommandBus
from .config import Config

class App:
    _sensor_types: dict = {}
    _command_bus: CommandBus
    _config: Config

    def __init__(self, container: Container, command_bus: CommandBus, config: Config):
        self._container = container
        self._command_bus = command_bus
        self._config = config

    async def run_command(self, command: BaseCommand):
        return await self._command_bus.handle(command)

    async def get_sensors(self):
        return []

    async def get_sensor(self, sensor_id):
        return ''
    
    def get_config(self) -> Config:
        return self._config