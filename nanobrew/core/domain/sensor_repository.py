from .sensor_list import SensorList

class SensorRepository:
    async def fetch_all(self):
        raise NotImplementedError