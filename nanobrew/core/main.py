import asyncio
import logging
import sys

import nanoinject
import yaml

from .application.command.activate_sensors import ActivateSensors
from .application.command_bus import CommandBus
from .application.config import Config
from .application.container import Container
from .application.event_bus import EventBus
from .application.plugin_list import PluginList
from .application.query_bus import QueryBus
from .entrypoint.http.server import Server

async def init_plugins(config, commands, events, queries):
    logging.debug("Initiating plugins")
    plugins = PluginList("plugins.txt")
    await plugins.activate(config, commands, events, queries)

async def init_webserver(config, commands, events, queries):
    logging.debug("Initiating webserver")
    server = Server(config, commands, events, queries)
    await server.run()

async def main():
    logging.info("Starting nanobrew")

    config = get_config()
    container = Container(get_container())
    command_bus = CommandBus(container)
    event_bus = EventBus()
    query_bus = QueryBus()

    await init_plugins(config, command_bus, event_bus, query_bus)
    await init_webserver(config, command_bus, event_bus, query_bus)

    await command_bus.run_command(ActivateSensors())

def get_container():
    container = nanoinject.Container()
    container_config = nanoinject.Config.from_yaml_file('config/services.yaml')
    container_config.configure(container)

    return container

def get_config():
    return Config.from_yaml_file('config/config.yaml')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
