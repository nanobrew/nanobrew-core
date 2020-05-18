from ...domain.sensor_type import SensorType


class SensorTypeMapper:
    async def sensor_type_to_dict(self, sensor_type: SensorType):
        return await sensor_type.to_dict()
