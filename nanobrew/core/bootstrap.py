import logging

import nanoinject

from .application.command.activate_sensors import ActivateSensors
from .application.command_bus import CommandBus
from .application.config import Config
from .application.container import Container
from .application.event_bus import EventBus
from .application.plugin_list import PluginList
from .application.query_bus import QueryBus
from .entrypoint.http.server import Server

class Bootstrap:
    _commands: CommandBus = None
    _config: Config = None
    _container: Container = None
    _events: EventBus = None
    _queries: QueryBus = None

    async def initialize_plugins(self):
        logging.debug("Initializing plugins")
        plugins = PluginList('plugins.txt')

        await plugins.activate(
            self.get_config(),
            self.get_command_bus(),
            self.get_event_bus(),
            self.get_query_bus()
        )

    async def initialize_webserver(self):
        logging.debug("Initializing webserver")
        server = Server(
            self.get_config(),
            self.get_command_bus(),
            self.get_event_bus(),
            self.get_query_bus()
        )

        await server.run()

    async def activate_sensors(self):
        await self.get_command_bus().run_command(ActivateSensors())

    def get_config(self):
        if self._config is None:
            self._config = Config.from_yaml_file('config/config.yaml')

        return self._config

    def get_container(self):
        if self._container is None:
            container = nanoinject.Container()
            config = nanoinject.Config.from_yaml_file('config/services.yaml')
            config.configure(container)
            self._container = Container(container)

        return self._container

    def get_command_bus(self):
        if self._commands is None:
            self._commands = CommandBus(self.get_container())

        return self._commands

    def get_event_bus(self):
        if self._events is None:
            self._events = EventBus()

        return self._events

    def get_query_bus(self):
        if self._queries is None:
            self._queries = QueryBus()

        return self._queries
