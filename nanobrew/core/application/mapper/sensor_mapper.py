from ...domain.sensor import Sensor


class SensorMapper:
    async def sensor_to_dict(self, sensor: Sensor):
        return await sensor.to_dict()
