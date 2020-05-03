from aiohttp import web

from ....application import CommandBus, QueryBus
from ....application.query.fetch_sensors import FetchSensors

class SensorResource:
    _commands: CommandBus
    _queries: QueryBus

    def __init__(self, commands: CommandBus, queries: QueryBus):
        self._commands = commands
        self._queries = queries

    async def handle_get(self, request):
        sensors = await self._queries.run_query(FetchSensors())

        return web.json_response(sensors)

    async def handle_post(self, request):
        return web.json_response({
        })

    def attach(self, app: web.Application):
        app.add_routes([
            web.get('/sensors', self.handle_get)
        ])

        return app