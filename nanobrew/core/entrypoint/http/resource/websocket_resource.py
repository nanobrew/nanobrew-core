import logging

import aiohttp
from aiohttp import web

from ....application import CommandBus, EventBus, QueryBus
from ....application.query.fetch_sensors import FetchSensors


class WebsocketResource:
    _commands: CommandBus
    _events: EventBus
    _queries: QueryBus
    
    def __init__(self, commands: CommandBus, queries: QueryBus, events: EventBus):
        self._commands = commands
        self._queries = queries
        self._events = events

    def attach(self, app: web.Application):
        app.add_routes([
            web.get('/ws', self.websocket_handler)
        ])

        return app

    async def websocket_handler(self, request):
        logging.debug('Websocket handler starting')
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        async def sensor_value_changed(event):
            await ws.send_json(event.to_dict())

        await self._events.attach('sensor_value_changed', sensor_value_changed)

        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                if msg.data == 'close':
                    await ws.close()
                else:
                    await ws.send_str(msg.data + '/answer')
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print('ws connection closed with exception %s' % ws.exception()) 
        print('websocket connection closed')

        return ws

