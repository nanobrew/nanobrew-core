from ..domain.domain_event import DomainEvent
from ..domain.event_listener import EventListener as ListenerInterface
from .event_bus import EventBus


class EventListener(ListenerInterface):
    _event_bus: EventBus

    def __init__(self, event_bus: EventBus):
        self._event_bus = event_bus

    async def raise_event(self, event: DomainEvent):
        await self._event_bus.emit(event.get_name(), event)
