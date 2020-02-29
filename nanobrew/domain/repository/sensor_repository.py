from nanobrew.domain.sensor import Sensor
from nanobrew.domain.sensor_id import SensorId
from nanobrew.domain.sensor_list import SensorList

class SensorRepository:
    def __init__(self):
        pass

    def findAll(self) -> SensorList:
        pass

    def findOne(self, id: SensorId) -> Sensor:
        pass
