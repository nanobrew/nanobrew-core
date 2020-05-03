import logging

class EventBus:
    """A generic and simple event dispatcher"""
    _listeners: dict
    _wildcard_listeners: list

    def __init__(self):
        self._listeners = {}
        self._wildcard_listeners = []

    async def attach(self, event_name, listener: callable):
        if event_name not in self._listeners:
            self._listeners[event_name] = []

        self._listeners[event_name].append(listener)

    async def attach_to_all(self, listener: callable):
        self._wildcard_listeners.append(listener)

    async def emit(self, event_name, *args, **kwargs):
        if event_name in self._listeners:
            for callback in self._listeners[event_name]:
                await callback(*args, **kwargs)

        for callback in self._wildcard_listeners:
            await callback(*args, **kwargs)

    async def remove(self, event_name, listener_to_remove: callable):
        if event_name not in self._listeners:
            return

        for key, listener in enumerate(self._listeners[event_name]):
            if listener == listener_to_remove:
                del self._listeners[event_name][key]

    async def remove_from_all(self, listener_to_remove: callable):
        for key, listener in enumerate(self._wildcard_listeners):
            if listener == listener_to_remove:
                del self._wildcard_listeners[key]