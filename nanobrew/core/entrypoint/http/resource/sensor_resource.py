from aiohttp import web

from ....application import CommandBus, QueryBus
from ....application.error.validation_failed import ValidationFailed
from ....application.query.fetch_sensors import FetchSensors
from ....application.command.add_sensor import AddSensor
from ....application.command.delete_sensor import DeleteSensor

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
        body = await request.json()

        try:
            sensor_id = await self._commands.run_command(AddSensor(body['name'], body['sensor_type'], body['parameters']))

            headers = {
                'Location': '/sensors/' + sensor_id
            }

            return web.json_response(status=201, headers=headers, data={
                'name': body['name'],
                'sensor_type': body['sensor_type'],
                'parameters': body['parameters']
            })

        except ValidationFailed as error:
            return web.json_response(status=422, data={
                'reason': error.get_errors()
            })

    async def handle_delete(self, request):
        sensor_id = request.match_info['sensor_id']

        try:
            await self._commands.run_command(DeleteSensor(sensor_id))
            return web.Response(status=204)

        except KeyError:
            return web.Response(status=404)


    def attach(self, app: web.Application):
        app.add_routes([
            web.get('/sensors', self.handle_get),
            web.post('/sensors', self.handle_post),
            web.delete('/sensors/{sensor_id}', self.handle_delete)
        ])

        return app