
from aiohttp import web

from ....application import CommandBus, QueryBus
from ....application.query.fetch_sensor_types import FetchSensorTypes

class SensorTypeResource:
    _commands: CommandBus
    _queries: QueryBus

    def __init__(self, commands: CommandBus, queries: QueryBus):
        self._commands = commands
        self._queries = queries

    async def handle_get(self, request):
        sensors = await self._queries.run_query(FetchSensorTypes())

        return web.json_response(sensors)

    def attach(self, app: web.Application):
        app.add_routes([
            web.get('/sensor_types', self.handle_get)
        ])

        return app