from .base_command import BaseCommand
from .container import Container

class CommandBus:
    _container: Container

    def __init__(self, container: Container):
        self._container = container

    async def run_command(self, command: BaseCommand):
        handler = command.get_handler(self._container)

        return await handler.handle(command)