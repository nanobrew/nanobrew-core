from aiohttp import web
import asyncio

class Server:
    def __init__(self):
        self.app = web.Application()
        self.app.add_routes([
            web.get('/', self.handle)
        ])

    async def handle(self, request):
        name = request.match_info.get('name', "Anonymous")
        text = "Hello, " + name
        print(text)
        await asyncio.sleep(10)

        return web.Response(text=text)

    def run(self):
        web.run_app(self.app)