from .sensor import Sensor

class SensorList:
    _sensors: dict = {}

    def __init__(self, sensors: dict = {}):
        self._sensors = sensors

    async def add_sensor(self, sensor_id: str, sensor: Sensor):
        self._sensors[sensor_id] = sensor

    def __iter__(self):
        return iter(self._sensors.values())