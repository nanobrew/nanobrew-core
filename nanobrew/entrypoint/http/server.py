import asyncio
import logging

from aiohttp import web
from aiohttp.web import AppRunner, TCPSite

from nanobrew.app import App as Nanobrew
from nanobrew.config import Config

class Server:
    _web_app: web.Application
    _nanobrew_app = Nanobrew
    _config: Config

    def __init__(self, nanobrew_app: Nanobrew):
        self._nanobrew_app = nanobrew_app
        self._config = nanobrew_app.get_config()
        self._web_app = web.Application()
        self._web_app.add_routes([
            web.get('/', self.handle)
        ])

        self._web_app['nanobrew'] = nanobrew_app

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
