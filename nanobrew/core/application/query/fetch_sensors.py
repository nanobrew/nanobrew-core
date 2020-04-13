from __future__ import annotations

from ...domain.sensor_repository import SensorRepository
from ..base_query import BaseQuery
from ..container import Container
from ..mapper.sensor_mapper import SensorMapper


class FetchSensors(BaseQuery):
    def get_handler(self, container):
        return self.Handler(container.get_service('sensors'))

    class Handler:
        _sensors: SensorRepository

        def __init__(self, sensors: SensorRepository):
            self._sensors = sensors

        async def handle(self, query: FetchSensors):
            sensors = await self._sensors.fetch_all()
            mapper = SensorMapper()

            return {key: await mapper.sensor_to_dict(sensor) for key, sensor in sensors.items()}
