from nanobrew.domain.sensor_list import SensorList

class SensorRepository:
    async def fetch_all(self) -> SensorList:
        raise NotImplementedError