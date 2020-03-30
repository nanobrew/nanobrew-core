from ...domain.sensor import Sensor


class SensorMapper:
    @classmethod
    def sensor_to_dict(cls, sensor: Sensor):
        return sensor.to_dict()
