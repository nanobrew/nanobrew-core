from ..application.container import Container
from .base_query import BaseQuery


class QueryBus:
    _container: Container

    def __init__(self, container: Container):
        self._container = container

    async def run_query(self, query: BaseQuery):
        handler = query.get_handler(self._container)

        return await handler.handle(query)
