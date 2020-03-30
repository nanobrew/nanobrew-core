from __future__ import annotations

from .container import Container


class BaseQuery:
    def get_handler(self, container: Container):
        raise NotImplementedError

    class Handler:
        async def handle(self, query: BaseQuery):
            raise NotImplementedError
