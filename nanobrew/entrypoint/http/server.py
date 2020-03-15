import asyncio
import logging

from aiohttp import web
from aiohttp.web import AppRunner, TCPSite
from aiohttp_graphql import GraphQLView
from graphene import ObjectType, Schema, String

from nanobrew.entrypoint.http.graphql.root_query import RootQuery

from nanobrew.app import App as Nanobrew

class Server:
    def __init__(self, nanobrew_app: Nanobrew):
        self.web_app = web.Application()
        self.web_app.add_routes([
            web.get('/', self.handle)
        ])

        # @TODO Move this to the graphql module, and have it attach to the app.
        schema = Schema(query=RootQuery)

        GraphQLView.attach(self.web_app, schema=schema, graphiql=True)

        self.web_app['nanobrew'] = nanobrew_app

    async def handle(self, request):
        nanobrew = await request.app['nanobrew'].getName()
        name = request.match_info.get('name', "Anonymous")

        text = "Hello world from %s. Welcome, %s" % (name, nanobrew)
        print(text)
        await asyncio.sleep(0)

        return web.Response(text=text)

    async def run(self):
        runner = AppRunner(self.web_app)
        await runner.setup()

        # @TODO Get this from config.
        host = "0.0.0.0"
        port = 5300

        site = TCPSite(runner, host, port)
        logging.info("Running nanobrew on %s:%d" % (host, port))
        await site.start()
