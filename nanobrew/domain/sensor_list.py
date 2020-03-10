from nanobrew.domain.sensor import Sensor

class SensorList:
    _sensors: dict = {}

    def __init__(self, sensors: dict = {}):
        pass

    async def add_sensor(self, sensor_id: str, sensor: Sensor):
        await sensor.activate()

        self._sensors[sensor_id] = sensor


