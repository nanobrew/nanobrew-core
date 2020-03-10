from nanobrew.domain.actor_list import ActorList 
from nanobrew.domain.sensor_list import SensorList
from nanobrew.domain.kettle_list import KettleList

class Brewery:
    _sensors: SensorList
    _actors: ActorList
    _kettles: KettleList

    def __init__(self, sensors: SensorList, actors: ActorList, kettles: KettleList):
        self._sensors = sensors
        self._actors = actors
        self._kettles = kettles