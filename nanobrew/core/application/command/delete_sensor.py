from __future__ import annotations

from ...domain.sensor_repository import SensorRepository
from ..container import Container


class DeleteSensor:
    sensor_id: str

    def __init__(self, sensor_id):
        self.sensor_id = sensor_id

    def get_handler(self, container: Container):
        return self.Handler(
            container.get_service('sensors')
        )

    class Handler:
        _sensors: SensorRepository

        def __init__(self, sensors: SensorRepository):
            self._sensors = sensors

        async def handle(self, command: DeleteSensor):
            sensor = await self._sensors.fetch_by_id(command.sensor_id)

            await sensor.delete(self._sensors)
