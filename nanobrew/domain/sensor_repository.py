from nanobrew.domain.sensor_list import SensorList

class SensorRepository:
    async def findAll(self) -> SensorList:
        raise NotImplementedError