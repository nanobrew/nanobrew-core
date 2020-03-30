import asyncio
import logging

from aiohttp import web
from aiohttp.web import AppRunner, TCPSite

from ...application.command_bus import CommandBus
from ...application.config import Config
from ...application.event_bus import EventBus
from ...application.query_bus import QueryBus
from .resource.sensors_resource import SensorsResource

class Server:
    _web_app: web.Application

    _config: Config
    _commands: CommandBus
    _events: EventBus
    _queries: QueryBus

    def __init__(self, config: Config, commands: CommandBus, events: EventBus, queries: QueryBus):
        self._commands = commands
        self._events = events
        self._queries = queries
        self._config = config

        self._web_app = self._configure(web.Application(), commands, queries)

        self._web_app.add_routes([
            web.get('/', self.handle),
        ])

    async def handle(self, request):
        text = "Hello world from Nanobrew."
        return web.Response(text=text)

    async def run(self):
        runner = AppRunner(self._web_app)
        await runner.setup()

        host = self._config.get('http.host')
        port = self._config.get('http.port')

        site = TCPSite(runner, host, port)
        logging.info("Running nanobrew on %s:%d" % (host, port))
        await site.start()

    def _configure(self, app: web.Application, commands, queries):
        resources = [
            SensorsResource(commands, queries)
        ]

        for resource in resources:
            resource.attach(app)

        return app