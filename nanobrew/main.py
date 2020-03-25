import asyncio
import logging
import sys

import nanoinject

from nanobrew.application.command_bus import CommandBus
from nanobrew.application.container import Container
from nanobrew.app import App
from nanobrew.domain.brewery import Brewery
from nanobrew.domain.sensor_list import SensorList
from nanobrew.domain.actor_list import ActorList
from nanobrew.domain.kettle_list import KettleList
from nanobrew.application.plugin_list import PluginList
from nanobrew.entrypoint.http.server import Server

from nanobrew.infrastructure.stub.sensor_repository import StubSensorRepository

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
    app = App(command_bus)

    await init_plugins(app)
    await init_webserver(app)

def get_container():
    container = nanoinject.Container()
    config = nanoinject.Config.from_yaml_file('config/services.yaml')
    config.configure(container)

    return container


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
