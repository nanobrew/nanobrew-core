import asyncio
import logging
import sys

import nanoinject
import yaml

from nanobrew.app import App
from nanobrew.application.command.activate_sensors import ActivateSensors
from nanobrew.application.command_bus import CommandBus
from nanobrew.application.container import Container
from nanobrew.application.plugin_list import PluginList
from nanobrew.config import Config
from nanobrew.entrypoint.http.server import Server

async def init_plugins(app: App):
    logging.debug("Initiating plugins")
    plugins = PluginList("plugins.txt")
    await plugins.activate(app)

async def init_webserver(app: App):
    logging.debug("Initiating webserver")
    server = Server(app)
    await server.run()

async def main():
    logging.info("Starting nanobrew")

    container = Container(get_container())
    command_bus = CommandBus(container)
    app = App(command_bus, get_config())

    await init_plugins(app)
    await init_webserver(app)

    await app.run_command(ActivateSensors())

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
