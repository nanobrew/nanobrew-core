from __future__ import annotations

from .container import Container

class BaseCommand:
    def get_handler(self, container: Container):
        raise NotImplementedError

    class BaseHandler:
        async def handle(self, command: BaseCommand):
            raise NotImplementedError