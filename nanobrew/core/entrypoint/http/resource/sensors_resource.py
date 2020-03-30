from aiohttp import web

from ....application import CommandBus, QueryBus

class SensorsResource:
    _commands: CommandBus
    _queries: QueryBus
    
    def __init__(self, commands, queries):
        self._commands = commands
        self._queries = queries

    async def handle_get(self, request):
        return web.json_response({
        })

    async def handle_post(self, request):
        return web.json_response({
        })

    def attach(self, app: web.Application):
        app.add_routes([
            web.get('/sensors', self.handle_get)
        ])

        return app