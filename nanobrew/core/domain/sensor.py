import asyncio
import uuid

from .event.sensor_value_changed import SensorValueChanged
from .event_listener import EventListener
from .sensor_type import SensorType


class Sensor:
    _last: float = None
    _sensor_id: str
    _sensor_name: str
    _sensor_type: SensorType
    _parameters: dict
    _reader = None
    _task: asyncio.Task = None

    def __init__(self, sensor_id, sensor_name, sensor_type: SensorType, parameters: dict):
        self._sensor_id = sensor_id
        self._sensor_name = sensor_name
        self._sensor_type = sensor_type
        self._parameters = parameters

    async def persist(self, repository):
        if self._sensor_id is None:
            self._sensor_id = str(uuid.uuid4())

        return await repository.persist(self)

    async def delete(self, repository):
        if self._task is not None:
            self._task.cancel() # Stop the task for this sensor.

        await repository.delete(self)

    def get_id(self):
        return self._sensor_id

    def get_type_name(self):
        return self._sensor_type.get_name()

    def get_name(self):
        return self._sensor_name

    def get_parameters(self):
        return self._parameters

    async def activate(self, listener: EventListener):
        self._task = asyncio.create_task(self._read(listener))

    async def _read(self, listener: EventListener):
        if self._reader is None:
            self._reader = await self._sensor_type.create_reader(self._parameters)

        while True:
            value = await self._reader.read()
            value = round(value, self._sensor_type.get_unit().get_precision())

            if value != self._last:
                await listener.raise_event(
                    SensorValueChanged(self._sensor_id, value, self._sensor_type.get_unit())
                )
                self._last = value

            await asyncio.sleep(5)

    async def to_dict(self):
        precision = self._sensor_type.get_unit().get_precision()

        # This is to prevent an error when the value is requested before the first tick is executed.
        value = round(self._last, precision) if self._last is not None else 0.00

        return {
            'name': self._sensor_name,
            'value': value,
            'type': self._sensor_type.get_name(),
            'unit': self._sensor_type.get_unit().to_dict(),
            'parameters': self._parameters,
        }
