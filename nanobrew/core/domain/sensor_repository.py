from .sensor_list import SensorList
from .sensor_data_mapper import SensorDataMapper

class SensorRepository:
    '''This class is a caching decorator over concrete repositories'''
    _sensors: dict = {}
    _repository: SensorDataMapper

    def __init__(self, data_mapper: SensorDataMapper):
        self._data_mapper = data_mapper

    async def fetch_all(self):
        if len(self._sensors) == 0:
            self._sensors = await self._data_mapper.fetch_all()

        return self._sensors
