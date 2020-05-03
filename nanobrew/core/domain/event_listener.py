from .domain_event import DomainEvent


class EventListener:
    def raise_event(self, event: DomainEvent):
        raise NotImplementedError
